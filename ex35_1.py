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