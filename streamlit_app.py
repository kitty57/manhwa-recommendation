import streamlit as st
import google.generativeai as genai
import random

genai.configure(api_key='AIzaSyDlBFVsmV8pao6Ax-bcR0dc5h4CusiNCsc')  

def prompt(manhwa_title):
    prompt_parts = [
        f"'As an avid manhwa reader who has extensively explored manhwas across all genres available online, please provide a brief synopsis of the selected manhwa:{manhwa_title}. Additionally, recommend five manhwas that are similar to the chosen manhwa:{manhw_title}. For each recommended manhwa, explain why you consider it similar to the chosen manhwa. Please add '---' before recommending the next manhwa.'",
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
        for i in recommendations:
            st.markdown(i)

if __name__ == '__main__':
    main()
