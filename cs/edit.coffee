edit = edit or {}

edit.ajaxLoad = (data) ->
	$.ajax {
		url: "api/file/"
		type: "GET"
		dataType: 'json'
		data: data
		success: (dataReturn) ->
			window.editor.getSession().setValue dataReturn["file"]
			$('#status').html "Loaded" + dataReturn["name"]
			$('#statusFile').html dataReturn['name']
		}

edit.ajaxSave = (data) ->
	$.ajax {
		url: "api/file/"
		type: "PUT"
		dataType: "json"
		data: data
		success: (dataReturn) ->
			$('#status').html "Saved" + dataReturn["name"]
			$('#statusFile').html dataReturn['name']
		}

edit.ajaxSaveAs = (data) ->
	$.ajax {
		url: "api/file/"
		type: "POST"
		dataType: "json"
		data: data
		success: (dataReturn) ->
			$('#status').html "Saved" + dataReturn["name"]
			$('#statusFile').html dataReturn['name']
		}