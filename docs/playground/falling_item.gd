extends Node

self.text = str(Global.score)
var item : FallingItem

func _on_item_collide():
    if body == Player:
        if item.collectable == true:
            score += item.itemPoints
        else:
            score -= item.itemPoints
