extends Panel

onready var province_name = get_node("/root/Main").params["InfoDisplay"]["province_name"]
onready var data = get_node("/root/Main").params["InfoDisplay"]["data"]

onready var Title = $MarginContainer/ScrollContainer/VBoxContainer/Title
onready var Capital = $MarginContainer/ScrollContainer/VBoxContainer/Capital
onready var Description = $MarginContainer/ScrollContainer/VBoxContainer/Description

func _ready():
	Title.text = province_name
	Capital.text = data['Capital']
	Description.text = data['Descripción']
