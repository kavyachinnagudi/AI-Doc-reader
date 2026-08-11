import streamlit as st 
import os 
from dotenv import load_dotenv 
import google.generativeai as genai 

# Load environment variables
load_dotenv() 

# Read API key 
api_key = os.getenv("GOOGLE_API_KEY") 

if not api_key:
    st.error("GOOGLE_API_KEY is missing from your .env file!")
    st.stop()

# Configure Gemini 
genai.configure(api_key=api_key) 

# Load model 
model = genai.GenerativeModel("gemini-3.5-flash") 

# Streamlit UI
st.title("AI Document Assistant") 
question = st.text_input("Ask anything") 

if st.button("Generate"): 
    if question.strip():
        response = model.generate_content(question) 
        st.write(response.text)
    else:
        st.warning("Please enter a question first.")