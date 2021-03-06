#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 20:31:56 2018

@author: shornbec
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen=screen
        self.image=pygame.image.load("Graphics/soundwave.bmp")
        
        self.rect=self.image.get_rect()
        
        self.rect=pygame.Rect(ship.rect.right+25,ship.rect.top-20,50,200)

        self.x=float(self.rect.x)
        
        
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor
        
    def update(self):
        self.x +=self.speed_factor
        self.rect.centerx=self.x
    
    def draw_bullet(self):
        self.screen.blit(self.image,self.rect)
        #pygame.draw.rect(self.screen,self.color,self.rect)