secret_number = 37
guess = int(input("Masukkan Tebakanmu: "))

if guess > secret_number :
  print("Too High!")
elif guess < secret_number :
  print("Too Low!")
else :
  print("Correct!")