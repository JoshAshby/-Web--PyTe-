#!/usr/bin/env python
"""
{Web: PyTe}
A capstone project by Josh Ashby, 2011-2012
This is the API and background process which the main javascript web app calls on.
This API does:
	File storing in couchDB
	File downloading to client
	File organization in Projects
	Returning project lists, file lists and files

http://xkcd.com/353/

Josh Ashby
2011
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
from config import *
from configSub import *

app = web.application(urls, globals())

class index:        
	'''
	class documentation
	'''
	def getFunc(self):
		return render.index()
	
	def postFunc(self):
		return render.index()
	
	def putFunc(self):
		return render.index()
	
	def deleteFunc(self):
		return render.index()
	
	def GET(self):
		return self.getFunc()
		
	def POST(self):
		return self.postFunc()
	
	def DELETE(self):
		return self.deleteFunc()
	
	def PUT(self):
		return self.putFunc()
		
if __name__ == "__main__":
	app.run()

#wsgi stuff
#app = web.application(urls, globals(), autoreload=False)
#application = app.wsgifunc()
