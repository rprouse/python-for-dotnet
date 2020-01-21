def main():
    data = [55, 987, 89, -233, 8, 13, -377, 3, 1, -34, 610, 144, 5, 21, 2, 1]

    data.sort(key=lambda n: abs(n))
    print(data)

    doubled = [2*n for n in data] # if n % 2 == 0]
    print(doubled)

if __name__ == '__main__':
    main()