import youtube
import mastodon_social
import reddit
import groq_analysis as groq
from flask import Flask, request, jsonify

def link_parser(link):
    arr = link.split("/")

    platform = arr[2]
    comments = "" 
    if (platform == "www.youtube.com"):
        vid_id = arr[3].split("=")
        comments = youtube.get_video_comments(vid_id)
    if (platform == "mastodon.social"):
        id = arr[3] + "/" + arr[4]
        comments = mastodon_social.get_toots_after_main_toot(id)
    if (platform == "www.reddit.com"):
        r_link = arr.join("/")
        comments = reddit.get_reddit_comments(r_link)
    return comments

app = Flask(__name__)

# This function will process the link (dummy processing here)
def process_link(link):
    # Example: Just returning the reversed link as "processed"
    return link[::-1]

@app.route('/process-link', methods=['POST'])
def handle_link():
    data = request.get_json()
    link = data.get('link')

    if not link:
        return jsonify({"error": "No link provided"}), 400

    # Process the link using function
    
    # output below after result with function's return
    return jsonify({"result": groq.groq_analysis(link_parser(link))})

if __name__ == '__main__':
    app.run(debug=True)