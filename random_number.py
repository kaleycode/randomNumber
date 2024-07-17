import random
print("Guess a random number game!")
print("You are going to guess a number between 1 and 1000000.")
attempt = 1
while True:
  myNumber = random.randint(1, 1000000)
    
  userguess=int(input("Go on! Guess a random number between 1 and 1000000: "))
  if userguess < 0:
    print("It's not a negative number! It is between 1 and 1000000.")
    attempt += 1
    continue
  if userguess > 1000000:
    print("That's not a number between 1 and 1000000!")
    continue
  if userguess < myNumber:
    print("Too low!")
    attempt +=1
    continue
  if userguess > myNumber:
    print("Too high!")
    attempt +=1
    continue
  
  if userguess == myNumber:
    print("You are a winner!")
    break
print("It took you", attempt, "attempt(s) to get the correct answer.")