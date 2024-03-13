import os

import http.client
import httplib2
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow



client_secrets_file = "yt_0Auth.json"
cred_file = "token.json"


httplib2.RETRIES = 1

CLIENT_SECRET = 'yt_0Auth.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
PRIVACY_STATUS = 'public'

# authorize request and store credentials
def get_authenticated_service():
    credentials = None
    if (os.path.exists(cred_file)):
        credentials = Credentials.from_authorized_user_file(cred_file, SCOPES)
    
    if credentials is None or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
            credentials = flow.run_local_server(port=0)
            with open(cred_file, "w") as token:
                token.write(credentials.to_json())
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def initalize_upload(file, options):
    youtube = get_authenticated_service()
    try:
        insert_request = youtube.videos().insert(
            part="snippet,status",
            body={
              "snippet": {
                "title": options["title"],
                "description": options["description"],
                "tags": options["tags"],
                "categoryId": options["category"]
              },
              "status": {
                "privacyStatus": options["status"]
              }
            },
            media_body=MediaFileUpload(file)
        )
        response = insert_request.execute()
        return response
    except HttpError as e:
        print(f"An HTTP error {e.resp.status} for: " + file)
        return None