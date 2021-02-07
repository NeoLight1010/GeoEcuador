extends Control

var selection = 0

func _process(_u_delta):
	if Input.is_action_just_pressed("ui_accept"):
		handle_selection(selection)

func handle_selection(_selection):
	if selection == 0:
		var root = get_node("/root/Main")
		root.change_scene("TriviaMenuDisplay")
