extends Panel

onready var province_name = get_node("/root/Main").params["InfoDisplay"]["province_name"]
onready var data = get_node("/root/Main").params["InfoDisplay"]["data"]

onready var Header = $MainVBox/Header
onready var Body = $MainVBox/Body

onready var Title = $MainVBox/Header/Center/Title
onready var Capital = Body.get_node("Scroll/DataVBox/Capital")
onready var Description = Body.get_node("Scroll/DataVBox/Description")
onready var ImageNode = Body.get_node("Scroll/DataVBox/Image")

func _ready():
	Title.text = province_name
	Capital.text = "Capital: " + data['Capital']
	Description.text = Provincia.new().read_description_txt(data['Descripción'])
	ImageNode.texture = Provincia.new().load_image(data['Imagen'])


func _on_Button_pressed():
	var Main = $"/root/Main"
	
	Main.change_scene("MapDisplay")
