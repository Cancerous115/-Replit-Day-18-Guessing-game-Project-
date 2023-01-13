print("Guess my number Game. 1-1,000,000!!!")
ponechoice = 66
attempts = 1
print()
while True:
    guess = int(input("What is your guess?"))
    if guess < 0:
      print("not recognized")
      exit()
    if guess > ponechoice:
        print("too high")
        attempts +=1
    elif guess < ponechoice:
        print("too low")
        attempts += 1
        continue
    elif guess == ponechoice:
      print("congrats on finally winning.")
      break
    else:
      print("No negatives...")
print("congrats on finally guessing correclty after", attempts, "attempts")

 