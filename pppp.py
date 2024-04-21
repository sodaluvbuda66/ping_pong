from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height)
    sprite.Sprite.__init__(self)
    self.image = transform.scale(image.load(player_image),(wight, height))
    self.speed = player.speed
    self.rect = self.image.get_rect()
    self.rect.x = player_x
    self.rect.y = player_y

    def reset(self):
        window_blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys(K_UP) and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys(K_DOWN) and self.rect.x < win_height - 80:
            self.rect.y += self.speed

back = (200, 255,255)
win_widht =600
win_height = 500
window = display.set_mode((win_widht, win_height))
window.fill(pack)
gane = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        display.update()
        clock.tick(FPS)



