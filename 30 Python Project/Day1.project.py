
                        # THE PERFECT GUESS
import random
print("🎯 Welcome to THE PERFECT GUESS 🎯")
while True:
  num_to_guess = random.randint(1,100)
  number_of_try = 0

  while(True):
       guess = int(input("Guess the number between 1 to 100: "))
    
       number_of_try += 1

       if num_to_guess > guess:
           print("please guess higher:")

       elif num_to_guess < guess:
           print("please guess lower: ")

       else:
           print(f"Congratulations!\nyou guess the perfect number {num_to_guess} in {number_of_try} attemps.")
           break

  play_again = input("Do you want to play again? (y/n): ").strip().lower()
  if play_again != "y":
   print("Thanks for playing!\n see you soon.  ")
  break     


  
    
    