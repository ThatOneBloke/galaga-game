import pgzrun
WIDTH = 600
HEIGHT = 400
run = True
score = 0

galaga = Actor("ship.png")
galaga.x = 300
galaga.y = 360

insects = []
ingamebullet = []

for x in range(3):
    for y in range(3):
        insect = Actor("bug.png")
        insect.x = 100 + x*75
        insect.y = 25 + y*50
        insects.append(insect)

def draw():
    screen.fill("black")
    galaga.draw()
    for i in insects:
        i.draw()
    for i in ingamebullet:
        i.draw()
    if run == False:
        screen.fill("red")
        screen.draw.text("you lost!", (300, 200))
    if insects == []:
        screen.fill("green")
        screen.draw.text("you won!", (300, 200))
    if run == False or insects == []:
        screen.draw.text("press 'r' to restart", (300, 230))
    screen.draw.text("score = " + str(score),(100, 100))

def update():
    global run, score
    if keyboard.left:
        galaga.x -= 5
    elif keyboard.right:
        galaga.x += 5
    for i in ingamebullet:
        i.y -= 5
    for a in insects:
        a.y += 0.5
        for i in ingamebullet:
            if i.colliderect(a):
                insects.remove(a)
                ingamebullet.remove(i)
                score += 1
        if a.colliderect(galaga):
            run = False

def on_key_down(key):
    global run, insects, ingamebullet, score
    if key == keys.SPACE:
        bullets = Actor("bullet.png")
        bullets.x = galaga.x
        bullets.y = galaga.y
        ingamebullet.append(bullets)
    if run == False or insects == []:
         if key == keys.R:
            run = True
            insects = []
            ingamebullet = []
            score = 0
            for x in range(3):
                for y in range(3):
                    insect2 = Actor("bug.png")
                    insect2.x = 100 + x*75
                    insect2.y = 25 + y*50
                    insects.append(insect2)

pgzrun.go()