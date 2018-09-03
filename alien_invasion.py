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
from background import Background


#
#mainClock=pygame.time.Clock()
#
#mainClock.tick(fps)

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
    
    x=0
    background = Background([800,0])
    
    #x=0

    Cats=Group()
    
    
    while True:
        
        gf.check_events(ai_settings,screen,ship,bullets,Cats)
        
        x-=1
        print(x)
        ship.update()
        
        gf.update_bullets(bullets,ai_settings,Cats)
        
        gf.cat_check(ai_settings,screen,Cats)
        
        gf.update_cat(ship,Cats)
        

        
        gf.update_screen(ai_settings,screen,ship,bullets,Cats,background,x)
        
        ai_settings.cat_gen+=1
        
        

run_game()
    