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
	var Main = $"/root/Main"
	
	if focused_province == province:
		# If province is clicked again.
		var data = {
			"province_name": province.province_name,
			"data": province.data
		}
		
		Main.change_scene("InfoDisplay", data)
		
	focused_province = province
	$InfoLabel.text = province.province_name
