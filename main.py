from pygame import *

window = display.set_mode((900, 800))
game = True
finish = False
timer = time.Clock()
color_fon = (135, 206, 250)

class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Platform(GameSprite):
    def __init__(self, player_img, player_x, player_y, player_speed, wight, height, key_up, key_down):
        super().__init__(player_img, player_x, player_y, player_speed, wight, height)
        self.up = key_up
        self.down = key_down
    def update(self):
        keys = key.get_pressed()
        if keys[self.up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[self.down] and self.rect.y < 800 - self.rect.height:
            self.rect.y += self.speed
class Ball(GameSprite):
    def __init__(self, player_img, player_x, player_y, player_speed, wight, height):
        super().__init__(player_img, player_x, player_y, player_speed, wight, height)
        self.player_speed_y = player_speed
    def update(self, pl_1, pl_2):
        self.rect.x += self.speed
        self.rect.y += self.player_speed_y
        if self.rect.y <= 0 or self.rect.y >= 800 - self.rect.height:
            self.player_speed_y *= -1
        if self.rect.colliderect(pl_1.rect) or self.rect.colliderect(pl_2.rect):
            self.speed *= -1
        
pl_l = Platform('player-left.png', 10, 300, 5, 30, 200, K_w, K_s)
pl_r = Platform('player-right.png', 860, 300, 5, 30, 200, K_UP, K_DOWN) 
ball = Ball('ball.png', 400, 350, 3, 100, 100) 
while game:
    window.fill(color_fon)
    for e in event.get():
        if e.type == QUIT:
            game = False
    pl_l.update()
    pl_r.update()
    ball.update(pl_l, pl_r)
    pl_l.reset()
    pl_r.reset()
    ball.reset()
    display.update()
    timer.tick(60)