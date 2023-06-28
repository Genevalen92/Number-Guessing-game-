#guess the number name 
import random
name = input("Hello what is your name? ")

print(f"Well,{name} I am thinking of a number between 1 and 50")
secretNumber = random.randint(1, 25)

#print(f"Debug: the number I am thinking is {secretNumber} ")

for guessesTaken in range (1, 8):
  print("Take a guess.")
  guess = int(input())
  
  if guess < secretNumber:
    print("Your guess is too low")
  elif guess > secretNumber:
    print("Your guess is too high")
  else:
    break  

if guess ==  secretNumber:
  print(f"Good job {name}! you guessed my number in {guessesTaken} guesses.")
else:
  print(f"Nope. the number I was thinking of was {secretNumber}. ")        
