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
        self.middle=screen.get_rect().width/2
        self.right=self.rect.right
        
        
        self.rect.centerx=self.screen_rect.left+30
        self.rect.bottom=600
        
        
        self.gravity=5
        
        
        self.center=float(self.rect.centerx)
        self.vert=0
    
        #Moving in a direction
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        
        #Jumping:
        self.jumping=False
        self.jump_height=50
        self.jump_value=0
        
        self.falling=False
        
        
        
        
    def update(self):
        #self.rect.right<self.screen_rect.right
        
        
        if self.moving_right:
            #self.rect.centerx+=1
            if self.center<self.middle:
                self.center+=self.ai_settings.ship_speed_factor
        
        
        if self.moving_left:
            self.image=pygame.image.load("Graphics/left.png")
        
        
        
        if self.moving_right:
            self.image=pygame.image.load("Graphics/test.bmp")

            
        
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
                self.gravity=-10
                self.jump_value+=10
                print(self.jump_height)
                print(self.jump_value)
            else:
                self.jumping=False
                self.falling=True
        
        if self.falling:
            if self.jump_value!=0:
                self.jump_value-=25
            else:
                self.falling=False
                
        
        
        self.rect.centerx=self.center

        
        
    def bot(self):
        self.rect.bottom += self.gravity
    
    
        
    
    def walk(self):
        if self.rect.centerx % 20 == 0:
            self.image=pygame.image.load("Graphics/test2.bmp")
        else:
            self.image=pygame.image.load("Graphics/test.bmp")
            
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    