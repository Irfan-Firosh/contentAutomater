import os

ssDir = "screenshots"
finalDir = "finalVideos"
voiceDir = "voiceovers"

def delSS():
    for ss in os.listdir(ssDir):
        path = os.path.join(ssDir, ss)
        print(path)
        os.remove(path)

def delVoiceovers():
    for voice in os.listdir(voiceDir):
        path = os.path.join(voiceDir, voice)
        print(path)
        os.remove(path)

def delFinal():
    for finalVid in os.listdir(finalDir):
        path = os.path.join(finalDir, finalVid)
        print(path)
        os.remove(path)
