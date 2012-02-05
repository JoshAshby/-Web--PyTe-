#!/usr/bin/env python2
"""
{Web: PyTe}
A capstone project by Josh Ashby, 2011-2012
Main app config file for URL's

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import web

try:
	from configSub import *
except:
	import sys, os
	abspath = os.path.dirname(__file__)
	sys.path.append(abspath)
	os.chdir(abspath)
from configSub import *


import file
import project

urls = (
	'/', 'index',
	'/file/', file.app,
	'/project/', project.app
)