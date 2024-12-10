import sys
import unicodedata
import argparse

def get_only_men(data):
    return [row for row in data if 'M' in row[0]]

def get_only_women(data):
    return [row for row in data if 'K' in row[0]]

def get_first_letters_only(data):
    seen = {}
    for row in data:
        first_letter = row[2][0]
        if first_letter in seen:
            seen[first_letter] += int(row[1])
        else:
            seen[first_letter] = int(row[1])
    return [["", str(seen[letter]), letter] for letter in sorted(seen.keys(), key=lambda x: seen[x], reverse=True)]

def capitalize(data):
    return [[row[0], row[1], row[2].capitalize()] for row in data]

def uppercase(data):
    return [[row[0], row[1], row[2].upper()] for row in data]

def lowercase(data):
    return [[row[0], row[1], row[2].lower()] for row in data]

def ascify_polish_letters(data):
    return [[row[0], row[1], unicodedata.normalize('NFKD', row[2]).encode('ascii', 'ignore').decode('ascii')] for row in data]

def get_only_names(data):
    return [[row[2]] for row in data]

def read_data():
    lines = sys.stdin.read().strip().split('\n')
    return [line.split(',') for line in lines[1:]]

def print_data(data):
    for row in data:
        print(','.join(row))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process data based on the specified operations.")
    parser.add_argument("operations", nargs='+', choices=[
        "men",
        "women",
        "firstletters",
        "uppercase",
        "capitalize",
        "lowercase",
        "ascii",
        "names"
    ], help="The operations to perform on the data in sequence.")

    args = parser.parse_args()

    operations = {
        "men": get_only_men,
        "women": get_only_women,
        "firstletters": get_first_letters_only,
        "uppercase": uppercase,
        "lowercase": lowercase,
        "capitalize": capitalize,
        "ascii": ascify_polish_letters,
        "names": get_only_names
    }

    data = read_data()

    for operation in args.operations:
        data = operations[operation](data)

    print_data(data)