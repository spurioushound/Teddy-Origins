#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:10:25 2018

@author: shornbec
"""

import pygame
from pygame.sprite import Sprite


class Cat(Sprite):
    def __init__(self,ai_settings,screen):
        super(Cat,self).__init__()
        
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        
        self.image=pygame.image.load('Graphics/cat.png')
        self.rect=self.image.get_rect()
        
        self.rect.right=self.screen_rect.right
        self.rect.bottom=300
        
        self.x=float(self.rect.x)
        
        self.jumping=True
        self.jump_value=0
        self.jump_height=30
        
        self.falling=False
        
        self.vert=float(self.rect.bottom)
        self.est=0
        
        
        #Lets move this cat
        
    #def move(self):
               
#        #Trying to Jump
#        if self.jump_value == 0:
#            self.est=rand.randrange(1,10)
#        
#        if self.est<=5 and self.jumping==False:
#            self.jumping=True
#        
#        print(self.est)
        
        
    
    def update(self):
        
        if self.jumping:
            if self.jump_value<self.jump_height:
                self.vert-=1
                self.jump_value+=1
            else:
                self.falling=True
                self.jumping=False
        
        if self.falling:
            if self.jump_value>0:
                self.vert+=1
                self.jump_value-=1
            else:
                self.falling=False
                self.jumping=True
            
        #Move him to the left
        self.rect.right-=1
        self.rect.bottom=self.vert
    
    
    
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)