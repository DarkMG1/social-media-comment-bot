from lib2to3.btm_utils import tokens

import googleapiclient.discovery
from helper import read_tokens

tokens_file = read_tokens('tokens.txt')
API_KEY = tokens_file.get('GOOGLE_API_KEY')
max = 100

def get_video_comments(video_id):
    print("Finding Youtube Comments for Video ID: " + video_id)
    """Fetches comments from a YouTube video.

    Args:
        video_id: The ID of the YouTube video.

    Returns:
        A list of comments.
    """

    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

    comments_request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id
    )


    comments = []
    while True:
        response = comments_request.execute()

        for item in response['items']:
            comments.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])

        if 'nextPageToken' in response:
            comments_request = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                pageToken=response['nextPageToken']
            )
        else:
            break

    result = ""
    print("Found " + str(len(comments)) + " comments." + "\n")
    for i in range(0,max):
        result += comments[i] + "\n"
    return(result)

# get_video_comments("yxoi8CiyCcU")