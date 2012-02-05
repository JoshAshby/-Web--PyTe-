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

class baseView(object):
	def __init__(self, data, wi):
		self.data = data
		
		if 't' in wi: t = wi['t']
		else: t = 'json'
		
		if t == 'html':
			inform = self.HTML()
		elif t == 'json':
			inform = self.JSON()
		elif t == 'pdf':
			inform = self.PDF()
			
		self.inform = inform
	
	def PDF(self):
		pass
		
	def HTML(self):
		pass
		
	def JSON(self):
		pass
	
	def returnData(self):
		return self.inform

class fileView(baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'file': self.data})

class projectView(baseView):
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({'project': self.data})