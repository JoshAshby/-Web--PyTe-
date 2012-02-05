#!/usr/bin/env python2
"""
{Web: PyTe}
A capstone project by Josh Ashby, 2011-2012

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import web
import json
'''
From: http://webpy.org/install and http://code.google.com/p/modwsgi/wiki/ApplicationIssues
This must be done to avoid the import errors which come up with having linear.py and config.py
'''
try:
	from configSub import *
except:
	import sys, os
	abspath = os.path.dirname(__file__)
	sys.path.append(abspath)
	os.chdir(abspath)
from configSub import *

from baseDocument import fileDoc
from baseView import fileView

urls = (
	"", "slash",
	"/(.*)/", "file"
)

class file:
	'''
	class documentation
	
	Retrieves and returns the information about a file.
	'''
	def getFunc(self, **kwargs):	
		'''
		function documentation
		
		GET verb call
		
		Returns:
			
		'''
		#Go through and make sure we're not in testing mode, in which case the unit tests will pass the barcode instead...
		try:
			wi = web.input()
			file = wi['file']
		except:
			file = kwargs['file']
		
		file = fileDoc.view("files/admin", key=bar).first()
		
		file = dict(file)
		
		view = fileView.fileView(file, wi)
		
		return view.returnData()
	
	def postFunc(self, **kwargs):
		'''
		function documentation
		
		POST verb call
		
		Returns:
			
		'''
		pass
	
	def putFunc(self, **kwargs):
		'''
		function documentation
		
		PUT verb call
		
		Returns:
			
		'''
		pass
	
	def deleteFunc(self, **kwargs):
		'''
		function documentation
		
		DELETE verb call
		
		Returns:
			
		'''
		pass
	
	def GET(self):
		return self.getFunc()
	
	def POST(self):
		return self.postFunc()
	
	def PUT(self):
		return self.putFunc()
	
	def DELETE(self):
		return self.deleteFunc()


app = web.application(urls, globals(), autoreload=False)
#application = app.wsgifunc()