from pygame import *
from random import *
from PyQt5.QtWidgets import *
from time import sleep
app = QApplication([])
class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, width, height, speed=0):
        self.image = transform.scale(image.load(player_img), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    run_x = 0
    run_y = 0

    cadr = 0
    end_y = 80
    end_x = 1000
    def updater(self):
        if self.cadr % 40 == 0:
            self.run_x = randint(-self.speed, self.speed)
            self.run_y = randint(-self.speed, self.speed)

        self.cadr += 1

        self.rect.x += self.run_x
        self.rect.y += self.run_y

        if self.rect.y < 0:
            self.rect.y += self.speed
        if self.rect.y > win_height - self.rect.y - self.end_y:
            self.rect.y -= self.speed
        if self.rect.x < 0:
            self.rect.x += self.speed
        if self.rect.x > self.end_x:
            self.rect.x -= self.speed

        self.reset()

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    end_y = 80
    end_x = 1430
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.rect.y - self.end_y:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < self.end_x:
            self.rect.x += self.speed
        self.reset()

    def cursorxy(self):
        pressed = mouse.get_pressed()
        #if mouse.get_focused():
        if pressed[0]:
            pos = mouse.get_pos()
            self.rect.x = pos[0] - self.rect.width / 2
            self.rect.y = pos[1] - self.rect.height / 2
            self.reset()

class Enemy(GameSprite):
    direction = 'right'
    def update(self):
        if self.direction == "right":
            self.rect.x += self.speed
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.rect.x > 900:
            self.direction = "left"
        elif self.rect.x < 700:
            self.direction = "right"
        self.reset()

    directiony = "down"
    def updateY(self):
        if self.directiony == "up":
            self.rect.y += self.speed
        if self.directiony == "down":
            self.rect.y -= self.speed
        if self.rect.y > 400:
            self.directiony = "dowm"
        elif self.rect.y < 100:
            self.directiony = "up"
        self.reset()
    run_x = 0
    run_y = 0

    cadr = 0
    end_y = 80
    end_x = 1000
    def updater(self):
        if self.cadr % 40 == 0:
            self.run_x = randint(-self.speed, self.speed)
            self.run_y = randint(-self.speed, self.speed)

        self.cadr += 1

        self.rect.x += self.run_x
        self.rect.y += self.run_y

        if self.rect.y < 0:
            self.rect.y += self.speed
        if self.rect.y > win_height - self.rect.y - self.end_y:
            self.rect.y -= self.speed
        if self.rect.x < 0:
            self.rect.x += self.speed
        if self.rect.x > self.end_x:
            self.rect.x -= self.speed

        self.reset()
class Spider(GameSprite):
    run_x = 0
    run_y = 0
    cadr = 0
    end_y = 80
    end_x = 1000
    def update(self):
        if self.cadr % 40 == 0:
            self.run_x = randint(-self.speed, self.speed)
            self.run_y = randint(-self.speed, self.speed)

        self.cadr += 1

        self.rect.x += self.run_x
        self.rect.y += self.run_y

        if self.rect.y < 0:
            self.rect.y += self.speed
        if self.rect.y > win_height - self.rect.y - self.end_y:
            self.rect.y -= self.speed
        if self.rect.x < 0:
            self.rect.x += self.speed
        if self.rect.x > self.end_x:
            self.rect.x -= self.speed

        self.reset()
class Wall(sprite.Sprite):
    def __init__(self, color, wall_x, wall_y, wall_width, wall_height):
        self.image = Surface((wall_width, wall_height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
def message1():
    message = QMessageBox()
    message.setText("Вітаю! Ви пройшли 1 рівень! Здолай монстрів, проходячі перешкоди!")
    message.setIcon(QMessageBox.Information)
    message.exec()


win_height = 1500
win_width = 830
FPS = 60
win = display.set_mode((win_height, win_width))
display.set_caption("Travel maze")
display.set_icon(image.load('plain.jpg'))
background = transform.scale(image.load('background.jpg'), (win_height, win_width))
mixer.init()
mixer.music.load("Hollywood.mp3")
mixer.music.play()
winner_sound = mixer.Sound("youwin.mp3")
winner_word = mixer.Sound("congratulations.mp3")
lose_sound = mixer.Sound('lose.mp3')
mixer.music.set_volume(0.3)

font.init()
font2 = font.Font(None, 50)

win_text = font2.render("You are won the maze! Gold surprise!", True, (141, 247, 114))
lose_text = font2.render("You are catch", True, (250, 59, 69))
clock = time.Clock()

red = Player("red_bird.png", 0, 200, 70, 70, 5)
killer = Enemy("killer.png", 600, 0, 100, 100, 5)
gold = GameSprite("sucess.png", 1350, 400, 100, 100, 0)
sprite2 = GameSprite("sprite.png", 300, 400, 150, 100, 5)
spider = Spider("spider.png", 100, 0, 150, 100, 5)
obslacle = GameSprite("obslacle.png", 100, 600, 150, 100)
obslacle2 = GameSprite("obslacle2.png", 200, 0, 150, 100)
obslacle3 = GameSprite("obslacle3.png", 1200, 400, 150, 100)
obslacle4 = GameSprite("obslacle4.png", 650, 300, 150, 100)
obslacle5 = GameSprite("obslacle5.png", 1300, 250, 150, 100)
obslacle6 = GameSprite("obslacle6.png", 930, 50, 150, 100)
obslacle7 = GameSprite("obslacle7.png", 1170, 580, 150, 100)
obslacles = [obslacle, obslacle2, obslacle3, obslacle4, obslacle5, obslacle6, obslacle7]
hand = GameSprite("hand.png", 600, 250, 350, 350)

wall_color = (239, 30, 54)
w1 = Wall(wall_color, 200, 150, 20, 600)
w2 = Wall(wall_color, 200, 50, 1100, 20) #not finish
w3 = Wall(wall_color, 200, 740, 1140, 20)
w4 = Wall(wall_color, 1320, 170, 20, 580)
w5 = Wall(wall_color, 350, 70, 10, 450)
w6 = Wall(wall_color, 220, 350, 50, 10)
w7 = Wall(wall_color, 300, 450, 50,10)
w8 = Wall(wall_color, 430, 700, 10,40)
w9 = Wall(wall_color, 240, 600, 130,10)
w10 = Wall(wall_color, 450, 140, 10,400)
w11 = Wall(wall_color, 530, 70, 10,50)
w12 = Wall(wall_color, 610, 140, 10,500)
w13 = Wall(wall_color, 610, 140, 200,10)
w14 = Wall(wall_color, 710, 240, 10,500)
w15 = Wall(wall_color, 450, 340, 70,10)
w16 = Wall(wall_color, 610, 340, 30,10)
w17 = Wall(wall_color, 810, 140, 10,500)
w18 = Wall(wall_color, 810, 640, 250,10)
w19 = Wall(wall_color, 1000, 640, 10,20)
w20 = Wall(wall_color, 1060, 150, 10, 500)
w21 = Wall(wall_color, 960, 50, 10, 500)
w22 = Wall(wall_color, 920, 300, 50, 10)
w23 = Wall(wall_color, 920, 550, 70, 10)
w24 = Wall(wall_color, 1150, 150, 70, 10)
w25 = Wall(wall_color, 1060, 600, 80, 10)
w26 = Wall(wall_color, 1220, 50, 10,600)
w27 = Wall(wall_color, 430, 700, 10,40)
w28 = Wall(wall_color, 240, 600, 130,10)

walls = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19, w20, w21, w22, w23, w24, w25, w26, w27, w28]
run = True
finish = False
f = 0
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == MOUSEBUTTONDOWN:
            red.cursorxy()
    if not finish:
        win.blit(background, (0,0))
        #win.blit(background, (0, 0))
        for i in walls:
            i.reset()
            if sprite.collide_rect(red, i):
                mixer.music.set_volume(0)
                hand.reset()
                lose_sound.play()
                win.blit(lose_text, (650, 350))
                finish = True
        red.update()
        killer.update()
        killer.updateY()
        killer.updater()
        gold.reset()
        sprite2.updater()
        spider.update()
        if f == 1:
            for i in walls:
                if sprite.collide_rect(red, gold):
                    mixer.music.set_volume(0)
                    winner_sound.play()
                    winner_word.play()
                    win.blit(win_text, (550, 350))
                    finish = True
                if sprite.collide_rect(red, i) or sprite.collide_rect(red, spider) or sprite.collide_rect(red, killer):
                    mixer.music.set_volume(0)
                    hand.reset()
                    lose_sound.play()
                    win.blit(lose_text, (650, 350))
                    finish = True
                    break
        if sprite.collide_rect(red, gold):
            message1()
            sleep(3)
            red.rect.x = 130
            red.rect.y = 150

            walls = obslacles
            f += 1
        display.update()
        clock.tick(FPS)


