import pygame

pygame.init()
pygame.mixer.init()

try:
    sound = pygame.mixer.Sound("correct.wav")
    sound.play()
    input("Playing sound. Press Enter to stop...")
except Exception as e:
    print("Error loading sound:", e)