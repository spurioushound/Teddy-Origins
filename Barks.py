#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 19:54:43 2018

@author: shornbec
"""

import pygame
from pygame.sprite import Sprite

class bark(Sprite):
    
    def __init__(self,ai_settings,screen,ship):
        super(bark,self).__init()     #This a 2.7 jam
        #super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        
        #Shape
        self.image=pygame.image.load("Graphics/soundwave.bmp")
        self.rect=self.image.get_rect()
        
        #pygame.Rect(0,0,ai_settings.bark_width,
         #                     ai_settings.bark_height)
        
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        
        
        #Vertical
        self.y=float(self.rect.y)
        
        ##Color
        #self.color=ai_settings.bark_color
        
        self.speed_factor=ai_settings.bark_speed_factor
        
    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y
    
    def draw_bark(self):
        #pygame.draw.rect(self.image,self.screen,self.rect)
        self.screen.blit(self.image,self.rect)