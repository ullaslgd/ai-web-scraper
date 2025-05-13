import streamlit as st
from scrape import web_scraper, scrape_body, clean_body, split_dom_content
from parse import parse_with_ollama

st.set_page_config(page_title="AI Web Scraper", page_icon=":mag_right:")

st.title("AI Web Scraper")
st.write(
    "This app allows you to scrape data from any website and parse it using AI. "
    "Simply enter the URL of the website you want to scrape, and the app will handle the rest."
)
url = st.text_input("Enter the URL of the website you want to scrape")

if st.button("Scrape"):
    st.write(f"Scraping data from {url}...")
    result = web_scraper(url)
    if result:
        st.write("Data scraped successfully!")
        body_content = scrape_body(result)
        cleaned_content = clean_body(body_content)

        st.session_state.dom_content = cleaned_content

        with st.expander("View DOM content"):
            st.text_area("DOM Content", cleaned_content, height=400) 

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse"):
        if parse_description:

            dom_chunks = split_dom_content(st.session_state.dom_content) 
            results = parse_with_ollama(dom_chunks, parse_description)
            st.write("Parsing completed!")
            st.write(results)
   
