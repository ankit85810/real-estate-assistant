import streamlit as st
from rag import process_urls, generate_answer

st.title("Real Estate Assistant")

url1 = st.sidebar.text_input("URL 1")
url2 = st.sidebar.text_input("URL 2")
url3 = st.sidebar.text_input("URL 3")

placeholder = st.empty()

process_url_button = st.sidebar.button("Process URLs")
if process_url_button:

    urls = [url for url in (url1, url2, url3) if url != ''] 
    if len(urls) == 0:
        st.sidebar.error("Please enter at least one URL.")

    else:
        with placeholder.container():
            st.info("Processing URLs. This may take a few minutes...")
            for status in process_urls(urls):
                st.write(status)
            st.success("Processing complete! You can now ask questions about the documents.")

query = st.text_input("Enter your question about the documents:")
if query:
    with placeholder.container():
        st.info("Generating answer...")
        try:
            answer, sources = generate_answer(query)
            st.markdown("**Answer:**")
            st.write(answer)
            st.markdown("**Sources:**")
            st.write(sources)
        except RuntimeError as e:
            st.error("You need to process URLs before asking questions.")