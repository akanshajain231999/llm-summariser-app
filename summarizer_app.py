import streamlit as st
import requests
import json

# Streamlit UI setup
st.set_page_config(page_title="LLM Article Summarizer", layout="centered")
st.title("🧠 Article Summarizer with GPT")
st.write("Paste an article below to get an abstractive summary using OpenAI's GPT model.")

# User input
article = st.text_area("Paste your article here:", height=300)
temperature = st.slider("Creativity (temperature)", 0.0, 1.0, 0.7)
max_tokens = st.slider("Summary Length (max tokens)", 50, 500, 200)

# On "Summarize" button click
if st.button("Summarize"):
    if not article.strip():
        st.warning("Please paste an article first.")
    else:
        with st.spinner("Summarizing..."):
            try:
                # Prepare API request
                url = "https://api.openai.com/v1/chat/completions"
                headers = {
                    "Authorization": f"Bearer {st.secrets['OPENAI_API_KEY']}",
                    "Content-Type": "application/json"
                }
                data = {
                    "model": "gpt-3.5-turbo",
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant that summarizes articles."},
                        {"role": "user", "content": f"Summarize this article:\n\n{article}"}
                    ],
                    "temperature": temperature,
                    "max_tokens": max_tokens
                }

                # Make the POST request (with verify=False)
                response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)

                if response.status_code == 200:
                    summary = response.json()["choices"][0]["message"]["content"].strip()
                    st.subheader("📄 Summary:")
                    st.success(summary)
                else:
                    st.error(f"Failed to summarize. Status Code: {response.status_code}")
                    st.code(response.text)

            except Exception as e:
                st.error(f"An error occurred: {e}")
