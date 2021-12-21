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
              ", among the most physically strong of warriors. He is well-educated, and so his mind is not weak either. But he is a fiend, and so it is his spirit that is lacking.", 7.5, 9.5, 5.5)
Berggrab = Demon("Lord Berggrab", "Zauberer", 50, 100, 100,
                 ", an ancient class of wizard of which he is the last remaining. He has no known weaknesses.", 16.5, 17.75, 20)


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
            success = mixer.Sound("End.mp3")
            success.play()
            print(f"⚔️ Rejoice! 💀👿☠️ The wicked {Demon.name} has fallen! ⚔️")
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


Erik_final_battle = Battle()
Human = Erik
Demon = Berggrab


def erik_final_intro():
    print("🏕️ There is no beer here, just the tiredness of battle settling in\n")
    print(
        f"Or just tiredness in general. This is the longest you've been away from the farm since {Erik.rank} school.🎓\n")
    print("You kinda don't want to go back. To the farm, that is. You look at the stranger.👤")
    connect = input(
        "Choose an option ⏺️ (type/enter the letter or A or B): A) Ask the stranger where he's from | B) Skip to the final battle")
    if connect == "A" or connect == "a":
        print("🏞️ You and the stranger start the long trek toward Lindisfarne Castle 🏞️\n")
        print("You look at him and ask, 😓💬 Where did you come from, stranger, if I may ask...\n")
        print("He looks at you, says 👤💬 I'm from a land called America.\n")
        print("You frown. You've never heard of it.\n")
        curio = input(
            "Choose an option ⏺️ (type/enter the letter or A or B): A) Ask the stranger where that is | B) Skip to the final battle")
        if curio == "A" or curio == "a":
            leere = mixer.Sound("leere.mp3")
            leere.play()
            print("You ask, 🤔💬 Is that to the East?\n")
            print("The stranger looks amused. 👤💬 It is a couple of thousand miles to the West, and a couple of hundred years in the future\n")
            print(
                "You are gobsmacked. 😳💬 You...is that why you have such nice teeth? 🤯\n")
            print("👤💬 Aye. I have come chasing the Zauberer and his goons. They too are from a time not yet past. A time that will hopefully never be.\n")
            scout = input(
                "Choose an option ⏺️ (type/enter the letter or A or B): A) Ask for tips on defeating Berggrab ☠️  | B) Skip to the final battle")
            if scout == "A" or scout == "a":
                leere_too = mixer.Sound("leere_too.mp3")
                leere_too.play()
                print(
                    "You ask, 😨💬 What do you know of him? The Zauberer, Lord Berggrab...☠️ \n")
                print(f" The stranger says, 👤💬 {Berggrab}\n")
                print("You take this in...\n")
                future = input(
                    "Choose an option ⏺️ (type/enter the letter or A or B): A) Ask to go to the future | B) Skip to the final battle")
                if future == "A" or future == "a":
                    leere_three = mixer.Sound("leere_three.mp3")
                    leere_three.play()
                    print("😥💬 Stranger, I'd like to go with you...\n")
                    print("👤💬 What does it look like you're doing?")
                    print(
                        "😓💬 No. To the future, after this folly has come to an end...\n")
                    print("The stranger eyes you with curiosity. 👤💬 Are you sure?")
                    conform = input(
                        "Choose an option ⏺️ (type/enter the letter or A or B): A) I might be sure... | B) Skip to final battle")
                    if conform == "A" or conform == "a":
                        print(
                            "🧶 You shrug. 🙄💬 I might be. There is naught here but toil, and sweat, and trouble. Taxes, and dirty teeth.\n")
                        print("The stranger cackles with delight.\n👤💬 The future ain't much different, and it's a lot hotter to boot. But, yeah. You fell the Zauberer, and I'll take you with.\n ")
                        return erik_vs_berggrab()
                    else:
                        print("🧶I guess I'll think on it. The castle approaches...\n")
                        return erik_vs_berggrab()
                else:
                    return erik_vs_berggrab()
            else:
                return erik_vs_berggrab()
        else:
            return erik_vs_berggrab()
    else:
        return erik_vs_berggrab()


def erik_vs_berggrab():
    failure = mixer.Sound("Failure.mp3")
    failure.play()
    print("--------🏛️🏰🏫The Battle of Lindisfarne Castle🏛️🏰🏫--------\n")
    print("🌫️The wind blows as you stand at the gates of the castle, fallen soldiers strewn about the lawn🌫️\n")
    print("The stranger waits at the bottom of the hill. 🗡️ You grip your dagger and stare up at the sprawling fortress.🏛️🏰🏫\n")
    input("Press enter to shout, 😤💬 Oi! Wicked magician, I challenge thee to trial-by-combat! 🎉")
    print("🌪️There is a poof of smoke, and a man in fine garments, with the head of a skeleton, appears.💀👿☠️\n")
    print("It is the Zauberer. Come from the future to subjugate the past.🏴‍☠️\n")
    print("Even with a skull for features, you can tell the creature is surprised to see you.\n It says, 💀👿☠️💬 How unlucky are you that fate has brought you to my doorstep.")
    input("Press enter to take a step toward the Zauberer🗡️\n")
    print("You say, 😤💬 I got enough bad luck to go around, friend, as you shall soon see. ⚔️\n")
    print("💀👿☠️💬 You reek of the lies you've been told. I suppose that's what makes you human. Sadly, neither fact will save you.⚔️")
    print(
        f"Your body health: 💘 {Erik.body}| Your mind health: 😵 {Erik.mind}| Your spirit health: 👻 {Erik.spirit}")
    while not Erik_final_battle.game_over:
        Erik_final_battle.new_round()
        Erik_final_battle.takeTurn()
        Erik_final_battle.win_check()
