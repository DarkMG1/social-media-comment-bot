import praw

from helper import read_tokens

# Replace these with your own credentials
tokens_file = read_tokens('tokens.txt')

client_id = tokens_file.get('REDDIT_CLIENT_ID')
client_secret = tokens_file.get('REDDIT_CLIENT_SECRET')
user_agent = tokens_file.get('REDDIT_USER_AGENT')

if not all([client_id, client_secret, user_agent]):
    print("Error: Missing API credentials. Please check your tokens.txt file.")
    exit(1)

def get_reddit_comments(post_url):
    # Initialize the Reddit instance
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)

    # Get the submission (Reddit post)
    try:
        submission = reddit.submission(url=post_url)
    except Exception as e:
        print(f"An error occurred while fetching the submission: {e}")
        exit(1)

    # Replace MoreComments to get all comments
    submission.comments.replace_more(limit=None)

    return submission.comments.list()
