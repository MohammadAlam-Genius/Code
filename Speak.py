
import pyttsx3
n = input("Input what you want to hear :")
object = pyttsx3.init()
object.say(n)
object.runAndWait()
