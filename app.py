import streamlit as st
import requests

st.title('Telc A2 B1 Writing Task evaluator')
st.write('This app evaluates question 31 of the Telc A2-B1 exam. Evaluate your text and get a score. Also recommended corrections will be shown.')

def word_count(text):
    return len(text.split())

user_input = st.text_area('Enter letter here (max 100 words):', height=250)

if st.button('Submit'):
    if word_count(user_input) <= 100:

        response = requests.post('http://localhost:8000/score', json={'query': user_input})
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            st.markdown(data['response']['response'],  unsafe_allow_html=True)
        else:
            st.error(f'Unexpected status code received: {response.status_code}')

    else:
        st.warning('Please enter a paragraph with no more than 100 words.')
