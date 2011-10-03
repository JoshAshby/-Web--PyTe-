$.ajaxSetup {
	cache: false
}

splitResize = (e) ->
	window.editor.resize()

key "ctrl+o", (event, handler) ->
	event.preventDefault()
	if localStorage	
		window.open.center()
		window.open.open()

key "ctrl+a", (event, handler) ->
	event.preventDefault()
	window.about.center()
	window.about.open()

$("#new").click ->
	editNew()
	
$("#open").click ->
	if localStorage
		window.open.center()
		window.open.open()

$("#aboutMenu").click ->
	about()
	
$("#python").click ->
	editMode "Python"
	
$("#javascript").click ->
	editMode "Javascript"
	
$("#coffeescript").click ->
	editMode "Coffeescript"

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
	
	$('#lang').html mode
	$('#statusLang').html mode
		
statusFile = (m) ->
	$('#statusFile').html m
	$('#file').html m
	
editNew = () ->
	window.editor.getSession().setValue ""
	if localStorage
		localStorage.setItem 'file', ''

docSave = () ->
	stuff = window.editor.getSession().getValue()
	if localStorage
		localStorage.setItem 'file', stuff

about = () ->
	window.about.center()
	window.about.open()

waitWindow = (message) ->
	$("#waitInfo").html message
	window.wait.center()
	window.wait.open()

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
				statusFile file.name
		
			when "coffee"
				editMode "cs"
				statusFile file.name
				
			when "py", "pyc"
				editMode "py"
				statusFile file.name
			else
				editMode "txt"
				statusFile "unknown"
			
		$("#fileInfo").hide()
		$("#folderInfo").hide()

conCollapse = (e) ->
	if localStorage
		localStorage.setItem 'consolSplit', false
conExpand = (e) ->
	if localStorage
		localStorage.setItem 'consolSplit', true
mainCollapse = (e) ->
	if localStorage
		localStorage.setItem 'mainSplit', false
mainExpand = (e) ->
	if localStorage
		localStorage.setItem 'mainSplit', true

#Now the initialization after the document is fully loaded.
$ ->
	height = $("body").height() - 90
	$("#consolSplit").height height
	$("#mainSplit").height ((height/4)*3)
	
	window.editor = ace.edit "edit"
	window.editor.setTheme "ace/theme/vibrant_ink"
	window.editor.getSession().setUseSoftTabs true
	document.getElementById('edit').style.fontSize='12px'
	window.editor.getSession().setTabSize 4
	window.editor.getSession().setUseWrapMode true
	window.editor.setReadOnly false
	window.editor.setShowPrintMargin false

	menu = $("#menu").kendoMenu {
		openOnClick: true
	}
	
	window.wait = $("#waitWindow").kendoWindow({
		draggable: false
		resizable: false
		width: "500px"
		height: "300px"
		title: "Please wait"
		modal: true
		actions: ["close"]
		visible: false
	}).data "kendoWindow"
	
	if $("body").width() < 800
		yesorno = true
		waitWindow "Your browser is now under 800px wide, some items have been hidden and the console and sidebar have been collapsed for more editor space. You can open them again if you want or need them."
	else
		yesorno = false
	
	window.consolSplit = $("#consolSplit").kendoSplitter({
		panes: [{
			collapsible: false
		}
		{
			collapsible: true
			size: "#{ height/4 }px"
		}]
		orientation: "vertical"
		expand: conExpand
		collapse: conCollapse
		resize: ->
			splitResize
			setTimeout splitResize, 50
	}).data "kendoSplitter"

	window.mainSplit = $("#mainSplit").kendoSplitter({
		panes: [{
			size: "200px"
			collapsible: true
			collapsed: yesorno
		}
		{
			collapsible: false
		}]
		orientation: "horizontal"
		expand: mainExpand
		collapse: mainCollapse
		resize: ->
			splitResize
			setTimeout splitResize, 50
	}).data "kendoSplitter"

	$("#vertSidebar").kendoTreeView()

	window.about = $("#about").kendoWindow({
		draggable: true
		resizable: false
		width: "500px"
		height: "300px"
		title: "About"
		modal: true
		actions: ["Close"]
		visible: false
	}).data "kendoWindow"
	
	window.open = $("#openWindow").kendoWindow({
		draggable: false
		resizable: false
		width: "500px"
		height: "300px"
		title: "Upload a file to edit"
		modal: true
		actions: ["close"]
		visible: false
	}).data "kendoWindow"
	
	window.welcome = $("#welcomeWindow").kendoWindow({
		draggable: false
		resizable: false
		width: "500px"
		height: "300px"
		title: "Welcome!"
		modal: true
		actions: ["close"]
		visible: false
	}).data "kendoWindow"
	
	if localStorage
		if not window['localStorage'].firstTime
			window.welcome.center()
			window.welcome.open()
			localStorage.setItem 'firstTime', true
			localStorage.setItem 'consolSplit', 'true'
			localStorage.setItem 'mainSplit', 'true'
		
		if window['localStorage'].consolSplit is "true"
			window.consolSplit.expand "#consoleMain"
		else
			window.consolSplit.collapse "#consoleMain"
		
		if window['localStorage'].mainSplit is "true"
			window.mainSplit.expand "#sidebar"
		else
			window.mainSplit.collapse "#sidebar"
		
		if window['localStorage'].lex
			editMode window['localStorage'].lex
		else
			editMode "py"
		
		if window['localStorage'].file
			window.editor.getSession().setValue window['localStorage'].file
			$("#fileInfo").hide()
			$("#folderInfo").hide()
		
		if window['localStorage'].fileName
			statusFile window['localStorage'].fileName
		else
			statusFile "untitled"
		
		window.editor.getSession().on 'change', ->
			docSave()
		
	else
		statusFile "untitled"
		editMode "py"
	
	$("#consoleMain").console()
	$("#consoleControl").consoleControl()
	
	$(window).bind "resize", ->
		if $("body").width() <= 800
			window.mainSplit.collapse "#sidebar"
			waitWindow "Your browser is now under 800px wide, some items have been hidden and the sidebar has been collapsed for more editor space. You can open them again if you want or need them."
		else
			if window['localStorage'].consolSplit
				window.consolSplit.expand "#consoleMain"
			else
				window.consolSplit.collapse "#consoleMain"
			if window['localStorage'].mainSplit
				window.mainSplit.expand "#sidebar"
			else
				window.mainSplit.collapse "#sidebar"