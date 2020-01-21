from switchlang import switch

def main():
    while True:
        text = input("Enter a number 1 -> 4 (blank to exit) ")
        if not text:
            print("Later...")
            break

        num = int(text)

        with switch(num) as s:
            s.case(1, lambda: print("One is fun"))
            s.case(2, lambda: print("Two times better"))
            s.case(3, lambda: print("Three's a crowd"))
            s.case(4, lambda: print("Four is fine"))
            s.default(lambda: print(f"What's up with {num}?"))

if __name__ == '__main__':
    main()