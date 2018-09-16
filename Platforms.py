#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 11:17:55 2018

@author: shornbec
"""
import pygame as pg

class Platform(pg.sprite.Sprite):
    def __init__(self,x,y,w,h,screen):
        super(Platform,self).__init__()
        self.screen=screen
        self.image=pg.Surface((w,h))
        self.image.fill((0,255,0))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.top=self.rect.top
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)