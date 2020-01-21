def main():

    print("Python iteration demo")

    # while True:
    #     name = input("What is your name? ")
    #     if not name:
    #         break
    #     print(f"Hello {name}")

    nums = [1, 5, 8, 10, 7, 2]
    for num in nums:
        print(f"Next value is {num}")

    for idx, num in enumerate(nums, start=1):
        print(f"The {idx}th num is {num}")

    for n in range(1, 6):
        print(f"Counting {n}")

if __name__ == '__main__':
    main()
