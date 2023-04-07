import streamlit as st 
import streamlit.components.v1 as components

st.image("./assets/fusionai-logo.png")
st.header("Welcome to FusionAI")
st.subheader("Unify your media experience with ease")

st.header("The Design")
with st.expander("Figma design"):
    st.image("./assets/explore-page.png")
    st.image("./assets/InsiderView.png")

st.header("The plan")

with st.expander("Executive summary"):

        st.write("""
        Our app is a unique platform that offers both content creators and users an innovative way to generate and access various types of content. 
        The app has two interfaces: Explorer and Creator, where visitors can access various types of content, including videos, articles, audios, and tweets while creators can upload, edit and use AI tools to generate content.
        """)

        st.write("""
                Our app aims to solve the problem of time-consuming content creation and fragmented content discovery. 
                By offering multiple types of content in a single platform, we aim to increase user engagement and retention while offering creators an opportunity to monetize their content.
        """)

with st.expander("Market Analysis"):
    st.write("""
    The global content creation and discovery market is expected to reach $892.5 billion by 2027, with an annual growth rate of 16.8%. 
    The increasing demand for video content, podcasts, and other forms of digital media presents a significant opportunity for our app to succeed in the market.
    """)

with st.expander("Competitive Analysis"):
    st.write("""
    Our app faces competition from established content creation and discovery platforms such as YouTube, Medium, and Spotify. 
    However, our unique value proposition of offering multiple types of content in a single platform, along with AI generative tools for creators, sets us apart from competitors.
    """)
with st.expander("Marketing Strategy"):
    st.write("""
    Our app will be marketed primarily through social media, paid advertising, and partnerships with content creators and publishers. 
    We will also offer referral programs to incentivize users to invite their friends and family to use the app.
    """)

with st.expander("Revenue Model"):
    st.write("""
    We plan to generate revenue through a freemium model, where the app is free to access for users, but creators pay for premium tools and features. 
    We will also offer subscription plans for users to access premium content and an advertising model, where advertisers can display ads on the app.
    """)

with st.expander("Conclusion"):
    st.write("""
    Our app aims to provide a unique solution for content creators and users, offering multiple types of content in a single platform and AI generative tools to save time on content creation. 
    With a solid marketing strategy and revenue model, we are confident in our ability to succeed in the competitive content creation and discovery market.
    """)