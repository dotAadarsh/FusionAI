import streamlit as st  
from streamlit_quill import st_quill
import openai
from transcript import transcript_from_video
from generateBlog import generate_blog_post

st.set_page_config(page_title="Fusion.AI | Creator", page_icon="None", layout="wide", initial_sidebar_state="auto", menu_items=None)

st.subheader("Experience the power of AI - your personalized content creator")


def generateImage(imageType, imageStyle, imageContent):
    try:
        response = openai.Image.create(
        prompt= f"Image Type: {imageType}, Image Style: {imageStyle}, ImageContent: {imageContent}",
        n=1,
        size="256x256"
        )

        image_url = response['data'][0]['url']

        return image_url

    except:
        return ""


def generateTweet(mood_prompt, topic):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write a {mood_prompt}Tweet about {topic} in less than 120 characters:\n\n",
        temperature=0,
        max_tokens=120,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )

    return response["choices"][0]["text"]

tool = st.radio(
    "What would you like to create?",
    ('Tweet', 'Blog', 'Image', 'Video'))

if tool == 'Tweet':
    st.header('Generate Tweets')
    topic = st.text_input(label="Topic (or hashtag)", placeholder="AI")
    mood = st.text_input(
        label="Mood (e.g. inspirational, funny, serious) (optional)",
        placeholder="creative",
    )

    OnGenerateTweet = st.button("Generate Tweet")
    if OnGenerateTweet:
        st.text_area("Generated Tweet: ", generateTweet(mood, topic))

elif tool == 'Blog':
    st.header("Create blog for your content")
    st.info("Under construction!")
    topic = st.text_input("Enter the topic")
    style = st.text_input("Style")
    audience = st.text_input("Audience")

    OnGenerateBlog = st.button("Generate Blog")
    if OnGenerateBlog:
        st.info("Come back soon!")

elif tool == 'Image':
    st.header("AI - Imager")
    st.caption("Powered by Dall-E")
    imageType = st.text_input("Image Type", "portrait")
    imageStyle = st.text_input("Image Style", "painterly")
    imageContent = st.text_input("Image Content", "A nightcity with tall skyscrappers and flying cars")

    OnclickGenerateImage = st.button("Generate Image")
    if OnclickGenerateImage:
        image_url = generateImage(imageType, imageStyle, imageContent)
        st.image(image_url) 
        
elif tool == 'Video':
        uploadedVideo = st.file_uploader("Please upload a video", type='.mp4')
        if uploadedVideo:
            whisper_response = transcript_from_video(uploadedVideo)
            transcript = whisper_response["text"]
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.video(uploadedVideo)
                st.subheader("Extracted Transcript")
                st.write(transcript)

            with col2: 
                c1, c2 = st.columns([3, 1])

                c2.subheader("Parameters")

                with c1:
                    st.subheader("Markdown AI-Gnerated Blog fromo Video Editor")
                    content = st_quill(
                        value=generate_blog_post(transcript),
                        placeholder="Write your text here",
                        html=c2.checkbox("Return HTML", False),
                        readonly=c2.checkbox("Read only", False),
                        key="quill",
                    )

                    if content:
                        st.subheader("Content")
                        st.text(content)