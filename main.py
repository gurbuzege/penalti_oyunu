from ursina import *
from direct.actor.Actor import Actor
from ursina.shaders import lit_with_shadows_shader,basic_lighting_shader as bls

Entity.default_shader = lit_with_shadows_shader

app = Ursina(borderless=False)

player = Entity(scale = 1, shader = bls)
actor = Actor("assets/man.glb")
actor.reparentTo(player)
actor.loop("idle.001")
print(actor.get_anim_names())

camera = EditorCamera()
sky = Sky()

app.run()