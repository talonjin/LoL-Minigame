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
WAVE_NUM = 3
a = []
minion_mid = Sprite(image="minion.png", x=75, y=1020, dx=1, dy=-0.92)

#spawn location variables
xLocation = 50
yLocation = 955


for i in range(WAVE_NUM):
    a.append(Sprite(image="minion.png", x=xLocation, y=yLocation, dx=0.3, dy=-0.22))
    xLocation += 73
    yLocation += 53


c = []
c.append(Sprite(image="wall.png", x=1070,y=320))
#wall = Sprite(image="wall.png", x=1070,y=320)
health_value = 100
tower_health = Text(value=health_value, x=1455, y=150, size=100, color=green)

d = []
minion_left = Sprite(image="minion.png", x=75, y=130, dx=0.245, dy=0.165)
for l in range(WAVE_NUM):
    d.append(Sprite(image="minion.png", x=75, y=130, dx=0.245, dy=0.165))


e = []
minion_right = Sprite(image="minion.png", x=1170, y=1000, dx=-0.19, dy=-0.15)
for o in range(WAVE_NUM):
    e.append(Sprite(image="minion.png", x=1170, y=1000, dx=-0.19, dy=-0.15))

score= Text(value=score_value, size=100, color= red, x=1455, y=80)



music.track = "song.mp3"
music.play()

fire = Sound("fire.wav")
explode = Sound("explode.wav")

while not keyboard.is_pressed(K_ESCAPE):

    score.erase()
    score.draw()

    tower_health.erase()
    for minion in a:
        if minion.right > 1085 and health_value > 0:
            health_value -= 0.5
            tower_health.value = health_value
    for minion in d:
        if minion.right > 900 and health_value > 0:
            health_value -= 0.5
            tower_health.value = health_value

    for minion in e:
        if minion.top < 440 and health_value > 0:
            health_value -= 0.5
            tower_health.value = health_value

    for i in c:
        i.erase()
        i.draw()
        if health_value == 0:
            i.erase()
            c.remove(i)
    tower_health.draw()

    if keyboard.is_pressed(K_q) and not Q_PRESSED:
        b.append(Sprite(image="bullet.png", x=luci.x, y=luci.y,dx=BULLET_SPEED*cos(radians(luci.angle + 90)), dy=BULLET_SPEED*sin(radians(luci.angle + 90))))
        Q_PRESSED = True
        fire.play()
    elif not keyboard.is_pressed(K_q):
        Q_PRESSED = False

#minions going down left
    for i in d:
        i.erase()
        i.y += i.dy
        i.x += i.dx
        i.draw()
        if d[0].bottom > 500:
            i.dx = 0.3
            i.dy = -0.22
        if d[0].right > 900 and minionPosition == True:
            i.dx = 0
            i.dy = 0

    for bullets in b:
        bullets.erase()
        if bullets.overlaps(minion_mid):
            explode.play()
            score_value += 1
            score.value = score_value
            for s in a:
                s.erase()
                a.remove(s)
        if bullets.overlaps(minion_left):
            explode.play()
            score_value += 1
            score.value = score_value
            for s in d:
                s.erase()
                d.remove(s)
        if bullets.overlaps(minion_right):
            explode.play()
            score_value += 1
            score.value = score_value
            for s in e:
                s.erase()
                e.remove(s)



# minion going down mid
    for i in a:
        i.erase()
        i.y += i.dy
        i.x += i.dx
        i.draw()
        if a[0].top < 620 and a[0].right > 950:
            i.dy = 0
            i.dx = 0



#minions going down right
    for s in e:
        s.erase()
        s.y += s.dy
        s.x += s.dx
        s.draw()
        if s.top < 680:
            s.dx = 0.3
            s.dy = -0.22
            minionPosition = True
        if s.top < 440 and minionPosition == True:
            s.dx = 0
            s.dy = 0

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