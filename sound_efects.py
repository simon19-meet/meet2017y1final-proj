import pygame
pygame.mixer.init()

pygame.mixer.music.load("I_believe_i_can_fly.mp3")

pygame.mixer.music.play(-1)

if birdy.pos()[1]>410:
    pygame.mixer.init()

    pygame.mixer.music.load("hello_darkness.mp3")

    pygame.mixer.music.play()
    
