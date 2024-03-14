import streamlit as st
import google.generativeai as genai
import random

genai.configure(api_key='AIzaSyDlBFVsmV8pao6Ax-bcR0dc5h4CusiNCsc')  

def prompt_with_answers(manhwa_title, user_answers):
    prompt_parts = [
        f'''As an avid manhwa reader who has extensively explored manhwas across all genres available online, please provide a brief synopsis of the selected manhwa: {manhwa_title}. 
        Additionally, recommend five manhwas that the user might like based on user's preferences.
        Preferences:
        -Favourite manhwa:{manhwa_title}
        -Favorite genre: {user_answers[0]}
        - Action-packed/slow-paced: {user_answers[1]}
        -Does the user prefer romance manhwa: {user_answers[2]}
        -Themes enjoyed by the user: {user_answers[3]}
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

    manhwa_title = st.text_input("What's the title of the manhwa that's your absolute favorite?")
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
        with st.expander(f"Synopsis"):
            st.markdown(f"📌 {recommendations[0]}")
        recommendations.pop(0)
        st.write("🌟 Recommendations and Why You'd Like Them")
        for idx, rec in enumerate(recommendations, start=1):
            with st.expander(f"Recommendation {idx}"):
                st.markdown(f"📌 {rec}")
                
    elif manhwa_title or any(user_answers):
        st.warning("Please provide answers to all questions to get recommendations.")

if __name__ == '__main__':
    main()
