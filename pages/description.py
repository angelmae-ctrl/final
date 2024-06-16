import streamlit as st

st.title("Description of Different Streamlit Application")


st.header('Machine Learning Compiled Application')
st.image("./my_pict/feelings1.png")
st.image("./my_pict/feelings2.png")

with st.expander("😊 Emotion Detector 😊"):
    st.markdown("""
    
    #
                An emotion analyzer in machine learning interprets feelings by studying labeled examples of emotions such as happiness, sadness, fear, nervous or anger. 
                It trains models to recognize patterns in how emotions are conveyed through words and sentences. 
                
    """, unsafe_allow_html=True)

st.header('🎌  Image Classification 🎌 ')
st.image("./my_pict/archery.png")
st.image("./my_pict/sportbalanceimg.png")
st.image("./my_pict/sportsimg.png")

with st.expander("Image Classification of Different Sports"):
    st.markdown("""
    
    #
                In machine learning for image classification in sports, the first step involves gathering a large set of images that show different sports like basketball, soccer, tennis, and others. 
                These images are then prepared and formatted so that a computer can understand and analyze them. This process sets the foundation for training algorithms to recognize and categorize sports images based on their visual features.
    """, unsafe_allow_html=True)

st.header('🔍Prediction')
st.image("./my_pict/predict.png")


with st.expander("🌦️ Weather Predictor 🌦️"):
    st.markdown("""
    
    In weather prediction using machine learning, we download datasets from sources like Kaggle, which provide historical data on temperature, humidity, wind speed, and atmospheric pressure. 
                These datasets are then fed into machine learning algorithms such as decision trees or random forests. The algorithms analyze past weather patterns to learn relationships between these variables and outcomes like rain or sunshine. 
                By training on historical data, the models can forecast future weather conditions. This technology is crucial for predicting weather patterns, offering insights beneficial for agriculture, disaster management, and daily planning.
                         
    """, unsafe_allow_html=True)
