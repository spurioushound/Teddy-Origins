#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 21:09:13 2018

@author: shornbec
"""

import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        self.screen=screen
        self.ai_settings=ai_settings
        
        #this is where we set the image
        self.image=pygame.image.load("Graphics/test.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        
        
        
        self.rect.centerx=self.screen_rect.left+30
        self.rect.bottom=680
        
        
        
        
        
        self.center=float(self.rect.centerx)
        self.vert=float(self.rect.bottom)
    
        #Moving in a direction
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        
        #Jumping:
        self.jumping=False
        self.jump_height=30
        self.jump_value=0
        
        self.falling=False
        
    def update(self):
        #self.rect.right<self.screen_rect.right
        if self.moving_right:
            #self.rect.centerx+=1
            self.center+=self.ai_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left>self.screen_rect.left:
            #self.rect.centerx-=1
            self.center-=self.ai_settings.ship_speed_factor
        
#        if self.moving_down:
#            #self.rect.centerx-=1
#            self.vert+=self.ai_settings.ship_speed_factor
        
        if self.moving_up:
            #self.rect.centerx-=1
            self.vert-=self.ai_settings.ship_speed_factor
        
        if self.jumping:
            if self.jump_value<self.jump_height:
                self.vert-=self.ai_settings.ship_speed_factor
                self.jump_value+=1
            else:
                self.falling=True
                self.jumping=False
        
        if self.falling:
            if self.jump_value>0:
                self.vert+=self.ai_settings.ship_speed_factor
                self.jump_value-=1
            else:
                self.falling=False
        
        self.rect.centerx=self.center
        self.rect.bottom=self.vert

    
    
        
    
    def walk(self):
        if self.rect.centerx % 10 == 0:
            self.image=pygame.image.load("Graphics/test2.bmp")
        else:
            self.image=pygame.image.load("Graphics/test.bmp")
            
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    