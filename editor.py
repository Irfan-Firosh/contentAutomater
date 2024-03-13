from moviepy.editor import *
import os
import random

screenshotDir = "screenshots"
voiceoverDirectory = "voiceovers"
gameplayDirectory = "gameplays"
finalVideoDirectory = "finalVideos"
scaleFactor = 1.2 # Scaling Percent of Video

def createClip(screenshot, voiceover):
    imageClip = ImageClip(screenshot)
    audioClip = AudioFileClip(filename=voiceover)
    imageClip = imageClip.set_duration(audioClip.duration)
    videoClip = imageClip.set_audio(audioClip)
    videoClip = videoClip.resize(scaleFactor)
    return videoClip

def compileClips(post_id, comment_ids):
    clips = []
    postSS = f"{screenshotDir}/{post_id}_post.png"
    postVoiceover = f'{voiceoverDirectory}/post-{post_id}.mp3'
    postClip = createClip(postSS, postVoiceover)
    clips.append(postClip)
    for comment in comment_ids:
        commentSS = f'{screenshotDir}/{comment}_comment.png'
        commentVoiceover = f'{voiceoverDirectory}/post-{post_id}-comment-{comment}.mp3'
        commentClip = createClip(commentSS, commentVoiceover)
        clips.append(commentClip)
    print(len(clips))
    finalClip = concatenate_videoclips(clips=clips)
    finalClip = finalClip.set_position(("center", "center"))
    return finalClip

def finalVideo(post_id, comment_ids):
    gameplayIndex = random.randint(1, 2)
    startTime = 0
    if gameplayIndex==1:
        startTime = random.randint(0, 540)
    if gameplayIndex==2:
        startTime = random.randint(0, 1800)
    compiledClips = compileClips(post_id, comment_ids)
    gameplayClip = VideoFileClip(filename=f'{gameplayDirectory}/gameplay-{gameplayIndex}.mp4')
    endTime = int(compiledClips.duration)
    gameplayClip = gameplayClip.subclip(startTime, startTime+endTime)
    clips = [gameplayClip, compiledClips]
    finalVideo = CompositeVideoClip(
        clips
    )
    output_file = f'{finalVideoDirectory}/{post_id}.mp4'
    finalVideo.write_videofile(
        output_file,
        codec="mpeg4",
        threads="12",
        bitrate="8000k"
    )

""" def file_exists(sspath, commentpath) -> bool:
    if os.path.exists(sspath) and os.path.exists(commentpath):
        return True
    return False """