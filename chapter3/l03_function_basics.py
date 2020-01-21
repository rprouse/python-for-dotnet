import random


def main():
    show_header()
    rand = random.randint(1, 100)
    count = 0

    while True:
        guess = get_guess()
        if not guess:
            continue

        count += 1
        if evaluate_guess(guess, rand):
            break

    print(f"You got the number in {count} attempts.")


def show_header():
    print("|                                         |")
    print("-------------------------------------------")
    print("|         PYTHON HIGH / LOW GAME          |")
    print("|                                         |")
    print("-------------------------------------------")
    print()
    print("I'm thinking of a number between 1 & 100.")
    print("How many steps can you guess it in?")
    print()


def get_guess() -> int:
    try:
        text = input("What number am I thinking of? ")
        val = int(text)
        if val < 1 or val > 100:
            print(f"{val} is not between 1 and 100")
            return None
        return val
    except:
        print("That is not a number")
        return None


def evaluate_guess(guess: int, rand: int) -> bool:
    if guess == rand:
        return True

    if guess < rand:
        print("That is too LOW")
    elif guess > rand:
        print("That is too HIGH")
    return False


if __name__ == '__main__':
    main()
