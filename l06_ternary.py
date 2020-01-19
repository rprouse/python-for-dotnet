def main():
    while True:
        try:
            txt = input("Enter a number between 1 and 100 (blank to exit): ")
            num = int(txt)
            num_class = "small" if num < 100 else "huge!"
            print(f"The number is {num_class}")
        except:
            print("Latter gator...")
            break;

if __name__ == '__main__':
    main()