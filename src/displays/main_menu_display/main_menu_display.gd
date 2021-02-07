# Trivia Menu.
extends MarginContainer

onready var selector_uno = $VBoxContainer/VBoxContainer/HBoxInicar/Selector
onready var selector_dos = $VBoxContainer/VBoxContainer/HBoxSalir/Selector

var current_selection = 0

func _ready():
	set_current_selection(0)

func _process(_u_delta):
	if Input.is_action_just_pressed("ui_down") and current_selection < 1:
		current_selection += 1
		set_current_selection(current_selection)
	elif Input.is_action_just_pressed("ui_up") and current_selection > 0:
		current_selection -= 1
		set_current_selection(current_selection)
	elif Input.is_action_just_pressed("ui_accept"):
		handle_selection(current_selection)

func handle_selection(_current_selection):
	if _current_selection == 0:
		var root = get_node("/root/Main")
		root.change_scene("MapDisplay")
	elif _current_selection == 1:
		var root = get_node("/root/Main")
		root.change_scene("TriviaMenuDisplay")

func set_current_selection(_current_selection):
	selector_uno.text = ""
	selector_dos.text = ""
	if _current_selection == 0:
		selector_uno.text = ">"
	elif _current_selection == 1:
		selector_dos.text = ">"
