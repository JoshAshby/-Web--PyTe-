#!/usr/bin/env python
"""
{Web: PyTe}
A capstone project by Josh Ashby, 2011-2012
Manages a project portfolio

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
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
from config import *
from baseDocument import projectDoc
from baseView import projectView
import baseObject

baseObject.urlReset()


@baseObject.route("/(.*)")
class projectObject(baseObject.baseHTTPObject):
	'''
	Can be called with api urls like so:
		/pyte/project/1
		/pyte/project/1/
		/pyte/project/?project=1
	
	get - Retrieves and returns the information about the given project.
	post - Creates a new project
	put - Updates the projects portfolio
	delete - Deletes the given projects portfolio
	'''
	def get(self):	
		'''
		GET verb call
		
		Returns:
			JSON/HTML/PDF view of the data.
		'''
		projectID = int(self.hasMember('project'))
		
		projectData = projectDoc.view("project/admin", key=projectID).first()
		
		projectData = dict(projectData)
		
		view = projectView(data=projectData)
		
		return view.returnData()

	def post(self):
		'''
		POST verb call
		
		Returns:
			JSON/HTML/PDF view of the data.
		'''
		projectID = int(self.hasMember('project'))
		author = self.hasMember('author')
		description = self.hasMember('description')
		name = self.hasMember('name')
		files = self.hasMember('files').join(',')
		
		projectData = projectDoc(hashID=projectID, author=author, description=description, name=name, files=files)
		
		projectData.save()
		
		projectData = projectDoc.view("project/admin", key=projectID).first()
		
		projectData = dict(projectData)
		projectData['update'] = True
		
		view = projectView(data=projectData)
		return view.returnData()
	
	def put(self):
		'''
		PUT verb call
		
		Returns:
			JSON/HTML/PDF view of the dat
		'''
		projectID = int(self.hasMember('project'))
		description = self.hasMember('description')
		author = self.hasMember('author')
		name = self.hasMember('name')
		files = self.hasMember('files').join(',')
		
		phashID = projectDoc().view('project/admin', key=projectID).first()['_id']
		
		projectData = projectDoc().get(phashID)
		projectData.description = description
		projectData.name = name
		projectData.author = author
		projectData.files = files
		
		projectData.save()
		
		projectData = projectDoc.view("project/admin", key=projectID).first()
		
		projectData = dict(projectData)
		projectData['save'] = True
		
		view = projectView(data=projectData)
		return view.returnData()
	
	def delete(self):
		'''
		DELETE verb call
		
		Goes through and tells the database to delete the given document
			And returns the data with value 'delete' as true
		
		Returns:
			JSON/HTML/PDF view of the dat
		'''
		projectID = int(self.hasMember('project'))
		
		name = database.view("project/admin", key=projectID).first()['value']
		
		name['delete'] = 'true'
		
		a = name['_id']
		
		database.delete_doc(a)
	
		projectData = dict(name)
		
		view = projectView(data=projectData)
		return view.returnData()


app = web.application(baseObject.urls, globals())