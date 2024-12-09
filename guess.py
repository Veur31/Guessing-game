import random

def randomnum():
    random_num = random.randint(1,100)

    print("Welcome to guessing game")
    print()
    attemp = 0
    max_attempt = 5
    while attemp < max_attempt:
        try:
            Num = int(input("Enter your guess: "))
            attemp +=1

            if Num < random_num:
                print("Your guess is too low")
            elif Num > random_num:
                print("Your guess is too high")
            else:
                print(f"Your guess it correctly, the random number is {random_num}")
                break
        except ValueError:
            print("Please input a number: ")
    if attemp == max_attempt and Num != random_num:
        print(f"No guess left, the number is {random_num}")
randomnum()
        
            




