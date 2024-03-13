import streamlit as st
import google.generativeai as genai
import random

genai.configure(api_key='YOUR_API_KEY')  # Replace 'YOUR_API_KEY' with your actual API key

def prompt(manhwa_title):
    prompt_parts = [
        f"'As a avid manhwa reader with a wide range of preferences,"
        f"recommend five manhwas similar to the given title: {manhwa_title},"
        f"Also for each manhwa, explain why you find it similar to the given title and add --- before recommending the next manhwa'",
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
        for i, recommendation in enumerate(recommendations, start=1):
            text_color = '#000000'
            background_color = '#' + '%06x' % random.randint(0, 0xFFFFFF) 
            style = f"color: {text_color}; background-color: {background_color}; padding: 10px; border-radius: 15px; margin-bottom: 45px;"
            recommendation_text = recommendation.replace('**', '<strong>', 1).replace('**', '</strong>', 1)
            st.markdown(f"<div style='{style}'>{recommendation_text}</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
