import streamlit as st
import google.generativeai as genai
import random

genai.configure(api_key='AIzaSyDlBFVsmV8pao6Ax-bcR0dc5h4CusiNCsc')  

def prompt_with_answers(manhwa_title, user_answers):
    prompt_parts = [
        f'''As an avid manhwa reader who has extensively explored manhwas across all genres available online, please provide a brief synopsis of the selected manhwa: {manhwa_title}. 
        Additionally, recommend five manhwas that are similar to the chosen manhwa: {manhwa_title}. Use the following information about the user's preferences while recommending a manhwa.
        1. Favorite genre: {user_answers[0]}
        2. Action-packed/slow-paced: {user_answers[1]}
        3. Does the user prefer romance manhwa: {user_answers[2]}
        4. Themes enjoyed by the user: {user_answers[3]}
        For each recommended manhwa, explain why you consider it similar to the chosen manhwa. 
        Please add '---' before recommending the next manhwa.''',
    ]
    return prompt_parts

def recommend(manhwa_title, model, user_answers):
    human_prompt = prompt_with_answers(manhwa_title, user_answers)
    response = model.generate_content(human_prompt)
    return response.text

def main():
    st.title('📚 Manhwa Recommendation App')

    manhwa_title = st.text_input('Enter the manhwa title:')
    questions = [
        "What genre do you prefer?",
        "Do you like action-packed manhwas or more slow-paced ones?",
        "Do you like reading romance manhwas?",
        "Any specific themes or tropes you enjoy?"
    ]
    user_answers = []
    for question in questions:
        answer = st.text_input(question)
        user_answers.append(answer)

    if manhwa_title and all(user_answers):
        model = genai.GenerativeModel(model_name="gemini-pro")
        response = recommend(manhwa_title, model, user_answers)
        recommendations = response.split('---') 
        st.write("🌟 Recommendations and Why You'd Like Them")
        for i in recommendations:
            st.markdown(f"📌 {i}")
    elif manhwa_title or any(user_answers):
        st.warning("Please provide answers to all questions to get recommendations.")

if __name__ == '__main__':
    main()
