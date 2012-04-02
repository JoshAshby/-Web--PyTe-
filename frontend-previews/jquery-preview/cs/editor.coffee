$.ajaxSetup {
	cache: false
}

editMode = (mode) ->
	switch mode
		when "python", "Python", "py"
			PythonMode = require("ace/mode/python").Mode;
			window.editor.getSession().setMode(new PythonMode())
		
		when "javascript", "Javascript", "js"
			JavascriptMode = require("ace/mode/javascript").Mode;
			window.editor.getSession().setMode(new JavascriptMode())

		when "Coffeescript", "CoffeeScript", "coffeescript", "coffee", "cs"
			CoffeeMode = require("ace/mode/coffee").Mode;
			window.editor.getSession().setMode(new CoffeeMode())

upload = document.getElementById("openUpload")
if FileReader
	upload.onchange = (e) ->
		e.preventDefault()
		
		file = upload.files[0]
		reader = new FileReader()
		reader.onload = (event) ->
			window.editor.getSession().setValue event.target.result

		reader.readAsText file
		last =(file.name.lastIndexOf ".") + 1
		title = (file.name.lastIndexOf ".")
		fileType = file.name.substr last,file.name.length
		
		docReadWrite()
		
		editMode fileType
		
		$('#uploadFile').close()

docReadOnly = (data) ->
	window.editor.setReadOnly true
	window.readOnly = true
	$('#save').hide()
	$("#readOnly").html "true"

docReadWrite = (data) ->
	window.editor.setReadOnly false
	window.readOnly = false
	$('#save').show()
	$("#readOnly").html "false"

docInfo = (data) ->
	window.author = data.author
	window.fileID = data.hashID
	window.title = data.title
	window.readOnly = data.readOnly
	
	window.editor.getSession().setValue data.programText
	
	$('title').text data.title
	
	$('#title').html data.title
	$('#author').html data.author
	$("#description").html data.description

docSave = (data) ->
	if data.readOnly is false
		stuff = window.editor.getSession().getValue()
		author = $('#author').text()
		title = $('#title').text()
		readOnly = $("#readOnly").text()
		description = $("#description").text()
		$.ajax {
			type: 'PUT'
			url: 'http://localhost/pyte/file/'
			dataType: 'json'
			data: {'file': window.fileID, 'programText': stuff, 'title': title, 'author': author, 'readOnly': readOnly, "description":description}
		}

docSaveAs = (data) ->
	stuff = window.editor.getSession().getValue()
	author = $('#author').text()
	title = $('#title').text()
	description = $("#description").text()
	readOnly = $("#readOnly").text()
	$.ajax {
		type: 'POST'
		url: 'http://localhost/pyte/file/'
		dataType: 'json'
		data: {'programText': stuff, 'title': title, 'author': author, 'readOnly': readOnly, "description":description}
	}
	$("#saveAsDialog").close()
		
$ ->
	height = $("body").height() - 55
	$("#editor").height height
	
	window.editor = ace.edit "editor"
	window.editor.setTheme "ace/theme/vibrant_ink"
	window.editor.getSession().setUseSoftTabs true
	document.getElementById('editor').style.fontSize='12px'
	window.editor.getSession().setTabSize 4
	window.editor.getSession().setUseWrapMode true
	window.editor.setShowPrintMargin true
	
	$.getJSON 'http://localhost/pyte/file/0', (data) =>
		if data.file.readOnly
			docReadOnly()
		docInfo(data.file)
		
	$('#save').click =>
		docSave(window)
	
	$("#saveAsButton").click =>
		docSaveAs(window)
	
	
	
	$.getJSON 'http://localhost/pyte/file/all/', (data) =>
		$("#fileList").append("<li><a id='#{ file.hashID }' href='##{ file.hashID }'>Title: #{ file.title }		Author: #{ file.author }	Description: #{ file.description }</a></li>") for file in data.totals
	
	$("li").click =>
		$.getJSON 'http://localhost/pyte/file/#{ this.id }', (data) =>
		if data.file.readOnly
			docReadOnly()
		docInfo(data.file)