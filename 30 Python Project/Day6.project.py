
                     #Live Typing Effect with live speaking (Robospeaker)

import pyttsx3
import time
import threading
# content  = "Python ..... is ...Typing..by ... itself!"

def speak_text(text):
     engine = pyttsx3.init()
     time.sleep(0.1)
     engine.say(text)
     engine.runAndWait()
 


if __name__ == '__main__':
    content = '''Hello! This is my Python project named (EchoType Pro) 
    for creating a Live Typing Effect with simultaneous voice narration. 
    It showcases how code can bring text to life, character by character, in real-time.
    A simple yet engaging demonstration of automation and text-to-speech.
    Thanku You from Ayush !
'''
    speech_thread = threading.Thread(target=speak_text, args=(content,))

    speech_thread.start()
    time.sleep(0.06)

    print("Typing Animation..")
    for char in content :
     print(char,end="",flush=True)
     time.sleep(0.06)

    speech_thread.join()


