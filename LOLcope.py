from livewires.beginners import *
from math import cos, sin, radians
#screen size
screen.set_size(1562,1082)
#booleans
Q_PRESSED = False
minionPosition = False
minionHit = False
#intro
welcome= Text(value="Mini-League",size= 115, color=green, x=screen.width/2, y= 100)

score_value = 0

#screen background
screen.background = "mid.jpg"


luci = Sprite(image="lucian.png", x = 1200, y= 125)

b = []
BULLET_SPEED = 10



#minions going down mid
WAVE_NUM = 1
a = []
minion_mid = Sprite(image="minion.png", x=50, y=955, dx=0.3, dy=-0.22)
minion_mid2 = Sprite(image="minion.png", x=123, y=1008, dx=0.3, dy=-0.22)
minion_mid3 = Sprite(image="minion.png", x=196, y=1061, dx=0.3, dy=-0.22)
#spawn location variables
#xLocation = 50
#yLocation = 955


for i in range(WAVE_NUM):
    a.append(Sprite(image="minion.png", x=xLocation, y=yLocation, dx=0.3, dy=-0.22))
#    xLocation += 73
#    yLocation += 53


c = []
c.append(Sprite(image="wall.png", x=1070,y=320))
#wall = Sprite(image="wall.png", x=1070,y=320)
health_value = 100
tower_health = Text(value=health_value, x=1455, y=150, size=100, color=green)

minion_left = Sprite(image="minion.png", x=75, y=130, dx=0.245, dy=0.165)


minion_right = Sprite(image="minion.png", x=1170, y=1000, dx=-0.19, dy=-0.15)


score= Text(value=score_value, size=100, color= red, x=1455, y=80)



music.track = "song.mp3"
music.play()

fire = Sound("fire.wav")
explode = Sound("explode.wav")

while not keyboard.is_pressed(K_ESCAPE):

    score.erase()
    score.draw()

    if keyboard.is_pressed(K_q) and not Q_PRESSED:
        b.append(Sprite(image="bullet.png", x=luci.x, y=luci.y,dx=BULLET_SPEED*cos(radians(luci.angle + 90)), dy=BULLET_SPEED*sin(radians(luci.angle + 90))))
        Q_PRESSED = True
        fire.play()
    elif not keyboard.is_pressed(K_q):
        Q_PRESSED = False

#minions going down left
    minion_left.erase()
    minion_left.y += minion_left.dy
    minion_left.x += minion_left.dx
    minion_left.draw()
    if minion_left.bottom > 500:
        minion_left.dx = 0.3
        minion_left.dy = -0.22
    if minion_left.right > 900 and minionPosition == True:
        minion_left.dx = 0
        minion_left.dy = 0

    for bullets in b:
        bullets.erase()
        if bullets.overlaps(minion_mid) or bullets.overlaps(minion_mid2) or bullets.overlaps(minion_mid3) or bullets.overlaps(minion_left) or bullets.overlaps(minion_right):
            explode.play()
            score_value += 1
            score.value = score_value
            minion_left.erase()
            minion_right.erase()
            minion_mid.erase()
            minion_mid2.erase()
            minion_mid3.erase()

    tower_health.erase()
    if minion_mid.right > 950 and minion_mid2.right > 1035 and minion_mid3.right > 1120 and health_value > 0:
        health_value -= 0.5
        tower_health.value = health_value
    for i in c:
        i.erase()
        i.draw()
        if health_value <= 0:
            i.erase()
            c.remove(i)
            #if not i:
                #minion_mid.dx = 1
                #minion_mid.dy = 1
    tower_health.draw()

# minion going down mid
    minion_mid.erase()
    minion_mid.y += minion_mid.dy
    minion_mid.x += minion_mid.dx
    minion_mid.draw()
    minionPosition == True
    if minion_mid.right > 950 and minionPosition == True:
        minion_mid.dy = 0
        minion_mid.dx = 0


    minion_mid2.erase()
    minion_mid2.y += minion_mid2.dy
    minion_mid2.x += minion_mid2.dx
    minion_mid2.draw()
    minionPosition = True
    if minion_mid2.right > 1035 and minionPosition == True:
        minion_mid2.dy = 0
        minion_mid2.dx = 0

    minion_mid3.erase()
    minion_mid3.y += minion_mid3.dy
    minion_mid3.x += minion_mid3.dx
    minion_mid3.draw()
    minionPosition = True
    if minion_mid3.right > 1120 and minionPosition == True:
        minion_mid3.dy = 0
        minion_mid3.dx = 0


#minions going down right
    minion_right.erase()
    minion_right.y += minion_right.dy
    minion_right.x += minion_right.dx
    minion_right.draw()
    if minion_right.top < 680:
        minion_right.dx = 0.3
        minion_right.dy = -0.22
        minionPosition = True
    if minion_right.top < 440 and minionPosition == True:
        minion_right.dx = 0
        minion_right.dy = 0

    welcome.erase()
    welcome.draw()

# aiming
    luci.erase()
    if keyboard.is_pressed(K_w):
        luci.angle+= 1
    elif keyboard.is_pressed(K_e):
        luci.angle-= 1
    luci.draw()
    if luci.angle >= 85:
        luci.angle = 85
    if luci.angle <= 1:
        luci.angle = 1

    # Moving Bullets
    for bullets in b:
        bullets.x += bullets.dx
        bullets.y += bullets.dy
    #Drawing
    for bullets in b:
        bullets.draw()

    screen.update()