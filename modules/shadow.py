import pygame
from interpolation import *

class Shadow(pygame.sprite.Sprite):
    def __init__(self, image, rect, y_delta, isPlayerOne):
        pygame.sprite.Sprite.__init__(self, self.containers)

	self.image = image.convert()
        self.rect = rect

        self.final_pos = [0,0]
        self.original_pos = (0,0)

        self.original_pos = [rect.x, rect.y]
        if (isPlayerOne == True):
	    self.final_pos[0] = self.original_pos[0] + 120
        else:
            self.final_pos[0] = self.original_pos[0] - 150
        self.final_pos[1] = self.original_pos[1] + y_delta
        
        self.current_time = 0
        self.animation_length = 6*60 * 2

        self.alpha = 200

    def update(self, tick, EventList):
        self.current_time += tick
        self.rect = Interpolation(beginning_pos = self.original_pos,
                                 end_pos = self.final_pos,
                                 current_time = self.current_time,
                                 animation_length = self.animation_length)

        if (self.current_time > self.animation_length):
            self.kill()

        self.image.set_alpha(self.alpha)
        self.alpha -= 10
