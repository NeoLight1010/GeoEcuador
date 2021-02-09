extends Control

var selection = 0

onready var label_puntaje = $MarginContainer/CenterContainer/VBoxContainer/PuntajeFinal

func _process(_u_delta):
	var puntaje_final = $"/root/Main".params["TriviaGameOverDisplay"]["score"]
	label_puntaje.text = "Puntaje final: " + str(puntaje_final)
	
	if Input.is_action_just_pressed("ui_accept"):
		handle_selection(selection)

func handle_selection(_selection):
	if selection == 0:
		var root = get_node("/root/Main")
		root.change_scene("TriviaMenuDisplay")
