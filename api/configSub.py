#!/usr/bin/env python2
"""
{Web: PyTe}
A capstone project by Josh Ashby, 2011-2012
Sub-App config files

http://xkcd.com/353/

Josh Ashby
2012
http://joshashby.com
joshuaashby@joshashby.com
"""
import web

debug = 0

class slash:
	def GET(self): raise web.seeother("/")