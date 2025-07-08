 
                               #RoboSpeaker 
                             #you can talk by it.

import pyttsx3

engine = pyttsx3.init()


if __name__ =='__main__':
    welcome_message =("Welcom to RoboSpeaker created by Ayush :")
    print(welcome_message)
    engine.say(welcome_message)
    engine.runAndWait()

    while True:
            input_message = input("Enter what you want to say :")
            
            if input_message.lower() == "stop now":
                  print("Thank you ! ")
                  print("Bye Bye")
                  engine.say("thank you for coming !")
                  engine.say("Bye Bye")
                  engine.runAndWait()

                  break
            engine.say(input_message)
            engine.runAndWait()

            
