'''from gtts import gTTS
import playsound
tts = gTTS("hello")
tts.save('out.mp3')
playsound.playsound('out.mp3')'''

import pyttsx3
 
# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()
 
# say method on the engine that passing input text to be spoken
engine.say('Hello sir, how may I help you, sir.')
 
# run and wait method, it processes the voice commands.
engine.runAndWait()