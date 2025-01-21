import sys, pygame, time, os, random
from pygame import *



class Game:
    def __init__(self):
       pygame.init()
       self.screen = pygame.display.set_mode((275, 500))
       self.images = ["background-day.png", "bluebird-midflap.png", "pipe-green.png"]
       self.run_images = True
       self.frames = pygame.time.Clock()
       self.move_x = 0
       self.move_y = 0
       self.fps = 60
    

    def load_images(self):
        while self.run_images:           
            for image in self.images:

                self.background = pygame.image.load(self.images[0]).convert()
                self.birds = pygame.image.load(self.images[1]).convert()
                self.pipe = pygame.image.load(self.images[2]).convert()
                self.screen.blit(self.background, (0, 0))
                self.screen.blit(self.birds, (50, 200))
                self.screen.blit(self.pipe, (175, 300))

                pygame.display.update()
             
            
            
    def physics(self):
        pass

    def score(self):
        pass

    def game_state(self):
        pass

    def input_handler(self):
        space_bar = True
        up_arrow = True

    def collision_detection(self):
        pass

    def run_game(self):
        pass
        
if __name__ == "__main__":
    game = Game()
    game.load_images()

