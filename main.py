import youtube
import mastodon_social
import reddit
import groq_analysis as groq

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

groq.groq_analysis(link_parser())