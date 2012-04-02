#!/usr/bin/env python
"""
{Web: PyTe}
A capstone project by Josh Ashby, 2011-2012

For more information, see: https://github.com/JoshAshby/House-Inventory-API

http://xkcd.com/353/

Josh Ashby
2011
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


class baseView(object):
	'''
	Used as a design object for specific views. It takes care of determining which type
		of view to return (PDF, HTML, or JSON).
		(The default is JSON)
	
	New views should inherit this object to automate the routing process.
	
	New views should over-ride JOSN, HTML, and PDF functions, and to return what the view
		produced, one should use: return view.returnData()
	'''
	def __init__(self, **kwargs):
		self.data = kwargs['data']
		
		self.t = 'json'
		
		if 't' in kwargs: self.t = kwargs['t']
		if 'wi' in kwargs:
			if 't' in kwargs['wi']: self.t = kwargs['wi']['t']
		if 't' in web.input(): self.t = web.input()
		
		if self.t == 'html':
			self.inform = self.HTML()
		elif self.t == 'json':
			self.inform = self.JSON()
		elif self.t == 'pdf':
			self.inform = self.PDF()
	
	def PDF(self):
		pass
		
	def HTML(self):
		pass
		
	def JSON(self):
		pass
	
	def returnData(self):
		return self.inform


class totalView(baseView):
	'''
	Returns JSON, HTML or PDF formating of the file information
	'''
	def JSON(self):
		for i in self.data['data']:
			i.pop("doc_type")
			i.pop("_rev")
			i.pop("docType")
			i.pop("_id")
		web.header('Content-Type', 'application/json')
		return json.dumps({'totals': self.data['data']})
		

class fileView(baseView):
	'''
	Returns JSON, HTML or PDF formating of the file information
	'''
	def JSON(self):
		self.data.pop('docType')
		web.header('Content-Type', 'application/json')
		return json.dumps({'file': self.data})


class projectView(baseView):
	'''
	Returns JSON, HTML or PDF formating of the project information
	'''
	def JSON(self):
		self.data.pop('docType')
		web.header('Content-Type', 'application/json')
		return json.dumps({"project": self.data})


class errorView(baseView):
	'''
	Returns JSON, HTML or PDF formating of the given error, and what data might be missing.
	'''
	def JSON(self):
		web.header('Content-Type', 'application/json')
		return json.dumps({"error": self.data['error'], 'missing': self.data['missing']})