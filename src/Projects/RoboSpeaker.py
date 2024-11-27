import pyttsx3

engine = pyttsx3.init()
intro = "Welcome! I am RoboSpeaker. Created by Atharva", "Type q if you want to exit"
print(intro)
engine.say(intro)
engine.runAndWait()
while True:
    text = input("Enter something you want me to Speak: ")
    if text == "q":
        end = "Bye Bye!"
        engine.say(end)
        engine.runAndWait()
        break
    engine.say(text)
    engine.runAndWait()

engine.stop()
