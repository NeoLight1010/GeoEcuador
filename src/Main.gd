extends Node2D


export(String) var DataJSON = "res://data/provincias/provincias.json"


var focused_province


func _ready():
	
	# Load data
	var data_json = Provincia.new().read_data_json(DataJSON)
	
	## Asign data to provinces
	for region in $"ecuador_ map/Regiones".get_children():
		for province in region.get_children():
			province.data = data_json[province.province_name]
			province.capital = province.data["Capital"]


func _on_Provincia_click(province):
	if focused_province == province:
		# If province is clicked again.
		print("Clicked again!")
		get_tree().change_scene("res://info_display/info_display.tscn")
	
	focused_province = province
	$InfoLabel.text = province.province_name
