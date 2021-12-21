import pygame
from pygame import mixer


def act_two_intro():
    welcome = mixer.Sound("Welcome.mp3")
    welcome.play()
    input("\n👹 Hello and welcome to Zauberer 👹: Press Enter to continue")
    print("==================================")
    print("Zauberer is a text-based fantasy adventure game, in which choices are made. 👹\n")
    print("You will play as one of four characters: Leo 🦁, Sonata 🐦, Erik 🦊, or Hera 🦢.\n")
    input("Each has different strengths and weaknesses, as will your enemies. Press enter for the choice menu. ✨\n")