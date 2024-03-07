import pygame

'''
faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
'''

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
