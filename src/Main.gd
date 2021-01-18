extends Node2D


export(String) var DataJSON = "res://data/provincias/provincias.json"


func _ready():
	
	# Load data
	var data_json = Provincia.new().read_data_json(DataJSON)
	
	## Asign data to provinces
	for region in $"ecuador_ map/Regiones".get_children():
		for province in region.get_children():
			province.data = data_json[province.province_name]
			province.capital = province.data["Capital"]


func _on_Provincia_click(province):
	print("Click on " + province.province_name)
	print("Capital: " + province.capital)
	print()
