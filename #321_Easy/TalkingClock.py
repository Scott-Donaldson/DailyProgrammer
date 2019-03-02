import datetime
import win32com.client as wincl

Currenttime = datetime.datetime.now()
time = Currenttime.strftime("%H:%M %p")

Sentence = "It's"
Sentence += " " + time

speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak(Sentence)
