extends Node2D

var params = {}
var scenes = {
	'InfoDisplay': 'res://displays/info_display/info_display.tscn',
	'MapDisplay': 'res://displays/map_display/map_display.tscn'
}

func _ready():
	change_scene('MapDisplay')


static func merge_dic(target, patch):
	for key in patch:
		target[key] = patch[key]


func change_scene(scene, _params={}):
	if not params.has(scene):
		params[scene] = {}
	
	merge_dic(_params, params[scene])
	get_tree().change_scene(scenes[scene])
