# Example file showing a circle moving on screen
import pygame
import pygame_gui
import sys

BG_COLOR = (0, 0, 0)  

class Draw:
    def __init__(self) -> None:
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 720
        pygame.init()

        pygame.display.set_caption("Drawing")
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.manager = pygame_gui.UIManager((self.SCREEN_WIDTH, self.SCREEN_HEIGHT),'ui-themes/buttonTheme.json')
        self.running = True

    def layout(self):
        self.ui = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((0, 0), (160, self.SCREEN_HEIGHT)),
                                             manager=self.manager)
        
        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30, 50), (50, 50)),
                                                text='Red',
                                                manager=self.manager,
                                                container=self.ui
                                                )
        

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
                    #self.running = False
                    self.manager.set_visual_debug_mode(True)
            elif event.type == pygame.VIDEORESIZE:
                self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.size
                self.manager.set_window_resolution((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
                self.ui.set_dimensions((160, self.SCREEN_HEIGHT))
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.hello_button:
                    print('Clicked')
            self.manager.process_events(event)

    def update(self):
        time_delta = self.clock.tick(240) / 1000.0
        self.manager.update(time_delta)
    
    def draw(self):
        self.screen.fill(BG_COLOR)
        self.manager.draw_ui(self.screen)
        pygame.display.flip()
    

if __name__ == "__main__":
    game = Draw()
    game.run()
