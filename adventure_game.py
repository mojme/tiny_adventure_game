import time
import random

# simplifiyng function
# prints text with a timer whenever there is t2t in the text


def printpause(text):
    i = 0
    sub_start = 0
    while i <= len(text):
        temporary = text[i:i+3]
        # print(temporary)
        if temporary == "t2t":
            print(text[sub_start:i])
            time.sleep(2)
            i += 3
            sub_start = i
        else:
            i += 1
    print(text[sub_start:i])
    time.sleep(2)

# game data
# list of creatures the game will choose from


creatures = ["ork", "dwarf", "dragon", "vampire", "elf"]
# the default weapon
weapon = "old and rusty knife that nearly breaks apart"
default_weapon = weapon
new_weapons = [
    "smartphone of eternal distraction", "holy sword of QWERTY",
    "the toothbrush of power and strength", "chainsaw of blood and honor"]
# a random creature as the monster
villain = creatures[random.randint(0, len(creatures)-1)]

creature = ""

# game elements


# finds out the player's name and assigns a creature,
# returns the players creature
def intro():
    name = input("Hello player, what is your name?\n")
    creature = creatures[len(name) % len(creatures)]
    printpause(
        name +
        " it shall be.t2t Mhhh....t2t It sounds like you are a(n) "
        + creature + ". \nIs that correct?")
    while True:
        answer = input("Type 'y' for yes and 'n' for no\n")
        if answer == "y":
            printpause(
                "I just know you are a(n) "
                + creature + " by your name. Isn't that fantastic?")
            break
        elif answer == "n":
            printpause(
                "Oh.. then you must be nothing more than an utterly"
                "boring human. Too bad! ")
            creature = "human"
            break
            else:
                print(
                    "Ahh come on. I asked you a simple question."
                    "I expect a simple answer!")
    printpause("But okay... enough talking. Let's start the game: \n\n\n")
    return creature


# plays the scene that happens on the field, returns house or cave as the next scene
def field():
    printpause(
        "You find yourself standing in an open field, filled with grass and yellow wildflowers. t2t"
        "Rumor has it that some wicked creature is somewhere around here,"
        " and has been terrifying the nearby village.t2t"
        "...t2t"
        "In front of you is a house.t2t"
        "To your right is a dark cave.t2t"
        "Enter 1 to knock on the door of the house.t2t"
        "Enter 2 to peer into the cave.t2t"
        "You hold in your hand your "+weapon+". t2t"
        "What would you like to do?")
    while True:
        choice = input("(Please enter 1 or 2).\n")
        if choice == "1":
            return "house"
        elif choice == "2":
            return "cave"
        else:
            printpause("I don't know what that is.")
        return 0


# plays the scene at the house, alternates text depending on the weapon,
# returns user's choice of "fight" or "run away"
def house():
    # play scenario according to choice (run or fight)
    printpause(
        "You approach the door of the houset2t"
        "You are about to knock when the door opens and out steps a "
        + villain + "t2t"
        "Epp! This must be the creature you have heard about, a true "
        + villain + "t2t"
        "The " + villain + " attacks yout2t")
    if creature == villain:
        printpause(
            "This seems odd to you, because you are a "
            + creature + "just like them. Still...")
    else:
        pass
    if weapon == default_weapon:
        printpause(
            "You feel under-prepared for the attack, holding only your "
            + weapon + "!")
    else:
        printpause(
            "You feel very comforable handeling the situation with your "
            + weapon + "!")

    while True:
        choice = input(
                "What would you like to do (1) fight or (2) run away?\n")
        if choice == "1":
            return "fight"
        elif choice == "2":
            return "run away"
        else:
            printpause("I don't know what that is.")
    return 0


# determines the outcome of the fight depending on the weapon or the creature
def fight():
    # chose to fight at the house influenced by creature being and weapon, if
    # weapon not " old and rusty knife that nearly breaks apart ",
    # wins the fight
    if creature.__eq__(villain):
        printpause(
            "The " + villain + " runs towards you and opens their arms.t2t"
            '"MY dear friend", they say "why don`t you come in and join me for a good old '
            + villain + "-dinner?t2t"
            "You are slightly confused because you realise that the creature"
            " everyone fears is a "
            + creature + "just like you.t2t"
            "But of course you accept the invite and join your new " + villain + "-friend.")
        return "friends"
    elif weapon.__eq__(default_weapon):
        printpause(
            "You would do your best...t2t"
            "but your " + weapon + " breaks and you cannot match the " + villain + ".t2t"
            "You have been defeated!")
        return "game over"
    # has a weapon to win the fight and is not the same creature
    else:
        printpause(
            "As the " + villain + " moves to attack you unleash your new "
            + weapon + "."
            "The " + weapon + " is massive and you feel "
            "very powerful as you lift it towards the attack."
            "The " + villain + " looks at your shiny new toy"
            " and runs away!t2t"
            "You have rid the town of the" + villain + "."
            " You are victorious!")
        return "win"


# either assigns player find a random powerful weapon or nothing happens
# if they do not have the default weapon anymore
def cave():
    global weapon
    # if weapon already picked up nothing happens, otherwise weapon = random weapon name
    # if weapon is still default, player picks up a brand new weapon
    if weapon.__eq__(default_weapon):
        number = random.randint(0, len(new_weapons)-1)
        weapon = new_weapons[number]
        printpause(
            "You walk cautiously into the cave.t2t"
            "Turns out to be only a very small cave.t2t"
            "Your eye catches a glint of metal behind a rock.t2t"
            "You have found the " + weapon + "!t2t"
            "You discard your silly old " + default_weapon + "and take the new "
            + weapon + " with you.t2t")
    # if weapon is already new, the player won't find anything anymore
    else:
        printpause(
            "You have been here before, and gotten all"
            " the good stuff.t2t"
            "It's just an empty cave now.t2t")
    print("You walk back out to the field.\n")

# plays the game, works recurringly


def play_game(skip_intro=0):  # function that starts the play_game
    global weapon
    global creature
    global villain

    if skip_intro == 0:
        creature = intro()
    else:
        pass

    # starts the field
    choice = field()

    if choice == "house":
        choice = house()

        # when the player chose to fight
        if choice == "fight":
            choice = fight()
            # when creature and villain are the same
            if choice == "friends":
                print(choice)
                printpause(
                    "You guys have a good time over your dinner.t2t"
                    "The only ones not having such a good time are the"
                    "people in the nearby village.t2t"
                    "Instead of one " +
                    villain + " strolling around town, there are now two.t2t"
                    "But I guess that makes you certainly win this game"
                    "\n Sucess: You won")
            # when they fought and the player won
            elif choice == "win":
                printpause("\n\n Congrats, you won! \n\n")
            # when they fought and the player lost
            elif choice == "game over":
                printpause("xxxt2t\n\n\n\nGAME OVER\n\n\n")

                # when the player decides to run away, he ends up back on the field
        elif choice == "run away":
            printpause("You ran away, back to the field where you started. ")
            play_game(1)
    elif choice == "cave":
        cave()
        play_game(1)

    # if they want to restart, skip it is restarted
    while True:
        choice = input("Do you want to restart the game (y) yes or (n) no ?")
        if choice == "y":
            printpause("Excellent.t2tRestarting the game.t2t")
            # resetting values
            villain = creatures[random.randint(0, len(creatures)-1)]
            weapon = default_weapon
            play_game(0)
        elif choice == "n":
            printpause("Okay.t2tThanks for playing.t2t")
            quit()
        else:
            printpause("Sorry, I did not get it.")


# start  play_game
play_game()
