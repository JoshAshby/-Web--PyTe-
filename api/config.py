#!/usr/bin/env python
"""
{Web: PyTe}
A capstone project by Josh Ashby, 2011-2012
Main app config file for URL's and other common utilies that don't have a home

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
import couchdbkit
import filePage
import projectPage

base = '/pyte/'

urls = (
	(base + 'file'), filePage.app,
	(base + 'project'), projectPage.app
)

hashChoice = "0123456789"

class slash:
	'''
	Simply is used to make sure that everything that isn't slashed is
	'''
	def GET(self): raise web.seeother("/")
