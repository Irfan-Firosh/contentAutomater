import praw
import time
from tqdm import tqdm
from voiceOver import *
from wifiConnector import *
from screenShot import *
from editor import *
from clearDir import *
import config

def main():
    connect("PAL3.0")
    time.sleep(15)
    agent = "chrome:redditStatsMapper:v1.1.1 (by /u/Experimnet)"
    reddit = praw.Reddit(
        client_id =config.praw_client_id,
        client_secret = config.praw_client_secret,
        password=config.praw_password,
        user_agent=agent,
        username=config.praw_username,
    )

    path = "processedPosts.txt"

    submissions = reddit.subreddit("askreddit").top(time_filter="day", limit=5)
    clear_file(path)

    existingPostIDs = getExistingPostIDs(path)
    
    # Looping through all the IDs
    for submission in tqdm(submissions, desc="Generating Content", unit= "comments"):
        if (submission.id in existingPostIDs or submission.over_18):
            continue
        addID(submission, path)
        takeSS(submission.url, submission.id, "", 1)
        postVoiceover(submission.id, submission.title)
        getCommentFromPost(submission)

    # Generating Video
    genVideo()

def getExistingPostIDs(file_path) -> set:
    existingIDs = set()
    try:
        with open(file_path, "r") as file:
            for line in file:
                existingIDs.add(line.strip())
    except Exception as e:
        print("Error reading the file")
    
    return existingIDs
 
def clear_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = len(file.readlines())
            print('Total Line:', lines)
            if (lines > 100):
                with open(file_path, "w") as file:
                    pass
    except Exception as e:
        print("Error clearing the file")

def addID(post, file_path):
    try:
        with open(file_path, "a") as file:
            file.write(post.id + "\n")
    except Exception as e:
        print("Error writing to the file")

def getCommentFromPost(post):
    post.comments.replace_more(limit=0)
    comments = post.comments.list()
    sorted_comments = sorted(comments, key=lambda comment: comment.score, reverse=True)
    comment_count = 0
    for comment in sorted_comments:
        if (len(comment.body.split()) > 100 or len(comment.body.split()) > 100 ):
            continue
        addComment(comment, post)
        comment_count += 1
        if comment_count >= 3:
            break

def addComment(comment, post):
    id = comment.id
    text = comment.body
    # Add audio to each audio, or add it to a file
    createVoiceover(id, text, post.id)
    # Generate ss
    takeSS(post.url, post.id, comment.id, 2)

def genVideo():
    for post in config.success:
        comments = []
        if post in config.failPost:
            continue
        for comment in config.success[post]:
            if comment in config.failComment:
                continue
            comments.append(comment)
        finalVideo(post, comments)

def clearInventory():
    try:
        delSS()
        delVoiceovers()
    except:
        print("Error Clearing The File")

clearInventory()
main()
print(config.success)