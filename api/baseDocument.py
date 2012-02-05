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

import couchdbkit

databaseName = 'pyte'

database = couchdbkit.Server()[databaseName]

class fileDoc(couchdbkit.Document):
	hash = couchdbkit.StringProperty()
	title = couchdbkit.StringProperty()
	programText = couchdbkit.StringProperty()
	
	doc_type = "fileDoc"

fileDoc.set_db(database)

class projectDoc(couchdbkit.Document):
	hash = couchdbkit.StringProperty()
	name = couchdbkit.StringProperty()
	files = couchdbkit.DictProperty()
	
	doc_type = "projectDoc"

projectDoc.set_db(database)