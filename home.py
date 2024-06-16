
import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "ITEQMT Machine Learning Application Portfolio", "👩🏻‍🎓"),
        Section("Main Page", "⚠️"),
        Page("pages/aboutme.py", "👨‍🎓THINGS ABOUT ANGEL", "1️⃣", in_section=True),
        Page("pages/description.py", "⚖️ STREAMLIT DESCRIPTION", "2️⃣", in_section=True),
        Page("pages/itqmtlearnings.py", "✨ITEQMT LEARNINGS", "3️⃣", in_section=True),
     
  
        Section("Sample Projects", "💼"),
        Page("pages/sentimentemotion.py", "✍ Basic Sentiment Analyzer", "1️⃣", in_section=True),
        Page("pages/imageclassifier.py", "🌟 Classification", "2️⃣", in_section=True),
        Page("pages/prediction.py", "💫 Prediction", "3️⃣", in_section=True),

        Section("Project Source Code","💻"),
        Page("pages/sentimentemotionanalyzer_src.py","🛠️ Sentiment Analyzer SRC", "1️⃣", in_section=True),
        Page("pages/imageclassifier_src.py","🛠️ Image Classificatiom SRC", "2️⃣", in_section=True),
        Page("pages/prediction_src.py","🛠️ Prediction SRC", "3️⃣", in_section=True),
        
    ]
)

hide_pages(["Thank you"])

st.markdown("---")
st.header("LAMIS, ANGEL MAE of BSIS 3B")
st.image("./my_pict/myself.jpg")
st.markdown("---")

with st.expander("🖥️ MACHINE LEARNING 🖥️ """):
    st.markdown("""

    #
        What is Machine Learning?
                
Machine learning is a subset of artificial intelligence (AI) that enables computers to learn and improve from experience without being explicitly programmed.
 It involves developing algorithms that can learn patterns and make data-driven predictions or decisions.
               
        Types of Machine Learning
                
* Supervised Learning: Involves training a model on labeled data, where the algorithm learns to map input to output based on example input-output pairs.
* Unsupervised Learning: Involves training a model on unlabeled data, where the algorithm learns patterns and structures without specific output labels.
* Reinforcement Learning: Involves training a model to make sequences of decisions, learning through trial and error based on feedback (reward or penalty) from its actions.

                
        Applications of Machine Learning
                
* Predictive Analytics: Forecasting future trends or behaviors based on historical data, such as sales forecasting or churn prediction.
* Image and Speech Recognition: Identifying objects in images, recognizing faces, or converting speech to text, powering applications like virtual assistants.
* Natural Language Processing (NLP): Processing and understanding human language, enabling sentiment analysis, chatbots, and language translation services.
    #""", unsafe_allow_html=True)

st.title('INTRODUCTION TO THIS APPLICATION')

st.markdown("""

WWelcome to the System Interface! We're thrilled to have you explore the world of image classification, emotion analyzer, and prediction. 
            This innovative app utilizes machine learning to identify sports, understand emotions, predict air quality, and assess health impacts. 
            All powered by Streamlit, this user-friendly interface empowers you to unlock the potential of data in a fun and interactive way.

            ### 🔎 Overview""", unsafe_allow_html=True)





st.markdown("""
Machine learning, a pivotal branch of artificial intelligence, enables computers to learn from data without explicit programming. 
By teaching algorithms with large sets of data, they can find patterns and connections that help them make accurate predictions and decisions. 
For example, algorithms trained on pictures of cats and dogs can tell them apart based on their different features. 
Machine learning is used in many areas, like improving facial recognition and spam blocking, powering self-driving cars, and assisting doctors in diagnosing illnesses. 
As machine learning advances, its impact on industries and daily life is expected to grow, as it continues to find insights and improve results across different fields.
                       
### ⭐⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 