from googletrans import Translator
import pyttsx3

engine = pyttsx3.init()

result = Translator().translate('感觉是你的。工作很难', dest='en')
print(result.text)
engine.say(result.text)
engine.runAndWait()

