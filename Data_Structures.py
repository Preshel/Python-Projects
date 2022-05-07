import random
name = (input("What is Your name: "))
print(f"{name}, WELCOME to PRESHEL'S DEN")
print("The name of this game is 'GUESS ME'.\nThe rules are simple: \n1. You select two numbers."
      "\n2. A number will be generaated by the computer within the range of your chosen numbers. \n3. You have 5 chances to guess the correct number."
      "\nIf you win, you get 5 points. If you lose, you get nothing")
print(f"{name}, are you ready to play the game? If you are, press ENTER: ")
user = input()

lower_bound = int(input("Enter a low number: "))
upper_bound = int (input("Enter a high number: "))
computer = random.randint(lower_bound, upper_bound)
i = int(0)
while i in range(5):
      user = int(input("Take a guess: "))
      remainder = 4 - i
      if user == computer:
            print("Congratulations")
            break
      elif user < computer and remainder > 1:
            print("Try Again! You guessed too small")
      else:
            if user > computer and remainder > 1:
                print("Try Again! You guessed too big")
      i = i + 1
      if remainder > 1:
            print(f"You have {remainder} number of times left")
      else:
            if user < computer and remainder == 1:
                print("Try Again! You guessed too small \nThis is your last chance!")
            else:
                if user > computer and remainder == 1:
                      print("Try Again! You guessed too big \nThis is your last chance!")

if remainder == 0:
      print(f"You Lose. The correct answer is {computer}")