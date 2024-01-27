extends Node

@export var mob_scene: PackedScene
var score

# Called when the node enters the scene tree for the first time.
func _ready():
	pass

func game_over():
	$ScoreTimer.stop()
	$MobTimer.stop()
	$HUD.show_game_over()
	$Music.stop()
	$DeathSound.play()
	
func new_game():
	score = 0
	$Player.start($StartPosition.position)
	$StartTimer.start()
	$HUD.update_score(score)
	$HUD.show_message("Get Ready")
	get_tree().call_group("mobs", "queue_free")
	$Music.play()

	
func _on_score_timer_timeout():
	score += 1
	$HUD.update_score(score)

func _on_start_timer_timeout():
	$MobTimer.start()
	$ScoreTimer.start()

func _on_mob_timer_timeout():
	#creates new instance of mob scene
	var mob = mob_scene.instantiate()
	
	#choose random location on path2d
	var mob_spawn_location = $MobPath/MobSpawnLocation
	mob_spawn_location.progress_ratio = randf() 
	
	# Godot uses radians, not degrees. 
	# Pi represents a half turn in radians, about 3.1415 (there is also TAU which is equal to 2 * PI). 
	# If you're more comfortable working with degrees, you'll need to use the deg_to_rad() and rad_to_deg() functions to convert between the two.
	var direction = mob_spawn_location.rotation + PI / 2 #sets mob direction perpendicular to path
	mob.position = mob_spawn_location.position #set mobs position to randowm location
	direction += randf_range(-PI / 4, PI / 4) #add randomness to direction
	mob.rotation = direction
	
	var velocity = Vector2(randf_range(150.0,250.0),0.0) #choose velocity for mob
	mob.linear_velocity = velocity.rotated(direction)
	
	add_child(mob)
	


