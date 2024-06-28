from pygame import *
from random import randint
window = display.set_mode((500, 300))

display.set_caption('Понг пинг')
background = transform.scale(image.load("jaba.jpg"), (500, 300))


fps = 60
game = True
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (80, 80))
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


pl1 = Player('treasure.png', 30, 150, 10)



while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    pl1.reset()
    pl1.update()
    
    
    
    
    
    display.update()
    clock.tick(fps)