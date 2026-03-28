import streamlit as st
import requests

st.title("📄 AI Document Intelligence Agent")

# Upload section
st.header("Upload Document")

uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "csv", "xlsx"])

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
    
    response = requests.post("http://127.0.0.1:8000/upload/", files=files)
    
    if response.status_code == 200:
        st.success("Document uploaded successfully!")
    else:
        st.error("Upload failed")

# Query section
st.header("Ask a Question")

query = st.text_input("Enter your question")


if st.button("Get Answer"):
    if query:
        response = requests.get(
            "http://127.0.0.1:8000/query/",
            params={"q": query}
        )

        if response.status_code == 200:
            result = response.json()

            st.subheader("Answer")
            st.write(result["answer"])

            st.subheader("Validation")
            st.write(result["validation"])

            st.subheader("Sources")
            for s in result["sources"]:
                st.write("-", s[:200] + "...")
        else:
            st.error("Query failed")

st.markdown(
    "<p style='text-align: center; color: pink; font-weight: bold;'>Developed by Isha Sarangi | 2026</p>",
    unsafe_allow_html=True
)