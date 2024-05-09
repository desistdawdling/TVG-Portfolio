extends Node

var score = 0

var falling_item = [
    preload("red_berry.tscn"),
    preload("yellow_fruit.tscn")
]

func _ready():
    inst()



func _physics_process(delta):
    if _drop_timer_timout == true:
        inst(rand.x)



func inst(pos):
    # var instance = rand(falling_item).instantiate() 
    add_child()


func 

