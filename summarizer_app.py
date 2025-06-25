import streamlit as st
import requests
import json
import fitz  # PyMuPDF for PDF reading


# Streamlit UI setup
st.set_page_config(page_title="LLM Article Summarizer", layout="centered")
st.title("🧠 Article Summarizer with GPT")
st.write("Upload a file or paste an article below to get an abstractive summary using OpenAI's GPT model.")

# Upload file
uploaded_file = st.file_uploader("Upload a .txt or .pdf file", type=["txt", "pdf"])

# Optional: fallback text input
article = ""
if uploaded_file:
    try:
        if uploaded_file.type == "text/plain":
            article = uploaded_file.read().decode("utf-8")
        elif uploaded_file.type == "application/pdf":
            pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            article = "\n\n".join([page.get_text() for page in pdf])
    except Exception as e:
        st.error(f"Could not read the file: {e}")
else:
    article = st.text_area("Or paste your article here:", height=300)

# Parameters
temperature = st.slider("Creativity (temperature)", 0.0, 1.0, 0.7)
max_tokens = st.slider("Summary Length (max tokens)", 50, 500, 200)

# Summarize
if st.button("Summarize"):
    if not article.strip():
        st.warning("Please upload or paste an article first.")
    else:
        with st.spinner("Summarizing..."):
            try:
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
