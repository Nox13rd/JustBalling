from pygame import *

_WIDTH = 800
_HEIGHT = 640
window = display.set_mode((_WIDTH, _HEIGHT))

clock = time.Clock()
class ImageSprite(sprite.Sprite):
    def __init__(self, image_file, position, size, speed=(0,0)):
        super().__init__()
        self.speed = Vector2(speed)
        self.rect = Rect(position, size)
        self.initial_position = position
        self.image = image.load(image_file)
        self.image = transform.scale(self.image, size)
    def reset(self):
        self.rect.topleft = self.initial_position
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)


class TxTSprite(sprite.Sprite):
    def __init__(self, words, color, position, font_size):
        super().__init__()
        self.font = font.Font(None, font_size)
        self.image = self.font.render(words, True, color)
        self.rect = self.image.get_rect()
        self.initial_position = position
        self.color = color
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
    def update_txt(self, new_txt):
        self.image = self.font.render(new_txt, True, self.color)



class Paddler(ImageSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed.y
        if keys[K_s]:
            self.rect.y += self.speed.y
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= _HEIGHT:
            self.rect.bottom = _HEIGHT

class Paddling(ImageSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_i]:
            self.rect.y -= self.speed.y
        if keys[K_k]:
            self.rect.y += self.speed.y
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= _HEIGHT:
            self.rect.bottom = _HEIGHT


class balling(ImageSprite):
    def update(self):
        self.rect.topleft += self.speed


paddle1 = Paddler(image_file="stick.png", position=(40, 535), size=(20, 80), speed=(10, 10))
paddle2 = Paddling(image_file="stick.png", position=(730, 535), size=(20, 80), speed=(10, 10))
ball = balling(image_file="boll.jpg", position=(700, 500), size=(50, 50), speed=(1, 1))
while not event.peek(QUIT):
    window.fill("darkorange")

    paddle1.update()
    paddle1.draw(window)
    paddle2.update()
    paddle2.draw(window)
    ball.update()
    ball.draw(window)
    display.update()
    clock.tick(60)
