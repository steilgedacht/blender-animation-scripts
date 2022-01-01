import bpy
import random

#duration in [frames]
duration = 60 

name = bpy.context.active_object.name
richtung = random.randint(1,4)

frame = bpy.data.scenes['Scene'].frame_current
bpy.ops.anim.keyframe_insert_menu(type='Location')
bpy.context.scene.frame_set(frame + duration)

if richtung == 1:
    bpy.data.objects[name].location = (5,0,0) #rechts
if richtung == 2:
    bpy.data.objects[name].location = (-5,0,0) #links
if richtung == 3:
    bpy.data.objects[name].location = (0,-5,0) #unten
if richtung == 4:
    bpy.data.objects[name].location = (0,5,0) #oben
    
bpy.ops.anim.keyframe_insert_menu(type='Location')
bpy.context.scene.frame_set(frame)
