import json

def main():
    data = {
        'name' = 'Rob',
        'language' = 'Python'
    }

    with open('test.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)


if __name__ == '__main__':
    main()