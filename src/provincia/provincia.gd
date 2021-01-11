extends Area2D
class_name Provincia

export(String) var province_name
export(PackedScene) var Polygon
export(NodePath) var InfoLabel

var mouse_over = false
var has_own_info_label = false

func _ready():
	InfoLabel = get_node(InfoLabel)
	
	# Set default Script Variables.
	if Polygon:
		remove_child($CollisionShape2D)
		add_child(Polygon.instance())
		
	if not province_name:
		province_name = name
		
	if not InfoLabel or not InfoLabel is Label:
		has_own_info_label = true
		InfoLabel = Label.new()
		add_child(InfoLabel)
		
	InfoLabel.text = province_name
	
	if has_own_info_label:
		InfoLabel.hide()


func _on_Provincia_input_event(_viewport, event, _shape_idx):
	if event is InputEventMouseButton and event.button_index == BUTTON_LEFT \
			&& event.pressed:
				
		if has_own_info_label:
			InfoLabel.show()
		else:
			InfoLabel.text = province_name

func _input(event):
	# Handle press outside of Province (only if has_own_info_label).
	if (event is InputEventMouseButton) and event.pressed and !mouse_over and has_own_info_label:
		InfoLabel.hide()


func _on_Provincia_mouse_entered():
	mouse_over = true


func _on_Provincia_mouse_exited():
	mouse_over = false
