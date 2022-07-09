# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

import pygame, sys

pygame.init()
 
screen = pygame.display.set_mode((480,480))
clock = pygame.time.Clock()


bg_surface = pygame.image.load('icon.png')


floor_surface= pygame.image.load('floor.png')
 
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.blit(bg_surface,(0,0))  

    screen.blit(floor_surface,(0,380))   



    
    
      
            
            
    pygame.display.update()
    clock.tick()        
    
    
    
    
    
