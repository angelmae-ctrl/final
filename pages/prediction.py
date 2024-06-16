import streamlit as st
import pickle

# Load the trained NaiveBayesClassifier from the saved file
filename = './pages/health_impact_model.sav'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

st.title("🌬️ Air Quality Health Impact Predictor 🌬️")
st.subheader("Enter air quality details to predict the health impact class:")

# User inputs for air quality details
aqi_input = st.slider("AQI (Air Quality Index): ", 0, 500)
pm10_input = st.slider("PM10 (μg/m³): ", 0, 500)
pm2_5_input = st.slider("PM2.5 (μg/m³): ", 0, 500)
no2_input = st.slider("NO2 (ppb): ", 0, 200)
so2_input = st.slider("SO2 (ppb): ", 0, 100)
o3_input = st.slider("O3 (ppb): ", 0, 300)

# Function to make a prediction
def predict_health_impact_class(aqi, pm10, pm2_5, no2, so2, o3):
    # Features function to convert inputs into a dictionary format expected by the model
    def features(aqi, pm10, pm2_5, no2, so2, o3):
        return {
            'aqi': aqi,
            'pm10': pm10,
            'pm2_5': pm2_5,
            'no2': no2,
            'so2': so2,
            'o3': o3
        }

    # Apply features function to user inputs
    test_data = features(aqi, pm10, pm2_5, no2, so2, o3)

    # Use the model to get the predicted health impact class
    prediction = loaded_model.classify(test_data)
    return prediction

# Display button and result
if st.button('Predict'):
    predicted_class = predict_health_impact_class(
        aqi_input, pm10_input, pm2_5_input, no2_input, so2_input, o3_input)
    
    st.text("The predicted health impact class based on the given air quality details is:")
    st.text(predicted_class)