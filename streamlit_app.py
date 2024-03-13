import streamlit as st

# Define a dictionary of manhwas with genres
manhwas = {
    'Action': ['Solo Leveling', 'Tower of God', 'The Breaker'],
    'Romance': ['True Beauty', 'The Secret of Angel', 'Love Alarm'],
    'Fantasy': ['Noblesse', 'Black Haze', 'The Gamer']
}

# Define function to recommend manhwas based on selected genres
def recommend_manhwas(selected_genres):
    recommended_manhwas = []
    for genre in selected_genres:
        recommended_manhwas.extend(manhwas.get(genre, []))
    return recommended_manhwas

# Streamlit UI
st.title('Manhwa Recommendation App')

# Genre selection
selected_genres = st.multiselect('Select genres', list(manhwas.keys()))

if selected_genres:
    # Recommend manhwas
    recommended_manhwas = recommend_manhwas(selected_genres)
    
    # Display recommendations
    st.subheader('Recommended Manhwas:')
    for manhwa in recommended_manhwas:
        st.write('- ' + manhwa)
else:
    st.write('Please select at least one genre.')

