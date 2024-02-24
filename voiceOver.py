import pyttsx3

voiceoverDirectory = "Voiceovers"

#Creating a voiceover function
def createVoiceover(comment_id, text):
    engine = pyttsx3.init()
    path = f'{voiceoverDirectory}/comment-{comment_id}.mp3'
    engine.save_to_file(text, path)
    engine.runAndWait()
    return path
