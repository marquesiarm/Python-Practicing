import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('camila.mp3')
pygame.mixer.music.play(loops=0, start=1)
pygame.event.wait(300000)
