import openai
import re
import streamlit as st 


@st.cache_data
def generate_blog_post(text):
    # Split the text into chunks of at most 2048 characters
    text_chunks = re.findall('.{1,2048}', text, flags=re.DOTALL)

    # Generate a blog post from each chunk
    blog_post_chunks = []
    for chunk in text_chunks:
        prompt = f"Generate a blog post in markdown format based on the following text:\n\n{chunk}\n\n"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        blog_post_chunks.append(response.choices[0].text.strip())

    # Concatenate the generated blog post chunks into a single string
    blog_post = "\n\n".join(blog_post_chunks)

    return blog_post
