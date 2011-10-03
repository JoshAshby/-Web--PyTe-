window.console = 0
$ = jQuery
$.fn.extend
	console: (options) ->
		self = $.fn.console
		opts = $.extend {}, self.default_options, options
		$(this).each (i, el) ->
			self.init el, opts
	consoleControl: (options) ->
		self = $.fn.consoleControl
		opts = $.extend {}, self.default_options, options
		$(this).each (i, el) ->
			self.init el, opts

$.extend $.fn.console,
	default_options:
		log: true
	
	init: (el, opts) ->
		$(el).html "<div id='conTop'>Javascript Console</div><div id='conMid'><ul id='consoleReply'><div id='gutterMid'></div></ul></div>"
		
		window.console = $("#consoleReply")
		
		addLine "Welcome to the javascript console"
		addLine "Start typing commands into the status bar's 'Console' section"
		addLine "As you enter commands, they will show up here, and the output will to."
		addLine "The only thing to note is that this list prepends"
		addLine "meaning the latest result is always at the top and the oldest is at the bottom."
	
	log: (opts) ->
		addline opts[0]
		reply = eval opts[0]
		addLine reply

$.extend $.fn.consoleControl,
	default_options:
		log: true
	
	init: (el, opts) ->
		$(el).html "<input type='text' id='consoleBar'></input><div id='consoleSub'>GO!</div>"
		
		
		$("#consoleSub").click ->
			stuff = $("#consoleBar").val()
			if stuff isnt ""
				addLine stuff
				$("#consoleBar").val ""
				reply = eval stuff
				addLine ("		" + reply)
	
addLine = (message) ->
	num = window.console.children().length 
	window.console.prepend "<li><span class='num'>#{ num }</span>> #{ message }</li>"