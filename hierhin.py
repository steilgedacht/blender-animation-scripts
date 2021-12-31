import bpy

name = bpy.context.active_object.name
x1 = bpy.data.objects[name].location.x
y1 = bpy.data.objects[name].location.y
z1 = bpy.data.objects[name].location.z

keylist =[]
frame = bpy.data.scenes['Scene'].frame_current
for f in bpy.context.object.animation_data.action.fcurves:
    for k in f.keyframe_points: 
        fr = k.co[0]
        keylist.append((int(abs(fr))));
                    
frame = bpy.data.scenes['Scene'].frame_current
for x in range(0,len(keylist)):
    if keylist[x] > frame:
        lastframe = keylist[x-2]
        break
try:
    print(lastframe)
except:
    lastframe = keylist[-1]

bpy.context.scene.frame_set(lastframe)
x = bpy.data.objects[name].location.x
y = bpy.data.objects[name].location.y
z = bpy.data.objects[name].location.z

bpy.context.scene.frame_set(frame - 60)
bpy.data.objects[name].location = (x,y,z)
bpy.ops.anim.keyframe_insert_menu(type='Location')

bpy.context.scene.frame_set(frame)
bpy.data.objects[name].location = (x1,y1,z1)
bpy.ops.anim.keyframe_insert_menu(type='Location')
