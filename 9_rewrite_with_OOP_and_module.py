import pygame, os, random
from lib.Assets import Assets

'''link of bg: http://surl.li/bwstg
link of car: http://surl.li/bwstc
link of sound bg https://github.com/ShashwatNigam99/Subway-Surfers/blob/master/sounds/theme.mp3
link of sound effect https://github.com/atirek-ak/subway-surfers'''

pygame.init()
clock = pygame.time.Clock()
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 588.5
BORDER_LEFT = 70
BORDER_RIGHT = 380

time = 0
level = 1
block_velocity = level + 4

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Race with block')


class Background():
    def __init__(self, filename, width, height, x, y):
        self.filename = filename
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def load(self):
        IMAGE_RAW = pygame.image.load(os.path.join('raw\Assets', self.filename))
        IMAGE = pygame.transform.scale(IMAGE_RAW, (self.width, self.height))
        WIN.blit(IMAGE, (self.x, self.y))


class Car(Background):
    def __init__(self, filename, width, height, x, y, velocity):
        super().__init__(filename, width, height, x, y)
        self.velocity = velocity

    def load(self):
        super().load()

    def rect(self):
        return pygame.Rect(self.x, self.y , self.width, self.height)

    def car_movement_handle(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]: 
            self.x -= self.velocity 
        if keys_pressed[pygame.K_RIGHT]: 
            self.x += self.velocity  

        if self.x <= BORDER_LEFT:
            self.x = BORDER_LEFT
        if self.x + self.width >= BORDER_RIGHT:
            self.x  = BORDER_RIGHT - self.width


class Block(Background):
    def __init__(self, width, height, x, y):
        super().__init__('',width, height, x, y)

    def block_movement(self):
        pygame.draw.rect(WIN, RED, (self.x, self.y, self.width, self.height))
        self.y += block_velocity
        if self.y > SCREEN_HEIGHT:
            self.y = 0 - self.height
            self.x = random.randrange(BORDER_LEFT, BORDER_RIGHT - self.width)
    
    def rect(self):
        return pygame.Rect(self.x, self.y , self.width, self.height)       

def game_loop():
    global level, block_velocity, time
    assets = Assets(WIN, SCREEN_WIDTH, SCREEN_HEIGHT, BORDER_LEFT, BORDER_RIGHT)
    assets.load_sound('sounds_theme.mp3')
    background = Background('Road.png', SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0)
    car = Car('car.png', 80, 80, SCREEN_WIDTH / 2 - 80 / 2, SCREEN_HEIGHT - 80, 10)
    block = Block(80, 20, random.randrange(BORDER_LEFT, BORDER_RIGHT - 80), 0)
    FPS = 60
    run = True

    while run:
        clock.tick(FPS)
        time += 1
        car_rect = car.rect()
        block_rect = block.rect()
        
        for envent in pygame.event.get():
            if envent.type == pygame.QUIT:
                run = False    
        
        if car_rect.colliderect(block_rect):
            pygame.mixer.pause()
            assets.load_sound('stumble.wav')
            assets.alert('you lose')
            run = False
        elif time % 360 == 0:
            assets.load_sound('levelup.wav')
            level += 1
            block_velocity += 1
        elif level == 20:
            assets.alert('you win')  
        
        background.load()
        car.load()
        assets.status_text('level', level, BORDER_LEFT, 0)
        assets.status_text('speed', block_velocity, BORDER_RIGHT, 0)
        car.car_movement_handle()
        block.block_movement()
        pygame.display.update()
        

game_loop()
