Objective: The primary goal of this project is to leverage the power of AI to automate the process of generating detailed notes from YouTube transcripts.

Tech stack used:
a.	youtube-transcript-api: It allows us to get the transcripts/subtitles for a video. It also works for automatically generated subtitles, supports translating subtitles and it does not require a headless browser, like other selenium-based solutions do!
b.	google-generativeai: As we must require a model from - To summarize. 
c.	streamlit: friendly UI

Workflow:
YouTube video link -----> extract the transcript text (YouTubeTranscriptApi) -------> model (prompt + transcript_text) -----> result (250 words).

Uses:
1.	Improved Learning: Converts video content into structured, easily digestible notes, which can help in studying and review.
2.	Time Efficiency: Reduces the need for manual note-taking, saving time for users who need to extract information from multiple videos.
3.	Enhanced Productivity: As it converts video content into organized notes, helping professionals and students stay organized and focused on relevant information.
