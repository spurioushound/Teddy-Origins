#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 21:02:06 2018

@author: shornbec
"""

class Settings():
    def __init__(self):
        """Initializae game settings"""
        #Screen settings
        self.screen_width=800
        self.screen_height=400
        self.bg_color=(230,230,230)
        
        #ship characteristics
        self.ship_speed_factor=1.5
        
        #Set his barks
        self.bullet_speed_factor=1
        self.bullet_width=5
        self.bullet_height=1
        self.bullet_color=60,60,60
        self.bullets_allowed=5
        
        self.cats_allowed=5