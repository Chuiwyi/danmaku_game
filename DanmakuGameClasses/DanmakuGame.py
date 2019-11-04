from . import Globals
import pygame,sys

class DanmakuGame:
    def __init__(self):
        pygame.init()  #Initialize Pygame
        Globals.init() #Declare and Initialize Globals
        Globals.Screen = pygame.display.set_mode(Globals.ScreenSize)
        self.running = True

    def run(self):
        while(self.running):
            #Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            #Update Game Objects



            #Render Game Objects
            Globals.Screen.fill((0,0,0))
            pygame.display.flip()

        sys.exit()