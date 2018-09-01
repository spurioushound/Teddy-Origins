# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
#This takes the settings class from the settings file
from settings import Settings
from Ship import Ship
import game_functions as gf
from pygame.sprite import Group
from cat import Cat




def run_game():
    pygame.init()
    ai_settings=Settings()
    
    screen=pygame.display.set_mode((
            ai_settings.screen_width,ai_settings.screen_height))
            
    pygame.display.set_caption("Teddy Attack")
    
    
    #set Ship settings
       
    ship=Ship(ai_settings,screen)
    
    #Set Attack method
    bullets=Group()
    
    
    cat=Cat(ai_settings,screen)
    
    
    
    while True:
        
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets,ai_settings)
        cat.cat_move()
        gf.update_screen(ai_settings,screen,ship,bullets,cat)
        
        
        

run_game()
    