import pygame
from pygame import mixer


def act_two_intro():
    welcome = mixer.Sound("Welcome.mp3")
    welcome.play()
    input("\nš¹ Hello and welcome to Zauberer š¹: Press Enter to continue")
    print("==================================")
    print("Zauberer is a text-based fantasy adventure game, in which choices are made. š¹\n")
    print("You will play as one of four characters: Leo š¦, Sonata š¦, Erik š¦, or Hera š¦¢.\n")
    input("Each has different strengths and weaknesses, as will your enemies. Press enter for the choice menu. āØ\n")