from zauber_pak import cast
from zauber_pak.cast import demon_battle_Erik
from zauber_pak.erik2 import desto_v_erik
import pygame
from pygame import mixer
import random
from random import choice


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
        rube.body -= self.bod_tack
        print(f"☣️ {self.name} has hit your body with 😫", (random.choice(
            body_spells)), "😫 Your physical health is now: 💘", rube.body)
        return

    def demon_spirit_attack(self, rube):
        rube.spirit -= self.spir_tack
        print(f"☣️ {self.name} has hit your spirit with 😭", (random.choice(
            spirit_spells)), "😭 Your spiritual health is now: 👻", rube.spirit)
        return

    def demon_mind_attack(self, rube):
        rube.mind -= self.mind_tack
        print(f"☣️ {self.name} has hit your mind with 😖", (random.choice(
            mind_spells)), "😖 Your mental health is now: 😵", rube.mind)
        return


Karminrot = Demon("Karminrot", "red mage", 25, 50, 100,
                  ", and his power comes from the dark, and from anger. The dark makes his spirit strong, but the anger makes his mind weak.", 5, 7.5, 9.5)
Phantast = Demon("Phantast", "dream engineer", 100, 25, 50,
                 ", which makes him powerful of mind and perhaps even spirit. But his mental focus means his body is likely his weakest aspect.", 9.5, 5, 7.5)
Desto = Demon("Desto", "night barbarian", 50, 100, 25,
              ", among the most physically strong of warriors. He is well-educated, and so his mind is not weak either. But he is a fiend, and so it is his spirit that is lacking.", 7.5, 9.5, 5.5)
Berggrab = Demon("Lord Berggrab", "Zauberer", 50, 100, 100,
                 ", an ancient class of wizard of which he is the last remaining. He has no known weaknesses.", 7.5, 9.75, 10)


def zauberer_erik():
    you = Erik
    print("\nYou are now Erik. ✔️\n")
    input("Press enter to return to your body and speak with the stranger. 👤\n")
    print("💫-----------✨-------------💫")
    print("\nYou are sat in your living room, on the stiff arm chairs handed down to you from your mom (along with the farm and everything in it, really). 🪑")
    print("On the coffee table are two cups of breakfast tea. Yours half-finished, the stranger's untouched.☕☕\n")
    input("It's definitely the stranger's turn to speak (Press Enter to convey this) 🙇\n")
    print("You clear your throat. You say, 💬 What's this about then?")
    print("The stranger looks at you like you aren't as clever as you think. He says, 💬 Are you the child of Earl Cullen?\n")
    input("Choose how to respond ⏺️ (type/enter the letter or A or B): A) to frown at the mention of your supposed-father's name | B) show no emotion at the mention of your supposed-father's name...😒\n")
    print("\nYou say, 💬 Not according to the executors of his estate.")
    print("The stanger sighs and tosses up his hands, giving you a whiff of his various rancid odors. 🤢")
    print("He says, 💬 I'm not talking about solicitors and clerks, boy, I'm talking about blood. Are you the child of Earl Cullen of Moray?\n")
    input("You love a resentful nod, and so you bust one out for the stranger (Press Enter to nod resentfully) 😶\n")
    print("💬 Then this is yours, he says.\n")
    print("From nowhere he pulls an ornate dagger 🗡️ and tosses it on the table, nearly spilling your tea. ")
    print("You blink at it. It looks expensive.")
    dag = input(
        "Choose how to respond ⏺️ (type/enter the letter or A or B): \n A) You are impressed | B) Weapons don't impress you")
    if dag == "A" or dag == "a":
        print("\nYou lean forward in your seat, peering down at the gleaming, gold-hilted weapon.\n 🗡️ 👀")
        print("Your mouth has for some reason gone dry. You look at the stranger.\n")
        print("You say, 💬 This is a knife of the Royal Guard...")
        print("The stranger grins, revealing the cleanest teeth you have ever seen. He says, 💬 And it is yours.")
        input("You don't hate gifts (Press enter to take the dagger 👍 🗡️) \n")
        print("🏆 🗡️ 📯 Congratulations! You have acquired the Rebel Dagger 📯 🗡️ 🏆 \n")
        print("You can now attack enemies! You now have enemies! Yay! 🎵 \n")
        print("It feels fine in your hand, if a bit heavy.\n🗡️Looking down at it, you say, 💬 My mother used to say you can't scam an honest man. And so, stranger, I ask you--why have you come here bearing gifts?")
        input("Press enter to lean back in your seat. 🪑 \n")
        print("👤 The stranger says, 💬 Last night the manor of Lord Ogilvy was sacked by a being known as the Zauberer. 👹\n")
        print("👤💬 This creature and his party take the shapes of men, but they are far from it. They are made of ancient antipathy and modern blood-magic.\n")
        hmm = input("Choose how to respond ⏺️ (type/enter the letter or A or B): \n A) Dang, dude, that sounds crazy! | B) Oh, okay. Why are you telling me this?\n")
        if hmm == "A" or hmm == "a":
            print(
                "The stranger looks at you as though just now realizing you are daft.\n")
            print("👤💬 Quite, he sighs. He adds, 💬 The Zauberer has captured or killed all of Lord Ogilvy's kin. 😡 The county is teetering on the brink of madness 😈")
            print("👤💬 The creature is calling itself Lord Berggrab, and now sits in the county chair. He threatens to make new and unjust laws\n")
            print("👤💬 He threatens to hike taxes on the poor and kill or imprison all who cannot pay or who disobey his new, draconian rules.")
            input("Yikes! (Press enter to say that the Zauberer sounds like a real dirtbag who needs to get murked 😤) \n")
            print("Again, the stranger looks at you like you are not the brightest of lanterns, but he at least looks pleased about it. 👤 💯 ")
            print("👤💬 Quite, says the filthy man. 💬 And it is up to you to do the murking. 😏 Only one possessing the blood of Earl Cullen can slay these ill creations.🙌\n")
            print("And the only soul within two hundred miles who fits that bill is you, Erik. You are the county's only hope.\n")
            input(
                "You can feel your teeth clenching. (Press enter to accept this quest to save the county) 🔥✔️\n")
            print("😲 Oh wow, okay. 📯 Quest ACCEPTED !📯\n")
            return battle_erik()
        else:
            print("The stranger looks at you as though just now realizing you are not only daft, but selfish. 💩 👤\n")
            print("You squirm under the reproach of his gaze. You say, 💬 You are a stranger. I am sorry, sir, but I have questions. 💯")
            print("The stranger sits up even straighter. 👤💬 The Zauberer is calling itself Lord Berggrab and has elected itself Head of County. 👹\n")
            print("It intends raise taxes and exploit, to murder, imprison, and destroy. He did the same in Orkney, which is now in ruins, its inhabitants all dead or fled. 🔥💯🔥")
            input("Press enter to admit that this sounds pretty bad...😯😟")
            print("The stranger relaxes. He says, 👤💬 The legends say these fiends can only be stopped by one with Cullen blood.\n")
            print(
                "And the only person in Briannia who possesses it is you. Erik Bauer, you're our only hope. 😨\n")
            input(
                "Press enter to accept this quest to save the county and your family farm 🔥✔️\n")
            print("😲 We love to see it. 📯 Quest ACCEPTED !📯\n")
            return battle_erik()
    else:
        print("\nYou grimace. You take in the gilded quality of the blade.\n 🗡️ 👀 😒")
        print("You take in the man's tattered look, and the disparity makes your distrust of him grow. 😠\n")
        print("Slowly, you say, 💬 This is a knife of the Royal Guard... How have you acquired it?\n")
        print("The stranger grins, revealing the cleanest teeth you have ever seen. He says, 💬 Aye. And it fell off a wagon.\n")
        print("D'ya want it or not?👺 \n")
        input("Press enter to hesitantly take the dagger 👍 🗡️ \n")
        print("🏆 🗡️ 📯 Congratulations! You have acquired the Rebel Dagger 📯 🗡️ 🏆 \n")
        print("You can now attack enemies! You now have enemies! Yay! 🎵 \n")
        print("It feels fine in your hand, if a bit heavy.\n Looking down at it, you say, 💬 My mother used to say you can't scam an honest man. And so, stranger, I ask you--why have you come here bearing gifts?")
        input("Press enter to lean back in your seat. 🪑 \n")
        print("👤 The stranger says, 💬 Last night the manor of Lord Ogilvy was sacked by a sorceror known as the Zauberer. 👹\n")
        print("👤💬 This creature and his party take the shapes of men, but they are far from it. They are made of ancient antipathy and modern blood-magic.\n")
        hmm = input("Choose how to respond ⏺️ (type/enter the letter or A or B): \n A) Dang, dude, that sounds crazy! | B) Oh, okay. Why are you telling me this?\n")
        if hmm == "A" or hmm == "a":
            print(
                "The stranger looks at you as though just now realizing you are daft.\n")
            print("👤💬 Quite, he sighs. He adds, 💬 The Zauberer has captured or killed all of Lord Ogilvy's kin. 😡 The county is teetering on the brink of madness 😈")
            print("👤💬 The creature is calling itself Lord Berggrab, and now sits in the county chair. He threatens to make new and unjust laws\n")
            print("👤💬 He threatens to hike taxes on the poor and kill or imprison all who cannot pay or who disobey his new, draconian rules.")
            input(
                "Press enter to say that the Zauberer sounds like he needs to get murked 😤 \n")
            print("Again, the stranger looks at you like you are not the brightest of lanterns, but he at least looks pleased about it. 👤 💯 ")
            print("👤💬 Quite, says the filthy man. 💬 And it is up to you to do the murking. 😏 Only one possessing the blood of Earl Cullen can slay these ill creations.\n")
            print("And the only soul within two hundred miles who fits that bill is you, Erik. You are the county's only hope.\n")
            held = input(
                "Choose how to respond ⏺️ (type/enter the letter or A or B): A) accept the quest enthusiastically | B) accept the quest begrudgingly\n")
            if held == "A" or held == "a":
                print("😲 Oh wow, okay. 📯 Quest ACCEPTED !📯\n")
                return battle_erik()
            else:
                print(
                    "You feel a pang of regret, but you can't tell if it's fresh. 📯 Quest ACCEPTED !📯\n ")
                return battle_erik()
        else:
            print("The stranger looks at you as though just now realizing you are not only daft, but selfish. 💩 👤\n")
            print("You squirm under the reproach of his gaze. You say, 💬 You are a stranger. I am sorry, sir, but I have questions. 💯")
            print("The stranger sits up even straighter. 👤💬 The Zauberer is calling itself Lord Berggrab and has elected itself Head of County. 👹\n")
            print("It intends raise taxes and exploit, to murder, imprison, and destroy. He did the same in Orkney, which is now in ruins, its inhabitants all dead or fled. 🔥💯🔥")
            input("Press enter to admit that this sounds pretty bad...😯😟\n")
            print("The stranger relaxes. He says, 👤💬 The legends say these fiends can only be stopped by one with Cullen blood.\n")
            print(
                "And the only person in Britannia who possesses it is you. Erik Bauer, you're our only hope. 😨")
            held = input(
                "Choose how to respond ⏺️ (type/enter the letter or A or B): A) accept the quest enthusiastically | B) accept the quest begrudgingly\n")
            if held == "A" or held == "a":
                print("😲 Oh wow, okay. 📯 Quest ACCEPTED !📯\n")
                return battle_erik()
            else:
                print(
                    "👤💬 You are going to save a lot of lives, Erik, says the stranger. 📯 Quest ACCEPTED !📯\n ")
                return battle_erik()


def battle_erik():
    from zauber_pak.cast import demon_battle_Erik
    print("\n🎬 The War for Deskford county now begins 🔥✨🎭\n")
    input("Press enter to learn some game rules 🎮")
    print("The Rebel Dagger has three forms of magic attack: \n")
    print("👻 Spirit attack, 💘 body attack, 😵 mind attack\n")
    print("You also have three forms of health: spirit, body, mind. When all of your health stats reach zero, the game is over.")
    print("Your enemy's also have three health stats, but you ONLY HAVE TO REDUCE ONE OF THEM TO ZERO TO WIN A FIGHT.\n")
    print(
        f"Here are Erik's stats: Body points: {Erik.body} Spirit points: {Erik.spirit} Mind points: {Erik.mind}\n")
    input("Press enter to begin 🎮\n")
    print("\n🔳--FADE IN--🔳\n")
    print(" 🍀      / \ 🌥️     ")
    print("    🍁  /   \   🥀  ")
    print("   🌷  /     \  🍀  ")
    print(" 🌲   /       \  🌷 ")
    print(" 🌳  /  🦋     \  🌳")
    print(" 🥀 /   👥      \ 🌲")
    print("\n👥 The stranger leads you down the back road leading to the Sunrise Pub 🍻\n")
    sunrise = input(
        "Choose an option ⏺️ (type/enter the letter or A or B): \nA) Ask the stranger about your first enemy | B) Jump right to the first fight\n")
    if sunrise == "a" or sunrise == "A":
        if sunrise == "a" or sunrise == "A":
            print("The sun hides behind clouds 🌥️ You look to the stranger: 💬 What can you tell me about the first of Lord Berggrab's men?\n")
            print("👤💬 I can tell you it's not a Man...\n")
            print("😑💬 Well he's a he, and he's at a pub, so...\n")
            print("👤💬Fine, fine! The first enemy is named Phantast. 👾\n")
            input("Press Enter to see Phantast's info. 👾\n")
            print(f"Your enemy is a demon called Phantast. {Phantast}. \n")
            print(
                "You thank the stranger for this information, and look ahead, as the pub approaches.\n")
            demon_battle_Erik()

    else:
        return demon_battle_Erik()
