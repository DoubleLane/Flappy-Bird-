import pygame
import os

BASE_IMG=pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")))

class Base:
    #motion of base
    
    VEL=5
    WIDTH=BASE_IMG.get_width()
    IMG=BASE_IMG

    def __init__(self,y):
        self.y=y
        self.x1=0
        self.x2=self.WIDTH
        
    def move(self):
        self.x1-=self.VEL
        self.x2-=self.VEL

        if self.x1 + self.WIDTH <0:
            self.x1 = self.x2 + self.WIDTH
        
        if self.x2 + self.WIDTH <0:
            self.x2 = self.x1 +  self.WIDTH

    def draw(self,win):
        #movement of the base is determined by 2 pictures of the base that move one after the other
        #ending of the one is the start for the another
        
        win.blit(self.IMG, (self.x1,self.y))
        win.blit(self.IMG, (self.x2,self.y))
       
