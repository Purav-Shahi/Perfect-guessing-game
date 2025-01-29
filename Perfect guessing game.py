import random

n = random.randint(1, 100)
guesses = 0

while True:
    guesses += 1
    a = int(input("Guess the number: "))

    if a > n:
        print("Lower number please.")
    elif a < n:
        print("Higher number please.")
    else:
        print(f"Congratulations! You guessed the number {n} in {guesses} attempts.")
        break
