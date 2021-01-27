extends Panel

onready var province_name = get_node("/root/Main").params["InfoDisplay"]["province_name"]
onready var data = get_node("/root/Main").params["InfoDisplay"]["data"]

onready var Title = $MarginContainer/ScrollContainer/VBoxContainer/Title
onready var Capital = $MarginContainer/ScrollContainer/VBoxContainer/Capital
onready var Description = $MarginContainer/ScrollContainer/VBoxContainer/Description
onready var ImageNode = $MarginContainer/ScrollContainer/VBoxContainer/Image

func _ready():
	Title.text = province_name
	Capital.text = "Capital: " + data['Capital']
	Description.text = Provincia.new().read_description_txt(data['Descripción'])
	ImageNode.texture = Provincia.new().load_image(data['Imagen'])
