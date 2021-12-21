import random
from random import shuffle

from pygame import mixer
from zauber_pak import act1, erik3, hera3, leo3, sonata3
from zauber_pak import act2
from zauber_pak import cast
from zauber_pak import hera
from zauber_pak import sonata
from zauber_pak import leofstan
from zauber_pak import erik
from zauber_pak import hera2
from zauber_pak import sonata2
from zauber_pak import leo2
from zauber_pak import erik2
import pygame


class Human:
    def __init__(self, name, rank, mind, body, spirit, stats):
        self.name = name
        self.rank = rank
        self.mind = mind
        self.body = body
        self.spirit = spirit
        self.stats = stats

    def __str__(self):
        return f"{self.name} is a {self.rank}{self.stats}.."


Leo = Human("Leo", "paladin", 25, 100, 100,
            ", a fierce warrior with inner zen, though not quite an intellectual. 🦁\n")
Sonata = Human("Sonata", "sprite", 50, 50, 100,
               ", a spiritually stable sort who only really reads psalms, but is of average strength and intelligence. 🐦\n")
Erik = Human("Erik", "druid", 100, 100, 25,
             ", a physically-strong spellcaster who prides body over mind, strength over spiritual clarity. 🦊\n")
Hera = Human("Hera", "sorceress", 100, 50, 50,
             ", determined, with wisdom beyond her years, though of average strength and spirit. 🦢\n")


class Demon:
    def __init__(self, name, rank, mind, body, spirit, rumor):
        self.name = name
        self.rank = rank
        self.mind = mind
        self.body = body
        self.spirit = spirit
        self.rumor = rumor

    def __str__(self):
        return f"Rumor is {self.name} is a {self.rank}{self.rumor}."


Karminrot = ("Karminrot", "red mage", 25, 50, 100,
             ", and his power comes from the dark, and from anger. The dark makes his spirit strong, but the anger makes his mind weak.")
Phantast = ("Phantast", "dream engineer", 100, 25, 50,
            ", which makes him powerful of mind and clever. This has led to a physical neglect that has rendered his body weak.")
Desto = ("Desto", "night barbarian", 50, 100, 25,
         ", among the most physically strong of warriors. He is well-educated, and so his mind is not weak either. But he is a fiend, and so it is his spirit that is lacking.")
Berggrab = ("Lord Berggrab", "Zauberer", 50, 100, 100,
            ", an ancient class of wizard of which he is the last remaining. He has no known weaknesses.")


pygame.init()
mixer.music.load("theme.mp3")
mixer.music.play(-1)
act1.act_one()

act2.act_two_intro()

print(Sonata)
print(Leo)
print(Erik)
print(Hera)


def act_two():
    selbst = input(
        "Who are you?\nPlease type and enter one of the choices: Leo ♂️ | Sonata ♀️ | Erik ♂️ | Hera ♀️ | OR type exit to quit.")
    if selbst == "Leo" or selbst == "leo" or selbst == "LEO":
        return leofstan.zauberer_leo()
    elif selbst == "Sonata" or selbst == "sonata" or selbst == "SONATA":
        return sonata.zauberer_sonny()
    elif selbst == "Erik" or selbst == "ERIK" or selbst == "erik":
        return erik.zauberer_erik()
    elif selbst == "Hera" or selbst == "HERA" or selbst == "hera":
        return hera.zauberer_hera()
    elif selbst == "exit" or selbst == "EXIT" or selbst == "Exit":
        print("Well, it was nice knowing you. 🏳️")
        return exit()
    else:
        print("Please enter a valid option. ❌ ")
        return act_two()


act_two()


def act_three():
    print("🌟 You can now choose to continue your journey as a new character, stay the same, or exit the game! 🌟")
    selbst = input(
        "Who are you now?\nPlease type and enter one of the choices: Leo ♂️ | Sonata ♀️ | Erik ♂️ | Hera ♀️ | OR type exit to quit.")
    if selbst == "Leo" or selbst == "leo" or selbst == "LEO":
        return leo2.desto_v_leo()
    elif selbst == "Sonata" or selbst == "sonata" or selbst == "SONATA":
        return sonata2.desto_v_sonny()
    elif selbst == "Erik" or selbst == "ERIK" or selbst == "erik":
        return erik2.desto_v_erik()
    elif selbst == "Hera" or selbst == "HERA" or selbst == "hera":
        return hera2.desto_v_hera()
    elif selbst == "exit" or selbst == "EXIT" or selbst == "Exit":
        print("Well, it was nice knowing you. 🏳️")
        return exit()
    else:
        print("Please enter a valid option. ❌ ")
        return act_three()


act_three()


def act_four():
    print("🌟 You can now choose to continue your journey as a new character, stay the same, or exit the game! 🌟")
    selbst = input(
        "Who are you really?\nPlease type and enter one of the choices: Leo ♂️ | Sonata ♀️ | Erik ♂️ | Hera ♀️ | OR type exit to quit.")
    if selbst == "Leo" or selbst == "leo" or selbst == "LEO":
        return leo3.Leo_final_intro()
    elif selbst == "Sonata" or selbst == "sonata" or selbst == "SONATA":
        return sonata3.Sonny_final_intro()
    elif selbst == "Erik" or selbst == "ERIK" or selbst == "erik":
        return erik3.erik_final_intro()
    elif selbst == "Hera" or selbst == "HERA" or selbst == "hera":
        return hera3.hera_final_intro()
    elif selbst == "exit" or selbst == "EXIT" or selbst == "Exit":
        print("Well, it was nice knowing you. 🏳️")
        return exit()
    else:
        print("Please enter a valid option. ❌ ")
        return act_four()


act_four()


def act_five():
    ende = mixer.Sound("end.mp3")
    ende.play()
    print("🔥✨👥 Standing over the fallen wizard, you feel a pity for him\n")
    print("💀👿☠️💬 Pity me not, he says, for death is merely a phase for my kind. A gift you have forsaken.")
    print("You snort, 🤨💬 Pity me not, you say, for I live. And that is something I much prefer.")
    print("The Zauberer laughs with his last breaths. 💀👿☠️💬 Are...are you alive? Are you sure? he asks, sounding genuinely curious.☠️\n")
    print("As he says this, panic rises in you, for you cannot actually remember who you are. Who you REALLY are...💬 Perhaps identity matters not in the future, you think, you hope. \n✨And then he is gone.✨")
    input("Press enter to close your eyes and turn away from the castle 😣\n")
    print("💬 Perhaps, you reckon, this body needn't be yours for you to still be yourself. Perhaps there is no truly knowing oneself, and life is about mastering the pretending.\n")
    print("You look down the hill.\nYou see the approaching stranger, looking pleased. Looking...baleful. Sinister.")
    print("\nAnd you feel a dread, as you steel yourself for the question that is coming next.🏳️\n")
    input("✨👥Do you want to go to the future? (Type and enter YES to reenter your body | type and enter NO to return to your mother's farm)✨👥")
    print("💘-------------✨--⌛THE END⌛--✨-------------💘")
    return exit()


act_five()
