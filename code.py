from pygame import *
from random import randint
window = display.set_mode((500, 300))

display.set_caption('Понг пинг')
background = transform.scale(image.load("jaba.jpg"), (500, 300))


fps = 60
game = True
clock = time.Clock()
finish = False
speed_x = 1
speed_y = 1
scrore1 = 0
scrore2 = 0

font.init()
font2 = font.SysFont('Times New Roman', 36)
los = font2.render('Потерян в таборе', True, (255, 0, 0))



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, sizex, sizey):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sizex, sizey))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 220:
            self.rect.y += self.speed
    def second_update(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 220:
            self.rect.y += self.speed


pl1 = Player('treasure.png', 30, 150, 10, 50, 70)
pl2 = Player('treasure.png', 400, 150, 10, 50, 70)
ball = GameSprite('not_cyborg.png', 250, 150, 5, 40, 40)


while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False





    if finish != True:
        window.blit(background, (0,0))
        text_win1 = font2.render('Очки' + str(scrore1), 1, (253,252,205))
        window.blit(text_win1, (0,0))
        text_win2 = font2.render('Очки' + str(scrore2), 1, (255,255,255))
        window.blit(text_win2, (300,0))
        
        pl1.reset()
        pl1.update()
        pl2.reset()
        pl2.second_update()
        ball.reset()
        ball.rect.x += speed_x    
        ball.rect.y += speed_y
        if sprite.collide_rect(pl1, ball) or sprite.collide_rect(pl2, ball):
            speed_x = speed_x * -1
        if ball.rect.y <= 0 or ball.rect.y >= 260:
            speed_y = speed_y * -1
        
        if ball.rect.x <= 0 or  ball.rect.x >= 460:
            finish  = True
            window.blit(los, (200,200)) 

        if sprite.collide_rect(pl1, ball):
            scrore1 += 1
        if sprite.collide_rect(pl2, ball):
            scrore2 += 1


    display.update()
    clock.tick(fps)
