import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# Display title

st.image(r"ino_img.jpg")

# Display the PNG image
st.title("Emotional Analysis Distribution ")
st.write('This app performs emotional analysis Distribution.')


try:
    model = pickle.load(open(r"ea.pkl",'rb'))
    bow = pickle.load(open(r"bow1.pkl",'rb'))
except Exception as e:
    st.error(f"An error occurred: {e}")



# Text input for user statement
user_input = st.text_area("Enter a emotional analysis statement:")

if user_input:
    # Transform the user input using the loaded CountVectorizer
    user_input_transformed = bow.transform([user_input])
    
    # Predict the sentiment using the loaded model
    prediction = model.predict(user_input_transformed)[0]
    

if st.button("Submit"):
    if prediction == 0:
        st.write("Sad")
        st.image(r"sad.jpeg",width = 150)
    elif prediction == 1:
        st.write("Joy")
        st.image(r"joy.png",width = 150)
    elif prediction == 2:
        st.write("Love")
        st.image(r"love.jpeg",width = 150)
    elif prediction == 3:
        st.write("Anger")
        st.image(r"angry.png",width = 150)
    elif prediction == 4:
        st.write("Fear")
        st.image(r"fear.png",width = 150)
    elif prediction == 5:
        st.write("Surprise")
        st.image(r"surprise.jpeg",width = 150)
