import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(i):
    if i in data:
        return "\n".join(data[i])
    elif len(get_close_matches(i, data.keys())) > 0:
        while True:
            a = input("Did you mean %s instead? (Y/N): " % get_close_matches(i, data.keys())[0]).lower()
            if a == 'y':
                return "\n".join(data[get_close_matches(i, data.keys())[0]])
            elif a == 'n':
                return "The word doesn't exist. Please double check it."

            else:
                print("invalid input")
                continue

    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ").lower()
print(translate(word))