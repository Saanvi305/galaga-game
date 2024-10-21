import pgzrun
WIDTH=800
HEIGHT=600
TITLE="shooting game"



ship=Actor('galaga',(WIDTH//2,HEIGHT-60))
bullets=[]

def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor('bullet'))
        bullets[-1].x=ship.x
        bullets[-1].x=ship.y-90




def update():
    if keyboard.left:
        ship.x-=5
        if ship.x<0:
            ship.x=0
    elif keyboard.right:
        ship.x+=5
        if ship.x>WIDTH:
            ship.x=WIDTH        



    




def draw():
    screen.clear()
    screen.fill("blue")
    for bullet in bullets:
     bullet.draw()
    ship.draw()






pgzrun.go()