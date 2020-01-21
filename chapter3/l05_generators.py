def main():
    for n in fibonacci():
        if(n > 1000):
            break
        print(n, end=', ')


def fibonacci():
    current, nxt = 0, 1

    while True:
        current, nxt = nxt, nxt + current
        yield current

if __name__ == '__main__':
    main()