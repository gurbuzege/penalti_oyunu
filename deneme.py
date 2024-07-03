from ursina import *
from direct.actor.Actor import Actor
from ursina.shaders import lit_with_shadows_shader,basic_lighting_shader as bls

Entity.default_shader = lit_with_shadows_shader

def input(key):
    if key == "a":
        actor.play("jump_left")
            
    if key == "d":
        actor.play("jump_right")
    
    if key == "space":
        body_entity.visible = not body_entity.visible

    if key == "r":
        ball.position = Vec3(20,2,35)

def update():
    if actor.get_current_anim() == None:
        actor.play('idle')

app = Ursina(borderless=False)

player = Entity(scale = 1, shader = bls)
actor = Actor("assets/man.glb")
actor.reparentTo(player)
actor.loop("idle")
player.set_position(Vec3(12,2,35.5))
player.rotation_y = -90

body = actor.expose_joint(None, "modelRoot", "mixamorig:Spine")
body_entity = Entity(model = "cube", scale = (50,100,30), collider = "box")
body_entity.reparent_to(body)
body_entity.world_scale = (0.5,1.5,0.5)

ball = Entity(model = "ball", scale = 0.5, y = 2 , z = 35.5, x = 20, collider = "sphere", shader = bls, start = 0, anim = None, direction = 0, hit = 0)

def shoot_direction():
    ball.start = 1
    if mouse.world_point:
        empty = Entity(position = mouse.world_point)
        print(mouse.world_point)
        print(ball.position)
    else:
        empty = Entity()
    
    empty.look_at(ball)

    print(empty.rotation)

    ball.rotation = empty.rotation
    ball.rotation_y = 0    
    ball.rotation_x -= 10
    ball.anim = ball.animate_position(ball.forward*10, duration = 2, curve = curve.linear)
    invoke(ball.animate_y, 2, 1, delay = 2)


ball.on_click = shoot_direction



print(actor.get_anim_names())

stadium = Entity(model = "mini_stadium", scale = 3, shader = bls)




camera = EditorCamera()
camera.set_position(Vec3(20,2.8,35.5))
camera.rotation_y = -90
camera.rotation_x = 10
sky = Sky()

app.run()