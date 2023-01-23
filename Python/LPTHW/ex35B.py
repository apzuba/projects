from sys import exit
import random

def gold_room():
    print("room full of gold. How much take?")

    choice = input("> ")
    if int(choice):
        how_much = int(choice)
    else:
        dead("please type the correct number")

    if how_much < 50:
        print("nice, not greedy, you win")
        exit(0)
    else:
        dead("don't be that greedy!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input ("A) take honey\tB)taunt bear\tC) open door\n> ")

        if choice == "take honey":
            dead("bear slaps your cheek")
        elif "taunt" in choice:
            n = random.randint(0,20)
            if n >= 12:
                bear_moved = True
                print(f"{n}\nbear moved through the door\n you can go throught it")
            elif 7 < n < 11:
                bear_moved = False
                print(f"{n}\nnothin happens but bear ignores you, try again")
            else:
                bear_moved = False
                dead(f"{n}\nthe bear got aggressive.")
        elif "open" in choice and bear_moved:
            gold_room()
        else:
            print("Please type correctly")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("It stares at you and you go insane.")
    print("Do you flee for your life or shook your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("tasty.")
    else:
        cthulhu_room()

def dead(why):
    print(why, "oh no\t YOU LOSE")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    trial = 0
    while trial < 3:
        choice = input("> ")
        trial += 1

        if choice == "left":
            bear_room()
        elif choice == "right":
            cthulhu_room()
        elif 0 < trial < 3:
            print(f"try again. {3 - trial} more chances.")
        else:
            dead("no more chances. you starve.")


start()
