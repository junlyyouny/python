import speech
import time

response = speech.input("Say something, please.")
speech.say("You said " + response)


def callback(phrase, listener):
    if phrase == "再见":
        listener.stoplistening()
    speech.say(phrase)
    print(phrase)


listener = speech.listenforanything(callback)
while listener.islistening():
    time.sleep(.5)