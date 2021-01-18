extends Area2D
class_name Provincia

signal Provincia_click(provincia)

export(String) var province_name
export(PackedScene) var Polygon
export(String) var DataJSON = "res://data/provincias/provincias.json"

var mouse_over = false
var has_own_info_label = false

# Data variables
var data
var description
var capital

func _ready():
	var root_node = get_tree().root.get_children()[0]
	connect("Provincia_click", root_node, "_on_Provincia_click")

	# Set default Script Variables.
	if Polygon:
		remove_child($CollisionShape2D)
		add_child(Polygon.instance())

	if not province_name:
		province_name = name


func _on_Provincia_input_event(_viewport, event, _shape_idx):	
	if event is InputEventMouseButton and event.button_index == BUTTON_LEFT \
			&& event.pressed:
				
		emit_signal("Provincia_click", self)
		


###################

func read_data_json(path):
	var file = File.new()
	var json

	file.open(path, File.READ)
	json = file.get_as_text()
	file.close()

	return JSON.parse(json).result
