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
        comments = youtube.get_video_comments(vid_id[1])
    elif (platform == "mastodon.social"):
        id = arr[3] + "/" + arr[4]
        comments = mastodon_social.get_toots_after_main_toot(id)
    elif (platform == "www.reddit.com"):
        comments = reddit.get_reddit_comments(link)
    else:
        comments = "Please input a youtube.com, mastodon.social, or reddit.com link with the https:// prefix."
    return comments

i_link = input("Enter a Youtube, Mastodon, or Reddit Link: ")
comments = link_parser(i_link)
print(groq.groq_analysis(comments))