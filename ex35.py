from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    how_much = 0;
    next = input(">")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        print("Man, learn to type a number.")
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        print("You greedy bastard")

gold_room();

def bear_room():
    print("There is a bear")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        next = input(">")

        if next == "take honey":
            print("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            print("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else: print("I got no idea what that means")







