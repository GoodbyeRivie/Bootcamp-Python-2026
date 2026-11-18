import random

secret_number = random.randint(1, 100)
guess = 0

while guess != secret_number :
  guess = int(input("Your Guess: "))

  if guess > secret_number :
    print("Too High!")
  elif guess < secret_number :
    print("Too Low!")
  else :
    print("Correct!")