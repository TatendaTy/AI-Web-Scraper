import streamlit as st
from scrape import (scrap_website, split_dom_content, clean_body_content, extract_body_content)
from content_parsing import parse_with_Ollama

# add title to the page
st.title("AI Web Scraper")
url = st.text_input('Enter a website URL:') # input text box for entering the website


# to run the streamlit app use: 'streamlit run main.py' in the terminal

if st.button('Scrape Site'):
    st.write('Scraping the website')
    
    result = scrap_website(url) # call the scrap_website function and store the result
    body_content = extract_body_content(result) # extract the body content from the result
    cleaned_content = clean_body_content(body_content) # clean the body content using the clean_body_content function

    # store the content in session for streamlit
    st.session_state.dom_content = cleaned_content # store the cleaned content in session state for easy access in other parts of the app
    
    # expander textbox that allows us to expand it to view more content
    with st.expander('View DOM Content'): # toggle button for viewing the DOM content
        st.text_area("DOM Content", cleaned_content, height=300) # write the content in a text area for viewing


# parsing content with Ollama
# take the DOM Content and user prompt and pass it to the LLM that will parse it based on what is to be achieved
# Ask user for a prompt to ask the LLM the specific information they want from the site

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what to parse?")

    if st.button('Parse Content'):
        # pass the cleaned content and user prompt to the Ollama model
        if parse_description:
            st.write('Parsing content...')
            dom_chunks = split_dom_content(st.session_state.dom_content) # parse the DOM content
            result = parse_with_Ollama(dom_chunks, parse_description) # pass the cleaned content and user prompt to the Ollama model
            st.write(result)  # display the parsed result
        else:
            st.warning('Please provide a description of what you want to extract from the text.')  # warning if no description is provided

            





