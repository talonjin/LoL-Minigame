from livewires.beginners import *
#screen size
screen.set_size(1562,1082)
#screen background
screen.background = "mid.jpg"
#minions going down mid
WAVE_NUM = 3
a = []
minion_mid = Sprite(image="minion.png", x=75, y=1020, dx=0.3, dy=-0.22)
#a.append(minion_mid)


#spawn location variables
xLocation = 50
yLocation = 955
for i in range(WAVE_NUM):
    a.append(Sprite(image="minion.png", x=xLocation, y=yLocation, dx=0.3, dy=-0.25))
    xLocation += 80
    yLocation += 60


minion_left = Sprite(image="minion.png", x=50, y=240)
minion_right = Sprite(image="minion.png", x=screen.width/2, y=screen.height/2)
luci = Sprite(image="lucian.png", x = 1200, y= 300,dx=1,dy=1)

while not keyboard.is_pressed(K_ESCAPE):

    luci.erase()
    luci.draw()

#minions going down left
    minion_left.erase()
    minion_left.draw()

#minion going down mid
    for i in a:
        i.erase()
        i.y += i.dy
        i.x += i.dx
        i.draw()
        if a[0].top < 620 and a[0].right > 950:
            i.dy = 0
            i.dx = 0

    screen.update()