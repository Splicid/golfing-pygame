# Example file showing a circle moving on screen
import pygame
import pygame_gui
import sys


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BG_COLOR = (0, 0, 0)  

class draw():
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption("Drawing")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True

    def layout(self):
        layout = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 0), (160, SCREEN_HEIGHT)),
                                             manager=self.manager)
        hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 50), (50, 50)),
                                                text='Red',
                                                manager=self.manager)
        #self.manager.set_visual_debug_mode(True)

    def run(self):
        self.layout()
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
            self.manager.process_events(event)

    def update(self):
        pass
    
    def draw(self):
        self.screen.fill(BG_COLOR)
        self.manager.update(self.clock.tick(120))
        self.manager.draw_ui(self.screen)
        pygame.display.flip()
    

if __name__ == "__main__":
    
    game = draw()
    game.run()