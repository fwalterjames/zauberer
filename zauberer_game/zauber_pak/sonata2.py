import random
from random import choice
import pygame
from pygame import mixer


class Human:
    def __init__(self, name, rank, mind, body, spirit, stats, mind_tack, bod_tack, spir_tack):
        self.name = name
        self.rank = rank
        self.mind = mind
        self.body = body
        self.spirit = spirit
        self.stats = stats
        self.mind_tack = mind_tack
        self.bod_tack = bod_tack
        self.spir_tack = spir_tack

    def __str__(self):
        return f"{self.name} is a {self.rank}{self.stats}."

    def human_body_attack(self, enemy):
        enemy.body -= self.bod_tack
        print(f"🎯 You have hit {enemy.name}'s body with 🩸", (random.choice(
            body_spells)), "🩸 Their body's health is now: 💘", enemy.body)
        return

    def human_mind_attack(self, enemy):
        enemy.mind -= self.mind_tack
        print(f"🎯 You have hit {enemy.name}'s mind with 🩸", (random.choice(
            mind_spells)), "🩸 Their mind's health is now: 😵", enemy.mind)
        return

    def human_spirit_attack(self, enemy):
        enemy.spirit -= self.spir_tack
        print(f"🎯 You have hit {enemy.name}'s spirit with 🩸", (random.choice(
            spirit_spells)), "🩸 Their spirit health is now: 👻", enemy.spirit)
        return


body_spells = ["Exhaustive Heat", "Sudden Frailty", "Skin Waste", "Bone Broke",
               "Eldritch Body-Politic", "Heart Spasm", "Lily Liver", "Vertigo", "Muscle Melt", "Phantom Shackles"]
spirit_spells = ["Identity Vertigo", "Horrid Vanity", "Depraved Envy", "Prideful Self-Hatred", "Ego Flourish",
                 "Gluttonous Self-Regard", "Craven's Ideation", "Defensive Narcissism", "Incomprehensible Hatred"]
mind_spells = ["Grave Thoughts", "Existential dread", "Depressive Fit", "Thought Paralysis",
               "Brain-Cell Freeze", "Vertigo", "Fleeting Psychosis", "Incurious Stagnation", "Abominable Insecurity"]

Leo = Human("Leo", "paladin", 25, 100, 100,
            ", a fierce warrior infused with Holy Light, though perhaps a bit weak of mind. 🦁\n", 2.5, 7.5, 7.5)
Sonata = Human("Sonata", "sprite", 50, 50, 100,
               ", born with magic in her blood, of strong spirit, but average in most other ways. 🐦\n", 5, 5, 7.5)
Erik = Human("Erik", "druid", 100, 100, 25,
             ", a physically-strong spellcaster who prides body over mind, strength over spiritual clarity. 🦊\n", 7.5, 7.5, 2.5)
Hera = Human("Hera", "sorceress", 100, 50, 50,
             ", determined, with wisdom beyond her years, though of average strength and spirit. 🦢\n", 7.5, 5, 5)


class Demon:
    def __init__(self, name, rank, mind, body, spirit, rumor, mind_tack, bod_tack, spir_tack):
        self.name = name
        self.rank = rank
        self.mind = mind
        self.body = body
        self.spirit = spirit
        self.rumor = rumor
        self.mind_tack = mind_tack
        self.bod_tack = bod_tack
        self.spir_tack = spir_tack

    def __str__(self):
        return f"Rumor is {self.name} is a {self.rank}{self.rumor}."

    def demon_body_attack(self, rube):
        while rube.body > 0:
            rube.body -= self.bod_tack
            print(f"☣️ {self.name} has hit your body with 😫", (random.choice(
                body_spells)), "😫 Your physical health is now: 💘", rube.body)
            return
        else:
            while rube.spirit > 0:
                rube.spirit -= self.spir_tack
                print(f"☣️ {self.name} has hit your spirit with 😭", (random.choice(
                    spirit_spells)), "😭 Your spiritual health is now: 👻", rube.spirit)
                return
            else:
                rube.mind -= self.mind_tack
                print(f"☣️ {self.name} has hit your mind with 😖", (random.choice(
                    mind_spells)), "😖 Your mental health is now: 😵", rube.mind)
                return

    def demon_spirit_attack(self, rube):
        while rube.spirit > 0:
            rube.spirit -= self.spir_tack
            print(f"☣️ {self.name} has hit your spirit with 😭", (random.choice(
                spirit_spells)), "😭 Your spiritual health is now: 👻", rube.spirit)
            return
        else:
            while rube.mind > 0:
                rube.mind -= self.mind_tack
                print(f"☣️ {self.name} has hit your mind with 😖", (random.choice(
                    mind_spells)), "😖 Your mental health is now: 😵", rube.mind)
                return
            else:
                while rube.body > 0:
                    rube.body -= self.bod_tack
                    print(f"☣️ {self.name} has hit your body with 😫", (random.choice(
                        body_spells)), "😫 Your physical health is now: 💘", rube.body)
                    return

    def demon_mind_attack(self, rube):
        while rube.mind > 0:
            rube.mind -= self.mind_tack
            print(f"☣️ {self.name} has hit your mind with 😖", (random.choice(
                mind_spells)), "😖 Your mental health is now: 😵", rube.mind)
            return
        else:
            while rube.body > 0:
                rube.body -= self.bod_tack
                print(f"☣️ {self.name} has hit your body with 😫", (random.choice(
                    body_spells)), "😫 Your physical health is now: 💘", rube.body)
                return
            else:
                while rube.spirit > 0:
                    rube.spirit -= self.spir_tack
                    print(f"☣️ {self.name} has hit your spirit with 😭", (random.choice(
                        spirit_spells)), "😭 Your spiritual health is now: 👻", rube.spirit)
                    return


Karminrot = Demon("Karminrot", "red mage", 25, 50, 100,
                  ", and his power comes from the dark, and from anger. The dark makes his spirit strong, but the anger makes his mind weak.", 5, 7.5, 9.5)
Phantast = Demon("Phantast", "dream engineer", 100, 25, 50,
                 ", which makes him powerful of mind and perhaps even spirit. But his mental focus means his body is likely his weakest aspect.", 9.5, 5, 7.5)
Desto = Demon("Desto", "night barbarian", 50, 100, 25,
              ", among the most physically strong of warriors. He is well-educated, and so his mind is not weak either. But he is a fiend, and so it is his spirit that is lacking.", 10.5, 11.5, 6.5)
Berggrab = Demon("Lord Berggrab", "Zauberer", 50, 100, 100,
                 ", an ancient class of wizard of which he is the last remaining. He has no known weaknesses.", 7.5, 9.75, 10)


class Battle:
    def __init__(self):
        self.game_over = False
        self.round = 0

    def new_round(self):
        self.round += 1
        print(f"\n🔥🔥 Round: {self.round}\n")

    def win_check(self):
        if Human.body < 1 and Human.spirit < 1 and Human.mind < 1 and Demon.body:
            self.game_over = True
            failure = mixer.Sound("Failure.mp3")
            failure.play()
            print("☠️ You have fallen, as has your village. 🩸 Game Over. ☠️")
            return
        elif Demon.body < 1 or Demon.mind < 1 or Demon.spirit < 1:
            self.game_over = True
            success = mixer.Sound("Success.mp3")
            success.play()
            print(f"⚔️ Rejoice! 🤖 The wicked {Demon.name} has fallen! ⚔️")
            return

    def takeTurn(self):

        attack = input(
            "Choose your type of attack: A) Attack the body | B) Attack the Mind | C) Attack the Spirit")
        if attack == "A" or attack == "a" or attack.lower() == "Body":
            Demon.demon_spirit_attack(Human)
            return Human.human_body_attack(Demon)
        elif attack == "B" or attack == "b" or attack.lower() == "Mind":
            Demon.demon_mind_attack(Human)
            return Human.human_mind_attack(Demon)
        elif attack == "C" or attack == "c" or attack.lower() == "Spirit":
            Demon.demon_body_attack(Human)
            return Human.human_spirit_attack(Demon)
        elif attack.lower() == "Exit":
            print("You have chosen to exit the game.")
            return


Hera_bridge_battle = Battle()
Human = Hera
Demon = Desto


def desto_v_sonny():
    print("You reenter your body as Sonata\n")
    print("\nThe stranger watches the demon melt, a glint in his eyes 👤")
    print("\nYou sip from a complimentary pint 🍺")
    input("Press enter to ask what happens now 🌅 ")
    print("😇💬 Who do we vanquish next? you ask from beneath a foam mustache\n")
    print("👤 the stranger seems slightly less irritated by you, now that you have killed an actual bad guy\n")
    print("👤💬 Now we head to the Tower Bridge, and destroy Vice Admiral Desto, the Zauberer's chief strategist 🤖\n")
    print("🤠💬 Lead the way! you loudly request, feeling much beer-happiness\n")
    tower = input(
        "Choose an option ⏺️ (type/enter the letter or A or B): \nA) Ask the stranger about Desto | B) Jump right to the second fight\n")
    if tower == "a" or tower == "A":
        print("🏞️🏡⛪You walk along the deserted countryside, en route to make further battle 🌄🏚️\n")
        print("🤔💬 Tell me about this Desto character, you urge the stranger\n")
        print(
            f"💬👤The stranger says, {Desto}. \nGetting past the bridge will get us closer to Lord Berggrab\n")
        input("Press enter to ponder this...")
        print("The stranger sees the worry in your eyes. 💬👤 Oh, you'll do great! he says\n")
        print("But what you're thinking about is what you'll get out of all this fighting...\n")
        print("And if life might be bigger than just a farm when the fighting's over...")
        return desto_battle_intro()
    elif tower == "b" or tower == "B":
        return desto_battle_intro()
    else:
        print("I'm sorry, that is not one of the options. Goodbye!")
        return


Sonny_bridge_battle = Battle()
Human = Sonata
Demon = Desto


def desto_battle_intro():
    print("------🌉🌫️ THE BATTLE OF TOWER BRIDGE 🌫️🌉------\n")
    print("👥 You and the stranger reach a stone bridge over a lapping brook.\n")
    print("🌉There stands a drooling man-creature with chrome skin, like some nightmare's King Arthur.\nThis demon is Vice Admiral Desto 🤖 He looks bare tough.\n ")
    input("🌫️ Press enter to make your presence known 😬\n")
    print("Gripping tight to your dagger 🗡️, you step forth. 😠💬 Oi! you shout\n")
    print("🔕...but the man-thing is staring off toward the foggy horizon, and does not seem to hear you...🔕\n")
    input("Press enter to clear your throat and try again 🙃\n")
    print("😠💬 I SAID OI! I hear there's a chrome troll blocking the bridge. Are you him, or his much uglier brother?\n")
    print("🤖 Desto emits a bunch of beeps and whirs, and you realize he'd been sleeping upright. He finally looks at you.🤖")
    print("He says, 🤖💬Are you sure you want those to be your last words, little girl? and takes out a glowing sword 🤺\n")
    print("You get into your fighting pose. 😠💬 Last words are only words, and I didn't come here to speak, beast.🗡️")
    input("Press enter to charge Vice Admiral Desto 🤖")
    print(
        f"Your body health: 💘 {Sonata.body}| Your mind health: 😵 {Sonata.mind}| Your spirit health: 👻 {Sonata.spirit}")
    while not Sonny_bridge_battle.game_over:
        Sonny_bridge_battle.new_round()
        Sonny_bridge_battle.takeTurn()
        Sonny_bridge_battle.win_check()
