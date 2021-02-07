extends Node2D

var params = {}
var scenes = {
	'MainMenuDisplay': 'res://displays/main_menu_display/main_menu_display.tscn',
	'InfoDisplay': 'res://displays/info_display/info_display.tscn',
	'MapDisplay': 'res://displays/map_display/map_display.tscn',
	'TriviaMenuDisplay': 'res://displays/trivia/menu_display/menu_display.tscn',
	'TriviaStartDisplay': 'res://displays/trivia/start_display/start_display.tscn',
	'TriviaGameOverDisplay': 'res://displays/trivia/game_over_display/game_over_display.tscn'
}

func _ready():
	change_scene('MainMenuDisplay')


static func merge_dic(target, patch):
	for key in patch:
		target[key] = patch[key]


func change_scene(scene, _params={}):
	if not params.has(scene):
		params[scene] = {}
	
	merge_dic(params[scene], _params) # Update params dicts.
	return get_tree().change_scene(scenes[scene])
