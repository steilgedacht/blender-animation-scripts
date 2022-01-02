# My Blender Animation Python Scripts
These are some python scripts that I use for animating repetitive tasks in Blender.

You can just copy the Python scripts into Blender, select the object on which you want the animation to be applyed on and then run the script.

# Setup

The name of the Scene has to be "Scene".
If your scene-name differs, than change the `bpy.data.scenes['Scene']` part to the name of your Scene
`bpy.data.scenes['YOUR_SCENE_NAME']`

Use a camera that faces downwards

![image](https://user-images.githubusercontent.com/89748204/147854974-8e8a782e-81e3-499c-af67-8bc30d9eb917.png)

Every script has a 
`duration = 60`
which adjusts the duration of the animation.
The number refers to frames, so a duration of 60 will result in a 60 frames long animation, which will take 1 second if you are animating in 60fps.

## herein & hinaus

These two scripts are for bringing objects into the camera view (herein.py) and bringing them out again (hinaus.py).

## hierher

This script moves an object two another location.
1) select the object 
2) choose the frame on which the object has to be on a certain location
3) run the script and the object will be there at that specific frame 
