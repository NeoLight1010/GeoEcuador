extends Control

onready var text_pregunta  = $PreguntaLayer/textPregunta
onready var RespuestaV     = $RespuestaLayer/RespuestaV 
onready var RespuestaF     = $RespuestaLayer/RespuestaF
onready var Animator       = $BotonLayer/Animator
onready var Timer          = $Timer
onready var PreguntaHolder = $PreguntaNode
onready var text_puntaje   = $PuntajeLayer/Puntaje

var puntaje = 0
var respuesta = null

func _ready():
	randomize()
	set_Pregunta()

func set_Pregunta():
	var childAmount = PreguntaHolder.get_child_count()
	var whichPregunta
	
	# Cada juego tiene 5 preguntas de un banco de mas (decidir cuantas)
	
	if (childAmount-4)> 0:
		whichPregunta = PreguntaHolder.get_child(randi()%childAmount)
		text_pregunta.set_text(whichPregunta.dato)
		respuesta = whichPregunta.respuesta
		
	else:
		var root = get_node("/root/Main")
		root.change_scene("TriviaGameOverDisplay")
		print("Cambiando a final")

	if whichPregunta != null:
		PreguntaHolder.remove_child(whichPregunta)
	
func _on_BotonFalso_pressed():
	if respuesta == true:
		RespuestaF.set_text("Incorrecto")
	else:
		RespuestaF.set_text("Correcto")
		puntaje += 1
	Animator.play("AnimBotonF")
	Timer.start()
	text_puntaje.set_text("Tu puntaje es: " + str(puntaje))

func _on_BotonVerdadero_pressed():
	if respuesta == false:
		RespuestaV.set_text("Incorrecto")
	else:
		RespuestaV.set_text("Correcto")
		puntaje += 1
	Animator.play("AnimBotonV")
	Timer.start()
	text_puntaje.set_text("Tu puntaje es: " + str(puntaje))

func _on_Timer_timeout():
	Animator.play_backwards(Animator.get_current_animation())
	set_Pregunta()
