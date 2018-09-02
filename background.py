#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 10:32:38 2018

@author: shornbec
"""

import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load('Graphics/background.bmp')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
