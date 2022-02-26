from numpy import random
i = 0
while i < 1:
    starting_number = input("Enter the starting number: ")
    if starting_number.isdigit():
        starting_number = int(starting_number)
        i += 1

    else:
        print(f"{starting_number} is not valid, Pls enter valid integer positive starting number")
        continue

while True:
    try:
        ending_number = input("Enter the ending number: ")
        ending_number = int(ending_number)
        if ending_number <= starting_number:
            print(f"ending number can't be less than {starting_number+1}")
        else:
            break

    except Exception as e:
        print(f"{ending_number} is not valid, pls enter valid integer ending number the error code is -------{e}")

x = random.randint(starting_number, ending_number)

k = 0
while True:
    try:
        guessed_number = input("try to guess the number: ")
        guessed_number = int(guessed_number)
        if guessed_number < starting_number or guessed_number > ending_number:
            print(F"{guessed_number} is not valid, can't be less than {starting_number} or more than {ending_number}")
        else:
            k += 1
            if guessed_number == x:
                print(f"you guessed it right, take {k} guess")
                break

    except Exception as r:
        print(f"{guessed_number} is not valid, pls enter valid integer guessed number, the error code is ------- {r}")

