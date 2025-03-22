import streamlit as st
from scrape import scrap_website

# add title to the page
st.title("AI Web Scraper")
url = st.text_input('Enter a website URL:') # input text box for entering the website


# to run the streamlit app use: 'streamlit run main.py' in the terminal

if st.button('Scrape Site'):
    st.write('Scraping the website')
    result = scrap_website(url) # call the scrap_website function and store the result
    print(result)
