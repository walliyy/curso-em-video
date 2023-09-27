# Faça um programa em Python que abra e repdoduza um áudio de um arquivo MP3
# from pydub import AudioSegment
# from pydub.playback import play 

# song = AudioSegment.from_mp3("manoel.mp3")
# play(song)

import pygame

pygame.init() # iniciar pygame

pygame.mixer.music.load('manoel.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()