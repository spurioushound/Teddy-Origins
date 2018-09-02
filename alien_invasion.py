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





def run_game():
    pygame.init()
    ai_settings=Settings()
    
    screen=pygame.display.set_mode((
            ai_settings.screen_width,ai_settings.screen_height))
            
    pygame.display.set_caption("Teddy Attack")
    
    
    #set Ship settings
       
    ship=Ship(ai_settings,screen)
    #cat=Cat(ai_settings,screen)
    
    
    #Set Attack method
    bullets=Group()
    
    

    Cats=Group()
    
    
    while True:
        
        gf.check_events(ai_settings,screen,ship,bullets,Cats)
        
        ship.update()
        
        gf.update_bullets(bullets,ai_settings,Cats)
        
        gf.update_cat(ship,Cats)
        
        gf.update_screen(ai_settings,screen,ship,bullets,Cats)
        
        
        

run_game()
    