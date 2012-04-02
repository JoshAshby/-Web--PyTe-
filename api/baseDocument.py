#!/usr/bin/env python
"""
{Web: PyTe}
A capstone project by Josh Ashby, 2011-2012
Database ORM design objects for use with the APP for more Pythonic database interaction.

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import json
import web
import sys
import os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
from config import *
import couchdbkit

databaseName = 'pyte'

database = couchdbkit.Server()[databaseName]


class fileDoc(couchdbkit.Document):
	"""
	ORM for the fileDoc doc_type document in couch.
	Provides a more Pythonic way of working with the database.
	"""
	hashID = couchdbkit.IntegerProperty()
	title = couchdbkit.StringProperty()
	description = couchdbkit.StringProperty()
	programText = couchdbkit.StringProperty()
	
	docType = "fileDoc"

fileDoc.set_db(database)

class projectDoc(couchdbkit.Document):
	"""
	ORM for the projectDoc doc_type document in couch.
	Provides a more Pythonic way of working with the database.
	"""
	hashID = couchdbkit.IntegerProperty()
	name = couchdbkit.StringProperty()
	description = couchdbkit.StringProperty()
	fileIDs = couchdbkit.ListProperty()
	
	docType = "projectDoc"

projectDoc.set_db(database)
