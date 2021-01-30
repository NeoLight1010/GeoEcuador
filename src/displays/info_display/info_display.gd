extends Panel

onready var province_name = get_node("/root/Main").params["InfoDisplay"]["province_name"]
onready var data = get_node("/root/Main").params["InfoDisplay"]["data"]

onready var Title = $MainVBox/Header/Center/Title
onready var Capital = $MainVBox/Body/DataVBox/Capital
onready var Description = $MainVBox/Body/DataVBox/Description
onready var ImageNode = $MainVBox/Body/DataVBox/Image

func _ready():
	Title.text = province_name
	Capital.text = "Capital: " + data['Capital']
	Description.text = Provincia.new().read_description_txt(data['Descripción'])
	ImageNode.texture = Provincia.new().load_image(data['Imagen'])
