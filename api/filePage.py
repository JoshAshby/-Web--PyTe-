#!/usr/bin/env python
"""
{Web: PyTe}
A capstone project by Josh Ashby, 2011-2012
Manages files within a project.

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import web
import json
import sys
import os
import random
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
from config import *
from baseDocument import fileDoc, database
from baseView import fileView,errorView,totalView
import baseObject

baseObject.urlReset()

hashChoice = "0123456789"


@baseObject.route("/all/")
class fileTotalObject(baseObject.baseHTTPObject):
	'''
	Can be called with api urls like so:
		/pyte/file/1
		/pyte/file/1/
		/pyte/file/?file=1
	
	get - Retrieves and returns the hashID, title, description, and author and readOnly of all the files
	'''
	def get(self):	
		'''
		GET verb call
		
		Returns:
			JSON/HTML/PDF view of the data.
		'''
		name = database.view("file/admin").all()
		
		for i in range(len(name)):
			name[i] = name[i]['value']
		
		totals = {'data': name}
		
		total = dict(totals)
		
		view = totalView(data=total)
		return view.returnData()


@baseObject.route("/(.*)")
class fileObject(baseObject.baseHTTPObject):
	'''
	Can be called with api urls like so:
		/pyte/file/1
		/pyte/file/1/
		/pyte/file/?file=1
	
	get - Retrieves and returns the information about the given file.
	post - Create a new file with the given information.
	put - Updates the given file with the new information,
		this would be used for everytime something saves a file
	delete - Deletes the given file.
	'''
	def get(self):	
		'''
		GET verb call
		
		Returns:
			JSON/HTML/PDF view of the data.
		'''
		fileID = int(self.hasMember('file'))
		
		fileData = fileDoc.view("file/admin", key=fileID).first()
		
		fileData = dict(fileData)
		
		view = fileView(data=fileData)
		return view.returnData()
	
	def put(self):
		'''
		POST verb call
		
		Returns:
			JSON/HTML/PDF view of the data.
		'''
		fileID = int(self.hasMember('file'))
			
		author = self.hasMember('author')
		programText = self.hasMember('programText')
		title = self.hasMember('title')
		readOnly = self.hasMember('readOnly')
		if readOnly is "true":
			data = {"error": "ReadOnly file", "missing": "false readOnly"}
			view = errorView(data=data)
			return view.returnData()
		else:
			readOnly = False
		
		fileData = fileDoc(hashID=fileID, author=author, programText=programText, title=title, readOnly=readOnly)
		
		fileData.save()
		
		fileData = fileDoc.view("file/admin", key=fileID).first()
		
		fileData = dict(fileData)
		fileData['update'] = True
		
		view = fileView(data=fileData)
		return view.returnData()
	
	def post(self):
		'''
		PUT verb call
		
		Returns:
			JSON/HTML/PDF view of the data
		'''
		fileID = ''.join(random.choice(hashChoice) for i in range(10))
		
		programText = self.hasMember('programText')
		author = self.hasMember('author')
		title = self.hasMember('title')
		readOnly = self.hasMember('readOnly')
		
		if readOnly is "true":
			readOnly = True
		else:
			readOnly = False
		
		fileData = fileDoc(hashID=int(fileID))
		fileData.programText = programText
		fileData.title = title
		fileData.author = author
		fileData.readOnly = readOnly
		
		fileData.save()
		
		fileData = fileDoc.view("file/admin", key=fileID).first()
		
		fileData = dict(fileData)
		fileData['save'] = True
		
		view = fileView(data=fileData)
		return view.returnData()
	
	def delete(self):
		'''
		DELETE verb call
		
		Goes through and tells the database to delete the given document
			And returns the data with value 'delete' as true
		
		Returns:
			JSON/HTML/PDF view of the dat
		'''
		fileID = int(self.hasMember('file'))
		
		name = database.view("file/admin", key=fileID).first()['value']
		
		name['delete'] = True
		
		a = name['_id']
		
		database.delete_doc(a)
	
		fileData = dict(name)
		
		view = fileView(data=fileData)
		return view.returnData()


app = web.application(baseObject.urls, globals())