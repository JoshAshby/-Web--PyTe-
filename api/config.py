#!/usr/bin/env python
"""
{Web: PyTe}
A capstone project by Josh Ashby, 2011-2012
Main app config file for URL's

http://xkcd.com/353/

Josh Ashby
2011
http://joshashby.com
joshuaashby@joshashby.com
"""
try:
	from configSub import *
except:
	import sys, os
	abspath = os.path.dirname(__file__)
	sys.path.append(abspath)
	os.chdir(abspath)
from configSub import *
import web

import file

urls = (
	'/', 'index',
	'/', file.app
)