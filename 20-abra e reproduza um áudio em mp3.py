import pygame
pygame.mixer.init()
pygame.mixer.music.load('mine.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass