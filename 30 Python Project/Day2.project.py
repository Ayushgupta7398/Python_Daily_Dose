                              # project 2
                       # Stone ,Peper, Scissor Game 
import random
# system = random.choice([ "s","p","sc"])

choice_name = { "s": "stone", "p":"peper","sc":"scissor"}

user_score = 0
system_score = 0
draw = 0

print("🎮 Welcome to stone ,peper,scissor Game!")
print("Instructions: Choose:\n's' for stone \n'p' for peper \n'sc' for scissor")


while True:
    user_input = input("enter the your choice :"). lower()
    system = random.choice(["s", "p", "sc"])  # This should be inside the while loop.

    #validation update
    if user_input  not in [ "s", "p","sc"]:
        print("❌ invalid choice")
        continue


    print(f"\n🧠system choice:",choice_name[system])
    print(f"🙋user choice:",choice_name[user_input])

    #game logic
                 # for draw
    if user_input == system:
        print("\n it is a draw!")     
        draw +=1
                   #for win 
    elif (system =="s"and user_input == "p") or\
        (system== "p" and user_input == "sc") or\
        (system== "sc" and user_input =="s") :
        print("\n 🎉 You win!")
        user_score += 1
                #for lose
    else:
        print( "\n 😢 You lose!")
        system_score += 1
                
                #for play again
    play_again = input("\n do you want to play again:(y/n)").lower()
    if play_again != "y":
       break


         # final result 
print("\n🏁 Game Over!")
print(f"✅ Your Score: {user_score}")
print(f"💻 System Score: {system_score}")
print(f"➗ Draws: {draw}")

if (user_score>system_score):
    print("\nyou win overall!")
elif( user_score <system_score):
    print("\nsystem won the game overa; !")
else:
    print( " \nThis is a draw overall!")

    


