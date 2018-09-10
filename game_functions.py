#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 18:01:29 2018

@author: shornbec
"""

import sys
import pygame
from bullet import Bullet
from cat import Cat
from Platforms import Platform



    

def check_events(ai_settings,screen,ship,bullets,Cats):
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            
            
            elif event.type==pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets,Cats)
                
            elif event.type==pygame.KEYUP:
                check_keyup_events(event,ship)
            
#    if len(cats)< ai_settings.cats_allowed:
#        create_cat(ai_settings,screen,cats)
#            
            

def check_keydown_events(event, ai_settings, screen, ship, bullets,Cats):
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
    
    elif event.key==pygame.K_b:
        create_cat(ai_settings,screen,Cats)

    
    elif event.key==pygame.K_q:
        sys.exit()
        
        
def cat_check(ai_settings,screen,Cats):
    if ai_settings.cat_gen %100 ==0:
        create_cat(ai_settings,screen,Cats)


        
def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets)< ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
        
 
#def randvar():
#    x=rand.randint(0,5)
#    return(x)

#
def create_cat(ai_settings,screen,Cats):
    new_cat_animal=Cat(ai_settings,screen)
    Cats.add(new_cat_animal)
        

        

     
                
                
                
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


def update_platforms(platforms,screen):
    pl=Platform(300,550,100,40,screen)
    platforms.add(pl)



def update_screen(ai_settings,screen,ship,bullets,Cats,background,x,platforms):
    #screen.fill(ai_settings.bg_color)
    
    
    
    rel_x= x % background.image.get_rect().width
    
    background.rect.left=rel_x-background.image.get_rect().width
    
    
    print(rel_x)
    
    screen.fill([255, 255, 255])
    screen.blit(background.image, background)
    
    
    if rel_x<800:
        background.rect.left=rel_x
        screen.blit(background.image, background)
    
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    for cat in Cats.sprites():
        cat.blitme()
        
    for plat in platforms.sprites():
        plat.blitme()

    
    ship.blitme()
    #cat.blitme()
        
    pygame.display.flip()





def update_cat(ship,Cats):
    Cats.update()
    

    if pygame.sprite.spritecollideany(ship,Cats):
        print("Dog Down!")


def update_bullets(bullets,ai_settings,Cats):
    bullets.update()
    
    for bullet in bullets.copy():
        if bullet.rect.right >= ai_settings.screen_width:
            bullets.remove(bullet)
    
    collisions=pygame.sprite.groupcollide(bullets,Cats,True,True)


