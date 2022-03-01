from numpy import random


class GuessNumber:
    def __init__(self):
        self.guesses = 0
        self.min = self.start_number()
        self.max = self.end_number()
        self.number = random.randint(self.min, self.max)

    def start_number(self):
        starting_number = input("Enter the starting number: ")
        if starting_number.isdigit():
            return int(starting_number)

        else:
            print(f"{starting_number} is not valid, Please enter valid integer positive starting number")
            return self.start_number()

    def end_number(self):
        try:
            ending_number = input("Enter the ending number: ")
            ending_number = int(ending_number)
            if ending_number <= self.min:
                print(f"ending number can't be less than {self.min + 1}")
                return self.end_number()
            else:
                return ending_number

        except Exception as e:
            print(f"{ending_number} is not valid, Error:{e}")
            return self.end_number()

    def play(self):
        while True:
            try:
                guessed_number = input("try to guess the number: ")
                guessed_number = int(guessed_number)
                if guessed_number < self.min or guessed_number > self.max:
                    print(f"{guessed_number} is not valid, can't be less than {self.min} or more than {self.max}")
                    return self.play()
                elif guessed_number > self.number:
                    self.guesses += 1
                    print("Your guess was over.")
                elif guessed_number < self.number:
                    self.guesses += 1
                    print("You guess was under.")
                else:
                    self.guesses += 1
                    if guessed_number == self.number:
                        print(f"you guessed it right, take {self.guesses} guess")
                        break
            except Exception as r:
                print(
                    f"{guessed_number} is not valid, Error: {r}")
                return self.play()


game = GuessNumber()
game.play()
