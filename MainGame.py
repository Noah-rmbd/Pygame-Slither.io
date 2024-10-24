import pygame
START_W = 300
START_H = 300
FPS = 60

class MainGame:
    def __init__(self):
        self.winDims = (1000, 700)
        self.window = pygame.display.set_mode(self.winDims)
        self.winColor = (75, 75, 75)
        self.quit = False
        self.clock = pygame.time.Clock()

        self.player = Player(0, 0, START_W, START_H)
        self.orbs = []

    def play(self):
        while not self.quit:
            self.update()
            self.render()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True

    def render(self):
        self.window.fill(self.winColor)

        pygame.display.update()
