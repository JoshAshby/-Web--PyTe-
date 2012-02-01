$.ajaxSetup {
	cache: false
}

editMode = (mode) ->
	switch mode
		when "python", "Python", "py"
			PythonMode = require("ace/mode/python").Mode;
			window.editor.getSession().setMode(new PythonMode())
			if localStorage
				localStorage.setItem 'lex', 'py'
			mode = "Python"
		
		when "javascript", "Javascript", "js"
			JavascriptMode = require("ace/mode/javascript").Mode;
			window.editor.getSession().setMode(new JavascriptMode())
			if localStorage
				localStorage.setItem 'lex', 'js'
			mode = "Javascript"

		when "Coffeescript", "CoffeeScript", "coffeescript", "coffee", "cs"
			CoffeeMode = require("ace/mode/coffee").Mode;
			window.editor.getSession().setMode(new CoffeeMode())
			if localStorage
				localStorage.setItem 'lex', 'cs'
			mode = "CoffeeScript"
			
editNew = () ->
	window.editor.getSession().setValue ""
	if localStorage
		localStorage.setItem 'file', ''

docSave = () ->
	stuff = window.editor.getSession().getValue()
	if localStorage
		localStorage.setItem 'file', stuff

upload = document.getElementById("openUpload")
if FileReader
	upload.onchange = (e) ->
		e.preventDefault()
		
		file = upload.files[0]
		reader = new FileReader()
		reader.onload = (event) ->
			window.editor.getSession().setValue event.target.result
			if localStorage
				localStorage.setItem 'file', event.target.result
		reader.readAsText file
		last =(file.name.lastIndexOf ".") + 1
		fileType = file.name.substr last,file.name.length
		
		if localStorage
			localStorage.setItem 'fileName', file.name
			
		switch fileType
			when "json", "js"
				editMode "js"
		
			when "coffee"
				editMode "cs"
				
			when "py", "pyc"
				editMode "py"
			else
				editMode "txt"

$ ->
	height = $("body").height() - 120
	$("#editor").height height
	$("#consoleArea").height height
	
	window.editor = ace.edit "editor"
	window.editor.setTheme "ace/theme/vibrant_ink"
	window.editor.getSession().setUseSoftTabs true
	document.getElementById('editor').style.fontSize='12px'
	window.editor.getSession().setTabSize 4
	window.editor.getSession().setUseWrapMode true
	window.editor.setReadOnly false
	window.editor.setShowPrintMargin true
			
	editMode "py"
			
	$("#consoleMain").console()
	$("#consoleControl").consoleControl()
	