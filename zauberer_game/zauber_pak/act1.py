from random import randint
from pygame import mixer


def act_one():
    print("\n =========   ====       ===     ===   =======   =========  ========  =========  ======== ")
    print("     ====   ==  ==      ===     ===   ==    ==  ==         ==    ==  ==         ==    == ")
    print("    ===    ===   ===    ===     ===   ======    ========   == ====   ========   == ====  ")
    print("  ===     ===========   ===     ===   ==   ===  ==         ==   ==   ==         ==   ==  ")
    print(" ===      ===     ===    ===   ===    ==  ===   ==         ==    === ==         ==    ===")
    print("========= ===     ===     ========    ======    ========== ==     == ========== ==     ===")
    print("\n💤You are dreaming, and in this dream you are many other people. You like how this feels.💤")
    print("\n💤 You are awakened by a harsh bang.\n")
    print("You are now yourself. The bang from within your bedroom.\n")
    input("Press enter to turn on your bedside lantern. 💡")
    print("\n------------💡------------")
    print("Your bedroom is now alight 🔥, and nothing looks out of the ordinary.\n")
    print("Your eyes drift to the window above your book shelf. Your brain finally registers a harsh storm out there. 🌩️ \n")
    night = input(
        "⏺️ Type SEARCH to get out of bed and look out the window, and SNOOZE to remain in bed.")
    if night == "SNOOZE" or night == "Snooze" or night == "snooze":
        print("😞 You really-really-really do not want to go over there.\n")
        print("You're NOT afraid, you just...you know, you're tired or whatever.\n")
        print("The wind howls ever madly as you attempt to drift off.\n")
        print("You dream of a man with skin made of iron, and of a stranger banging on your front door ⚰️")
        print("===============================================================\n")
        print("Nope! you think. Heart hammering a beat of anxiety in your chest, you climb back into bed.\n")
        print("The banging persists, the urgnt knocking of someone who might keep at it all night and yet who cannot take a hint.\n")
        print("Despite this intrusion, you drift off to sleep with relative ease, tired from the months of training and harvest you've had.\n")
        print("Your heart is warm with your hopes for a relaxing summer vacation... your mind is nagging with a distant worry..... ✨ ")
        print("--------------------------------------------- ✨ \n")
        input("Press enter to wake up ☀️ \n")
        print("Cockledoodle doo, you think, as you stretch your arms and yawn, wipe the sleep from your eyes, wishing for a few more hours abed. \n")
        print("You don't love farming, but your mother loved it, so you stick by it to honor her💘\n")
        input("Press enter to go outside and feed the chickens. 🐔🐔🐔🐔🐔 \n")
        print("You enter the living room, and pad over to the cottage's front door. You grab the door handle.\n")
        input("Press enter to open the front door.... 🚪\n")
        print("You gasp in surprise and take a step back.")
        print("Your farm looks the same as it ever did--a bit soggy from the storm, and a bit rundown from your being a lousy farmer, but nothing to gasp about.")
        print("No, your gasp is from the man who stands before you. 👤 A stranger...at your door...")
        print("The man throws up his hands. 💬 FINALLY, he says. DO YOU SLEEP WITH COTTON IN YOUR EARS?\n")
        print("The man is disheveled, and clearly not from this village. He wears a tattered cloak, has misshapen eyes and a wiry mustache. 👤\n")
        print("And he gives you the distinct impression that your life is about to change... 🥺\n")
        return segue()
    else:
        print("You take a deep breath, swing your legs off the bed...😶‍🌫️\n")
        input("Press enter to walk over and peer out the window. 🛌 ")
        print(" ============================")
        print(" ==   🌧️     ==       /-    ==")
        print(" ==    🌧️    ==     \/ |    ==")
        print(" ============================")
        print(" ==          ==    \   |   ==")
        print(" ==          ==      |     ==")
        print(" ==          ==      \     ==")
        print(" ============================")
        print("You see that a crooked branch has fallen from the apple tree on your cottage-farmhouse lawn. 🌳 \n")
        print("It now leans against the window's glass. 💭 This must've been the crashing that roused me, you think.")
        input("\nCase Closed! (Press enter to go back to bed, satisfied by your successful investigation.) 😇")
        print("==================❌😩=====================")
        leere = mixer.Sound("leere.mp3")
        leere.play()
        print("\nYou start back toward the bed 🛌\n")
        print("❌BANG ❌ BANG ❌BANG ❌ BANG ❌BANG ❌ \n")
        print("😮💭 What the hecking eff! you think, your heart racing a whole new notch.\n")
        print("⚠️ This new sound has come from the living room.")
        print("By the deep, shadow-gray of the clouds above your village, it must be after midnight and far from dawn.🕛🌑\n")
        print("***Your choices are, go back to sleep and pretend you have heard nothing. OR: go to the living room and investiage the banging.***")
        print("Please note: you live alone.")
        print("----------------------------------------------------------")
        guest = input(
            "⏺️ Type and enter NOPE to go back to bed, or SURE to check the door. 💫")
        if guest == "NOPE" or guest == "nope" or guest == "Nope":
            print("=============================😶‍🌫️===============================\n")
            print(
                "Nope! you think. Heart hammering anxiety drums in your chest, you climb back into bed.\n")
            print("The banging persists at your door, the urgnt knocking of someone who might keep at it all night and yet who cannot take a hint.\n")
            input("Press enter to get back out of bed and walk toward the closet 😰 \n")
            print(" 👁️‍🗨️ You're not going out there--you already made that choice--but you're scared, and need some guidance.\n")
            print(
                "🏴 You open the closet door and look at the full-length mirror behind the door.🚪\n")
            print("You need to speak with the thing that lives inside your mirror 🌀 \n")
            input("Press enter to activate your mirror and speak to the thing 🙃\n")
            print("🌀 the thing materializes over your own reflection. It looks despondent.👤\n👤Yes, it sighs more than asks, as though speaking is too much effort for it.")
            print("💬 I need to play rock-paper-scissors, you say: If I win, I stop stressing and get some sleep. If you win, I go answer the door.")
            print(
                "👤💬 Wait......the thing says, looking confused and alarmed. What's at the door?\n")
            input("Press enter to shout: IRRELEVANT!")
            return rock_paper_scissor()

        else:
            print("=======================")
            print("You take a deep breath and grab the hammer you used to fix the chicken coop just hours earlier 🔨\n")
            print(
                "🕴️ You creep out into the living room, and then you creep over to the cottage's front door.")
            print("You don't have a peephole--these are olden times, and no one in your village has thought of those yet--so you've got to open the door.\n")
            input("Press enter to open the front door... 🚪\n")
            print("----------------------------------- 🚪\n")
            print("⛈️ The world is a basin of torrential rain and thunder that happens to be shaped like your village, shaped like your farm ⛈️\n")
            print("Standing on your cottage porch is a strange little man. 👤\n")
            print("The man is disheveled, and clearly not from this county. He wears a tattered cloak, has misshapen eyes and a wiry mustache. 👤\n")
            print("He is soaking wet.\n")
            print("💬 IT'S ABOUT TIME, he wails with ornery grit. IT'S ONLY THE FATE OF THE ENTIRE CONTINENT AT STAKE!")
            danger = input(
                "⏺️ Type SAFE to slam the door in this loud, rude stranger's face, or SORRY to merely blink at him, puzzled\n")
            if danger == "Sorry" or danger == "SORRY" or danger == "sorry":
                print("You look at this stranger with groggy mind, and sleepy eyes\n")
                print("He speaks English, but his accent is unfamiliar to you. 🗺️\n")
                print(
                    "You say,😑💬 Sir, I wish to be sleeping. How may I help you, and how quickly can it be done?")
                print(
                    "He leans his face close to your face. You smell ale and unwashed horses.\n")
                input("Press enter to lean away... 🤢 \n")
                print("--------------------------------------")
                print("The stranger says, 💬 If you wish to keep this lovely farm, along with air in your lungs, you're gonna wanna let me in. Mate. 👤\n")
                print("And just like that, your life changes. 🥺")
                return segue()
            else:
                print("You step back and grab the door...")
                input(
                    "⏺️ Type and enter: A) to smile as the door slams 🙃 | B) to look apologetic as the door slams\n")
                print(
                    "💬 Yeah, sorry mate, you say, and prepare to close the door on this man and the storm he rode in on\n")
                print("But he shoves his muddy boot in the way 😐 \n")
                print(
                    "He leans his face close to your face. You smell ale and unwashed horses.\n")
                input("Press enter to lean away in disgust... 🤢 \n")
                print("The stranger says, 💬 If you wish to keep this lovely farm, along with air in your lungs, you're gonna wanna let me in. Mate. 👤\n")
                print("And just like that, your life changes. 🥺")
                return segue()


def rock_paper_scissor():
    t = ["Rock", "Paper", "Scissors"]
    Karminrot = t[randint(0, 2)]

    player = False
    print("❤️ Welcome to ROCK-PAPER-SCISSORS! A game you play with a being cursed to live for all eternity in your family mirror! ❤️\n")
    print("💁‍♀️If you win, you go right back to bed, following your gut about the person at your front door.💁‍♂️\n")
    print("👤if you lose, you ignore your own feelings--like you always do, like your mother always did--and go answer the door.👤")
    print("What fun!-🥰-Let's play!")
    while player == False:
        player = input("Type: Rock, Paper, or Scissors?")
        if player == Karminrot:
            print("Tie!")
            return rock_paper_scissor()
        elif player == "Rock" or player == "rock" or player == "ROCK":
            if Karminrot == "Paper":
                print("You lose!", Karminrot, "smothers", player)
                print("\n======== 😐 Ugh. ==========")
                print(
                    "You take a deep breath and grab the hammer you used to fix the chicken coop just hours earlier 🔨\n")
                print(
                    "You creep out into the living room, and then you creep over to the cottage's front door.")
                print("You don't have a peephole--these are olden times, and no one in your village has thought of those yet--so you've got to open the door.\n")
                input("Press enter to open the front door... 🚪\n")
                print("----------------------------------- 🚪\n")
                print("⛈️ The world is a basin of torrential rain and thunder that happens to be shaped like your village, shaped like your farm ⛈️\n")
                print("Standing on your cottage porch is a strange little man. 👤\n")
                print("The man is disheveled, and clearly not from this county. He wears a tattered cloak, has misshapen eyes and a wiry mustache. 👤\n")
                print("He is soaking wet.\n")
                print(
                    "💬 IT'S ABOUT TIME, he wails with ornery grit. IT'S ONLY THE FATE OF THE ENTIRE CONTINENT AT STAKE!")
                danger = input(
                    "⏺️ Type SAFE to slam the door in this loud jerk's face, or SORRY to merely blink at him, puzzled\n")
                if danger == "Sorry" or danger == "SORRY" or danger == "sorry":
                    print(
                        "You look at this stranger with groggy mind, and sleepy eyes\n")
                    print(
                        "He speaks English, but his accent is unfamiliar to you. 🗺️\n")
                    print(
                        "You say,😑💬 Sir, I wish to be sleeping. How may I help you, and how quickly can it be done?")
                    print(
                        "He leans his face close to your face. You smell ale and unwashed horses.\n")
                    input("Press enter to lean away... 🤢 \n")
                    print("--------------------------------------")
                    print("The stranger says, 💬 If you wish to keep this lovely farm, along with air in your lungs, you're gonna wanna let me in. Mate. 👤\n")
                    print("And just like that, your life changes. 🥺")
                    return segue()
                else:
                    input("Press enter to smile and slam the door 🙃 \n")
                    print(
                        "💬 Yeah, sorry mate, you say, and prepare to close the door on this man and the storm he rode in on\n")
                    print("But he shoves his muddy boot in the way 😐 \n")
                    print(
                        "He leans his face close to your face. You smell ale and unwashed horses.\n")
                    input("Press enter to lean away... 🤢 \n")
                    print("The stranger says, 💬 If you wish to keep this lovely farm, along with air in your lungs, you're gonna wanna let me in. Mate. 👤\n")
                    print("And just like that, your life changes. 🥺")
                    return segue()
            elif Karminrot == "Rock":
                print("That's a tie!")
                return rock_paper_scissor()
            else:
                print("You win!", player, "destroys", Karminrot)
                print(
                    "\nYou sigh with relief, and you shut the closet door. You crawl into bed.")
                print("Despite this stress, you drift off to sleep with relative ease, tired from the months of training and harvest you've had.\n")
                print("Your heart is warm with your hopes for a relaxing summer vacation... your mind is nagging with a distant worry..... ✨ ")
                print("--------------------------------------------- ✨ \n")
                input("Press enter to wake up ☀️ \n")
                print("Cockledoodle doo, you think, as you stretch your arms and yawn, wipe the sleep from your eyes, wishing for a few more hours abed. \n")
                print(
                    "You don't love farming, but your mother loved it, so you stick with it to honor her💘\n")
                input("Press enter to go outside and feed the chickens. 🐔🐔🐔🐔🐔 \n")
                print(
                    "You enter the living room, and pad over to the cottage's front door. You grab the door handle.\n")
                input("Press enter to open the front door.... 🚪\n")
                print("You gasp in surprise and take a step back.")
                print("Your farm looks the same as it ever did--a bit soggy from the storm, and a bit rundown from your lack of care, but nothing to gasp about.")
                print("No, your gasp is from the man who stands before you. 👤")
                print(
                    "The man throws up his hands. 💬 FINALLY, he says. DO YOU SLEEP WITH COTTON IN YOUR EARS?\n")
                print("The man is disheveled, and clearly not from this village. He wears a tattered cloak, has misshapen eyes and a wiry mustache. 👤\n")
                print(
                    "And he gives you the distinct impression that your life is about to change... 🥺\n")
                return segue()
        elif player == "Paper" or player == "paper" or player == "PAPER":
            if Karminrot == "Scissors":
                print("You lose!", Karminrot, "sliced", player)
                print("\n======== 😐 Ugh. ==========")
                print(
                    "You take a deep breath and grab the hammer you used to fix the chicken coop just hours earlier 🔨\n")
                print(
                    "You creep out into the living room, and then you creep over to the cottage's front door.")
                print("You don't have a peephole--these are olden times, and no one in your village has thought of those yet--so you've got to open the door.\n")
                input("Press enter to open the front door... 🚪\n")
                print("----------------------------------- 🚪\n")
                print("⛈️ The world is a basin of torrential rain and thunder that happens to be shaped like your village, shaped like your farm ⛈️\n")
                print("Standing on your cottage porch is a strange little man. 👤\n")
                print("The man is disheveled, and clearly not from this county. He wears a tattered cloak, has misshapen eyes and a wiry mustache. 👤\n")
                print("He is soaking wet.\n")
                print(
                    "💬 IT'S ABOUT TIME, he wails with ornery grit. IT'S ONLY THE FATE OF THE ENTIRE CONTINENT AT STAKE!")
                danger = input(
                    "⏺️ Type SAFE to slam the door in this loud jerk's face, or SORRY to merely blink at him, puzzled\n")
                if danger == "Sorry" or danger == "SORRY" or danger == "sorry":
                    print(
                        "You look at this stranger with groggy mind, and sleepy eyes\n")
                    print(
                        "He speaks English, but his accent is unfamiliar to you. 🗺️\n")
                    print(
                        "You say,😑💬 Sir, I wish to be sleeping. How may I help you, and how quickly can it be done?")
                    print(
                        "He leans his face close to your face. You smell ale and unwashed horses.\n")
                    input("Press enter to lean away... 🤢 \n")
                    print("--------------------------------------")
                    print("The stranger says, 💬 If you wish to keep this lovely farm, along with air in your lungs, you're gonna wanna let me in. Mate. 👤\n")
                    print("And just like that, your life changes. 🥺")
                    return segue()
                else:
                    input("Press enter to smile and slam the door 🙃 \n")
                    print(
                        "💬 Yeah, sorry mate, you say, and prepare to close the door on this man and the storm he rode in on\n")
                    print("But he shoves his muddy boot in the way 😐 \n")
                    print(
                        "He leans his face close to your face. You smell ale and unwashed horses.\n")
                    input("Press enter to lean away... 🤢 \n")
                    print("The stranger says, 💬 If you wish to keep this lovely farm, along with air in your lungs, you're gonna wanna let me in. Mate. 👤\n")
                    print("And just like that, your life changes. 🥺")
                    return segue()
            elif Karminrot == "Paper":
                print("That's a tie!")
                return rock_paper_scissor()
            else:
                print("You win!", player, "smothers", Karminrot)
                print(
                    "\nYou sigh with relief, and you shut the closet door. You crawl into bed.")
                print("Despite this stress, you drift off to sleep with relative ease, tired from the months of training and harvest you've had.\n")
                print("Your heart is warm with your hopes for a relaxing summer vacation... your mind is nagging with a distant worry..... ✨ ")
                print("--------------------------------------------- ✨ \n")
                input("Press enter to wake up ☀️ \n")
                print("Cockledoodle doo, you think, as you stretch your arms and yawn, wipe the sleep from your eyes, wishing for a few more hours abed. \n")
                print(
                    "You don't love farming, but your mother loved it, so you stick with it to honor her💘\n")
                input("Press enter to go outside and feed the chickens. 🐔🐔🐔🐔🐔 \n")
                print(
                    "You enter the living room, and pad over to the cottage's front door. You grab the door handle.\n")
                input("Press enter to open the front door.... 🚪\n")
                print("You gasp in surprise and take a step back.")
                print("Your farm looks the same as it ever did--a bit soggy from the storm, and a bit rundown from your lack of care, but nothing to gasp about.")
                print("No, your gasp is from the man who stands before you. 👤")
                print(
                    "The man throws up his hands. 💬 FINALLY, he says. DO YOU SLEEP WITH COTTON IN YOUR EARS?\n")
                print("The man is disheveled, and clearly not from this village. He wears a tattered cloak, has misshapen eyes and a wiry mustache. 👤\n")
                print(
                    "And he gives you the distinct impression that your life is about to change... 🥺\n")
                return segue()
        elif player == "Scissors" or player == "scissors" or player == "SCISSORS":
            if Karminrot == "Rock":
                print("You lose...", Karminrot, "bashes", player)
                print("\n======== 😐 Ugh. ==========")
                print(
                    "You take a deep breath and grab the hammer you used to fix the chicken coop just hours earlier 🔨\n")
                print(
                    "You creep out into the living room, and then you creep over to the cottage's front door.")
                print("You don't have a peephole--these are olden times, and no one in your village has thought of those yet--so you've got to open the door.\n")
                input("Press enter to open the front door... 🚪\n")
                print("----------------------------------- 🚪\n")
                print("⛈️ The world is a basin of torrential rain and thunder that happens to be shaped like your village, shaped like your farm ⛈️\n")
                print("Standing on your cottage porch is a strange little man. 👤\n")
                print("The man is disheveled, and clearly not from this county. He wears a tattered cloak, has misshapen eyes and a wiry mustache. 👤\n")
                print("He is soaking wet.\n")
                print(
                    "💬 IT'S ABOUT TIME, he wails with ornery grit. IT'S ONLY THE FATE OF THE ENTIRE CONTINENT AT STAKE!")
                danger = input(
                    "⏺️ Type SAFE to slam the door in this loud jerk's face, or SORRY to merely blink at him, puzzled\n")
                if danger == "Sorry" or danger == "SORRY" or danger == "sorry":
                    print(
                        "You look at this stranger with groggy mind, and sleepy eyes\n")
                    print(
                        "He speaks English, but his accent is unfamiliar to you. 🗺️\n")
                    print(
                        "You say,😑💬 Sir, I wish to be sleeping. How may I help you, and how quickly can it be done?")
                    print(
                        "He leans his face close to your face. You smell ale and unwashed horses.\n")
                    input("Press enter to lean away... 🤢 \n")
                    print("--------------------------------------")
                    print("The stranger says, 💬 If you wish to keep this lovely farm, along with air in your lungs, you're gonna wanna let me in. Mate. 👤\n")
                    print("And just like that, your life changes. 🥺")
                    return segue()
                else:
                    input("Press enter to smile and slam the door 🙃 \n")
                    print(
                        "💬 Yeah, sorry mate, you say, and prepare to close the door on this man and the storm he rode in on\n")
                    print("But he shoves his muddy boot in the way 😐 \n")
                    print(
                        "He leans his face close to your face. You smell ale and unwashed horses.\n")
                    input("Press enter to lean away... 🤢 \n")
                    print("The stranger says, 💬 If you wish to keep this lovely farm, along with air in your lungs, you're gonna wanna let me in. Mate. 👤\n")
                    print("And just like that, your life changes. 🥺")
                    return segue()
            elif Karminrot == "Scissors":
                print("That's a tie!")
                return rock_paper_scissor()
            else:
                print("You win!", player, "diced", Karminrot)
                print(
                    "\nYou sigh with relief, and you shut the closet door. You crawl into bed.")
                print("Despite this stress, you drift off to sleep with relative ease, tired from the months of training and harvest you've had.\n")
                print("Your heart is warm with your hopes for a relaxing summer vacation... your mind is nagging with a distant worry..... ✨ ")
                print("--------------------------------------------- ✨ \n")
                input("Press enter to wake up ☀️ \n")
                print("Cockledoodle doo, you think, as you stretch your arms and yawn, wipe the sleep from your eyes, wishing for a few more hours abed. \n")
                print(
                    "You don't love farming, but your mother loved it, so you stick with it to honor her💘\n")
                input("Press enter to go outside and feed the chickens. 🐔🐔🐔🐔🐔 \n")
                print(
                    "You enter the living room, and pad over to the cottage's front door. You grab the door handle.\n")
                input("Press enter to open the front door.... 🚪\n")
                print("You gasp in surprise and take a step back.")
                print("Your farm looks the same as it ever did--a bit soggy from the storm, and a bit rundown from your lack of care, but nothing to gasp about.")
                print("No, your gasp is from the man who stands before you. 👤")
                print(
                    "The man throws up his hands. 💬 FINALLY, he says. DO YOU SLEEP WITH COTTON IN YOUR EARS?\n")
                print("The man is disheveled, and clearly not from this village. He wears a tattered cloak, has misshapen eyes and a wiry mustache. 👤\n")
                print(
                    "And he gives you the distinct impression that your life is about to change... 🥺\n")
                return segue()
        else:
            print(
                "\n 👤 I don't understand that gesture. Check your spelling maybe? Let's go again...\n")
        # player was set to True, but we want it to be False so the loop continues
        player = False
        Karminrot = t[randint(0, 2)]


def segue():
    print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
