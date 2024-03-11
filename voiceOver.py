import pyttsx3
from gtts import gTTS

voiceoverDirectory = "voiceovers"

#Creating a voiceover function
def createVoiceover(comment_id, inp, post_id):
    path = f'{voiceoverDirectory}/post-{post_id}-comment-{comment_id}.mp3'
    tts = gTTS(text=inp, lang='en')
    tts.save(path)
    return path

def postVoiceover(post_id, inp):
    path = f'{voiceoverDirectory}/post-{post_id}.mp3'
    tts = gTTS(text=inp, lang='en')
    tts.save(path)
    return path