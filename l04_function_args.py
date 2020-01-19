def main():
    print("say_hello()")
    say_hello()
    print()

    print("say_hello(name)")
    say_hello("Joe")
    print()

    print("say_hello(name, times)")
    say_hello("Zoe", 5)
    print()

    print("say_hello(name, times, 1, 2, 3)")
    say_hello("Zoe", 5, 1, 2, 3)
    print()

    print("say_hello(name, times, 1, 2, 3, val=7, mode=prod)")
    say_hello("Zoe", 5, 1, 2, 3, val=7, mode="prod")
    print()


def say_hello(name='friend', times=1, *args, **kwargs):
    print(f"Hello there {name} with times={times}, args={args}, kwargs={kwargs}")

if __name__ == '__main__':
    main()