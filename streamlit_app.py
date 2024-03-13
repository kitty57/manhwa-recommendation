import streamlit as st
import google.generativeai as genai
import random

genai.configure(api_key='AIzaSyDlBFVsmV8pao6Ax-bcR0dc5h4CusiNCsc')  

def prompt(manhwa_title):
    prompt_parts = [
        f"'As a vivid manhwa reader who has read all manhwas of all genres present online,"
        f"recommend five manhwas similar to the given manhwa: {manhwa_title},give a short description of the chosen manhwa too."
        f"Also for each manhwa, explain why you find it similar to the given manhwa and add --- before recommending the next manhwa'",
    ]
    return prompt_parts
    
def recommend(manhwa_title, model):
    human_prompt = prompt(manhwa_title)
    response = model.generate_content(human_prompt)
    return response.text

def main():
    st.title('Manhwa Recommendation App')
    manhwa_title = st.text_input('Enter the manhwa title:')
    if manhwa_title:
        model = genai.GenerativeModel(model_name="gemini-pro")
        response = recommend(manhwa_title, model)
        recommendations = response.split('---') 
        st.write("Recommendations and Why you'd like them")
        st.markdown(recommendations)

if __name__ == '__main__':
    main()
