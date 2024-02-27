import pyttsx3
from gtts import gTTS

voiceoverDirectory = "voiceovers"

#Creating a voiceover function
def createVoiceover(comment_id, inp):
    path = f'{voiceoverDirectory}/comment-{comment_id}.mp3'
    tts = gTTS(text=inp, lang='en')
    tts.save(path)
    return path

#def createVoiceover(comment_id, text):
 #   engine = pyttsx3.init()
  #  path = f'{voiceoverDirectory}/comment-{comment_id}.mp3'
   # engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    #engine.save_to_file(text, path)
    #engine.runAndWait()
    #return path