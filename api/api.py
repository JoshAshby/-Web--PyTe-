#!/usr/bin/env python2
"""
{Web: PyTe}
A capstone project by Josh Ashby, 2011-2012
This is the API and background process which the main javascript web app calls on.
This API may do:
	File storing in couchDB
	File downloading to client
	File organization in Projects
	Returning project lists, file lists and files

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
import baseObject

baseObject.urlReset()


@baseObject.route('/')
class index(baseObject.baseHTTPObject):  
	'''
	Simple redirection for when only /pyte/ is accessed
	'''
	def get(self):
		raise web.seeother("pyte/file/")
		

urls += baseObject.urls

app = web.application(urls, globals())
app.internalerror = web.debugerror
		
		
if __name__ == "__main__":
	app.run()