# Example file showing a circle moving on screen
import pygame
import sys


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BG_COLOR = (0, 0, 0)  

class draw():
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Drawing Game")

        self.clock = pygame.time.Clock()

        self.running = True
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(120)  

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BG_COLOR)

        pygame.display.flip()
    


if __name__ == "__main__":
    game = draw()
    game.run()