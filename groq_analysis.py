from lib2to3.btm_utils import tokens
from groq import Groq

tokens_file = read_tokens('tokens.txt')
API_KEY = tokens_file.get('GROQ_API_KEY')

def groq_analysis(comments):
    client = Groq(
        API_KEY,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "GIVE 1 SENTENCE REASONING. PROVIDE OVERALL SCORE 1-10, 1 BEING NEGATIVE, 10 BEING POSITIVE. OVERALL SCORE COMES BEFORE THE REASONING. THERE WILL BE MULTIPLE COMMENTS. JUST GIVE THE OVERALL SCORE AND A ONE SENTENCE REASONING WITH HEADERS, NOTHING MORE."
                           "THE ANALYSIS IS ABOUT HOW THE SENTIMENT OF THE COMMENT RELATING TO THE MEDIA ABOVE. GIVE A SENTIMENT RATING SHOW HOW GOOD THE CONTENT WAS."
                           "EACH COMMENT WILL BE ON A NEW LINE. "
                           "Analyze the following COMMENTS and respond with an overall score of how positive or negative the comments are: " + comments,

            }
        ],
        model="llama3-8b-8192",
        max_tokens=1000,  # Set to 1 to get a single response
    )

    sentiment_analysis = chat_completion.choices[0].message.content
    return (sentiment_analysis)