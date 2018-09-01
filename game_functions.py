#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 18:01:29 2018

@author: shornbec
"""

import sys
import pygame
from bullet import Bullet
import random as rand
from cat import Cat



    

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            
            
            elif event.type==pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
                
            elif event.type==pygame.KEYUP:
                check_keyup_events(event,ship)
            
#    if len(cats)< ai_settings.cats_allowed:
#        create_cat(ai_settings,screen,cats)
#            
            

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
#    elif event.key==pygame.K_DOWN:
#        ship.moving_down=True
#    elif event.key==pygame.K_UP:
#        ship.moving_up=True
    
    elif event.key==pygame.K_SPACE and ship.jump_value==0:
        ship.jumping=True
        
    elif event.key==pygame.K_f:
        fire_bullet(ai_settings,screen,ship,bullets)
        
    elif event.key==pygame.K_q:
        sys.exit()
        
        
def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets)< ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
        
 
#def randvar():
#    x=rand.randint(0,5)
#    return(x)

#
#def create_cat(ai_settings,screen,cats):
#    new_cat=Cat(ai_settings,screen)
#    cats.add(new_cat)
#        

        

     
                
                
                
def check_keyup_events(event, ship):          
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
    elif event.key==pygame.K_DOWN:
        ship.moving_down=False
    elif event.key==pygame.K_UP:
        ship.moving_up=False
    elif event.key==pygame.K_SPACE:
        ship.jumping=False
        ship.falling=True





def update_screen(ai_settings,screen,ship,bullets,cat):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    cat.blitme()
    pygame.display.flip()






def update_bullets(bullets,ai_settings):
    bullets.update()
    
    for bullet in bullets.copy():
        if bullet.rect.right >= ai_settings.screen_width:
            bullets.remove(bullet)


