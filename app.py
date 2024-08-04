import streamlit as st
from dotenv import load_dotenv

load_dotenv() ##load all the nevironment variables
import os
import re
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """


## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,prompt):

    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

st.title("YouTube Transcript to Detailed Notes Converter")

def get_video_id(youtube_url):
    # Regex to match various YouTube video URL formats
    match = re.search(r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/(?:watch\?v=|embed\/|v\/|.+\/.+\/)?([^"&?\/\s]{11})', youtube_url)
    return match.group(1) if match else None

youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = get_video_id(youtube_link)
    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    else:
        st.error("Invalid YouTube URL. Please enter a valid link.")


if st.button("Get Detailed Notes"):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)