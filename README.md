# My Blender Animation Python Scripts
These are some python scripts that I use for animating repetetive tasks in Blender.

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
