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

while game:
    window.fill(color_fon)
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    timer.tick(60)