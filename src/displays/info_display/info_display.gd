extends Control

onready var province_name = get_node("/root/Main").params["InfoDisplay"]["province_name"]
onready var data = get_node("/root/Main").params["InfoDisplay"]["data"]

onready var Header = $MainVBox/Header
onready var Body = $MainVBox/Body

onready var Title = $MainVBox/Header/Center/Title
onready var Capital = Body.get_node("Scroll/DataVBox/Capital")
onready var Venues = Body.get_node("Scroll/DataVBox/Venues")
onready var Description = Body.get_node("Scroll/DataVBox/Description")
onready var ImageNode = Body.get_node("Scroll/DataVBox/Image")


func _ready():
	Title.text = province_name
	Capital.text = "Capital: " + data['Capital']
	Venues.text = "Puntos/eventos de interés: " + join_array(", ", data["Puntos de Interés"])
	Description.text = Provincia.new().read_description_txt(data['Descripción'])
	ImageNode.texture = Provincia.new().load_image(data['Imagen'])


func _on_Button_pressed():
	var Main = $"/root/Main"
	
	Main.change_scene("MapDisplay")


func join_array(delimiter, arr):
	var string = ""
	
	var i = 0
	for element in arr:
		if i != len(arr) - 1:
			string += element + delimiter
		else:
			string += element
		i += 1
	return string
