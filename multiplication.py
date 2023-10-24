from random import choices
import time


def main():

    # Welcome the player
    print_pokemon("charmander.txt")
    print("""\n\nHi! I'm charmander!
    Can you help me evolve by answering these multiplication problems?
    It totally makes sense. I promise.
    """)
    time.sleep(0.5)
    print("I'll give you up to three wrong answers....")
    time.sleep(1)

    pick_list = [i for i in range(0, 13)]
    tries = 0
    streak = 0
    pokemon = "Charmander"

    while tries < 3:
        pick = pick_number_pair(pick_list)

        answer = ask_the_question(pick)

        if evaluate_the_answer(answer, pick):
            print(f"Nice job! {pokemon} is getting stronger...")
            streak += 1
        else:
            tries += 1
            print(f"Nope! The correct answer is {(pick[0] * pick[1])}.")
            print(f"You have {3 - tries} tries remaining...")

        if streak == 10:
            pokemon = "Charmeleon"
            print_pokemon("charmeleon.txt")
            print("\nYour pokemon is evolving! Charmander evolved into Charmeleon!")
            print("\nCan you evolve him to Charizard? Keep trying!")
        elif streak == 20:
            pokemon = "Charizard"
            print_pokemon("charizard.txt")
            print("\nYour pokemon is evolving! Charmeleon evolved into Charizard!")
            print("\nCan you defeat the Elite Four? Keep trying!")
        elif streak == 30:
            print("\nYou've defeated the Elite Four! You're a pokemon master!")
            break

        time.sleep(1)

    print(f"You answered {streak} questions correctly!")
    if streak < 10:
        print_pokemon("charmander.txt")
        print("\n\nThat's...not great. Charmander runs away!")
    elif (streak > 10 and streak < 20):
        print_pokemon("charmeleon.txt")
        print("\n\nNot bad! Charmeleon approves!")
    else:
        print_pokemon("charizard.txt")
        print("\n\nAwesome! Charizard approves!")


def ask_the_question(pick):
    """

    :param pick:
    :return:
    """

    # Ask
    answer = input(f"How about {pick[0]} x {pick[1]} ? ")

    # Ensure it's a number
    try:
        answer = int(answer)
        return answer
    except (ValueError, TypeError):
        print("Hey! That's not a number!")
    return 99999


def pick_number_pair(pick_list):
    """

    :param pick_list:
    :return:
    """
    # Select a number combination at random
    # Temporarily modifying to allow for restricting to simpler problems
    # pick = choices(pick_list, k=2)

    p1 = choices(pick_list, k=1)[0]
    p2 = choices([0, 1, 2])[0]
    pick = (p1, p2)

    return pick


def evaluate_the_answer(answer, pick):
    """

    :param answer:
    :param pick:
    :return:
    """
    return answer == (pick[0] * pick[1])


def print_pokemon(pokemon):
    """

    :param pokemon:
    :return:
    """
    with open(f"{pokemon}") as f:
        line = f.readline()
        while line != '':  # The EOF char is an empty string
            print(line, end='')
            line = f.readline()


if __name__ == "__main__":
    playing = True
    while playing:
        main()

        play_again = input("Play again? (Yes or No)")
        if play_again.lower() == "no":
            playing = False
