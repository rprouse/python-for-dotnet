
def main():
    name = input("What is your name? ")
    some_method(name)


def some_method(name: str):
    if name.strip().lower() == 'rob':
        print("Hello old friend!")
    else:
        print(f"Nice to meet you {name}.")
        print("My name is Python!")


if __name__ == "__main__":
    main()