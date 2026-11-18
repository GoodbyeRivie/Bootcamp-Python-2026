import random

print("Level 1: Easy")
print("Level 2: Normal")
print("Level 3: Hard")
level = int(input("Masukkan Level 1-3: "))

if level == 1 :
  max_angka = 10
elif level == 2 :
  max_angka = 50
else : 
  max_angka = 100

secret_number = random.randint(1, max_angka)
guess = 0

while guess != secret_number :
  print("Rentang Angka 1 - ", max_angka)
  guess = int(input("Your Guess: "))

  if guess > max_angka or guess < 1 :
    print("Angka Di Luar Rentang!")
    break
  elif guess > secret_number :
    print("Too High!")
  elif guess < secret_number :
    print("Too Low!")
  else :
    print("Correct!")