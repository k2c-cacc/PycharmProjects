import pygame
#import time

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

parar = input('Digite algo para parar...')

#time.sleep(360)

pygame.event.wait()
