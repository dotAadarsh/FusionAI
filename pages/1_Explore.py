import streamlit as st
from googleapiclient.discovery import build
from transcript import generate_transcript
from generateBlog import generate_blog_post
import openai
from tweets import tweets
from streamlit_pills import pills

openai.api_key = st.secrets["OPENAI_KEY"]
DEVELOPER_KEY = st.secrets['yt_api_key']
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

st.set_page_config(page_title="Fusion.AI", page_icon="None", layout="wide", initial_sidebar_state="auto", menu_items=None)

st.header("Explore the contents in the way you want!")
@st.cache_data
def get_keywords_description(keywords):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="provide me a small description in markdown for each of the following " + keywords,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    
    description = response["choices"][0]["text"]
    return description


@st.cache_data
def search_videos(query):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(q=query, type='video', videoDuration='short', part='id,snippet', maxResults=7).execute()
    videos = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append({
                'id': search_result['id']['videoId'],
                'title': search_result['snippet']['title'],
                'description': search_result['snippet']['description'],
                'publishedAt': search_result['snippet']['publishedAt'],
                'thumbnails': search_result['snippet']['thumbnails']['default']['url']
            })
    return videos


@st.cache_data
def get_keywords(transcript):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Extract important keywords mentioned in the following transcript: " + transcript,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    keywords = response["choices"][0]["text"]
    return keywords


query = st.text_input('Enter your search query', value="Artificial Intelligence")
videos = search_videos(query)


if len(videos) == 0:
    st.error('No videos found.')

else:
    for video in videos:
        
        with st.expander(video['title']):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(video['thumbnails'], use_column_width=True)
                st.write(video['description'])
                st.write(f"Published on {video['publishedAt']}")

                whisper_response = generate_transcript(f'https://www.youtube.com/watch?v={video["id"]}')
                transcript = whisper_response["text"]

                keywords = get_keywords(transcript)
                keyword_list = []
                if keywords.startswith("Keywords: "):

                    keyword_list = keywords[10:].split(", ")
                else:
                    keyword_list = keywords.split(", ")

                selected = pills("keywords", keyword_list)

            with col2:
                tab1, tab2, tab3, tab4 = st.tabs(["BLOG", "VIDEO", "AUDIO", "SOCIAL"])

                with tab1:
                    blog_response = generate_blog_post(transcript)
                    st.write(blog_response)
                
                with tab2:
                    video_url = f'https://www.youtube.com/watch?v={video["id"]}'
                    st.video(video_url)

                with tab3:
                    st.audio(data="./audio.mp4")
                    st.subheader("Transcript")
                    st.write(transcript)
                
                with tab4:
                    st.header("Related Tweets")
                    hashtag = keyword_list[1]
                    tweets(hashtag)

        st.markdown("---")
