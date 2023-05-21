from pygame import *

font.init()
font = font.Font(None, 70)

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('фон.png'), (700, 500))
clock = time.Clock()
FPS = 60
py = 3
px = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

player = GameSprite("да.png", 290, 50, 90, 90, 2)
raketka1 = Player1("фигня.png", 20, 100, 50, 150, 6)
raketka2 = Player2("фигня.png", 630, 100, 50, 150, 6)

game = True
finish = False
final = 0
while game:        
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player.rect.x += px
        player.rect.y += py
        if  player.rect.y < 0:
            py *= -1
        if  player.rect.y > 410:
            py *= -1
        if player.rect.x > 615:
            fontone = font.render("Игрок 1 победил!", True, (255, 0, 0))
            window.blit(fontone, (180, 180))
            finish = True
        if player.rect.x < 10:
            fonttwo = font.render("Игрок 2 победил!", True, (0, 0, 255))
            window.blit(fonttwo, (180, 180))
            finish = True
        if sprite.collide_rect(raketka1, player) or sprite.collide_rect(raketka2, player):
           px *= -1
        player.update()
        player.reset()
        raketka1.update()
        raketka2.update()
        raketka1.reset()
        raketka2.reset()
    display.update()
    clock.tick(FPS)