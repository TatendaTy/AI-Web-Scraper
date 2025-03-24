import os
from dotenv import load_dotenv
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

# Retrieve the WebDriver endpoint securely
SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")

# use brightdata for webscraping
def scrap_website(website):
    """_summary_
    This function launches a Chrome browser and navigates to the specified website. It then waits for a captcha solver to finish and returns the page HTML content.

    Args:
        website: The URL of the website to scrape.

    Returns:
        html: The HTML content of the website.

    """    
    print("Launching Chrome browser...")

    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome') # sbr connection 
    with Remote(sbr_connection, options=ChromeOptions()) as driver: # connect to sbr as driver
        driver.get(website)
        # CAPTCHA handling code goes here
        print('Waiting captcha to solve...')
        solve_res = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10000},
        }) # Wait for captcha solver to finish and get status
        print('Captcha solve status:', solve_res['value']['status']) # 
        print('Navigated! Scraping page content') # 
        html = driver.page_source  # assign page source to html variable
        
        return html  # Return page HTML


# task 2: clean the DOM Content
def extract_body_content(html_content):
    """
    This function takes the HTML content of a website and extracts the body content. It uses BeautifulSoup to parse the HTML and extract the body content.

    Args:
        html_content: The HTML content of the website returned from the `scrap_website` function.

    Returns:
        str: The extracted body content of the website. 
    """    
    soup = BeautifulSoup(html_content, "html.parser") # parse HTML content using BeautifulSoup
    body_content = soup.body # extract body content from parsed HTML
    if body_content:
        return str(body_content)  # Return cleaned body content as a string
    return "" # Return empty string if no body content found

def clean_body_content(body_content):
    """_summary_
    This function takes the HTML content of a website and cleans it by removing unwanted elements such as script and style tags. 
    It also converts the cleaned HTML content to a string with newline characters as separators, 
    removes empty lines and strip leading/trailing whitespace from each line in the cleaned content if no newline characters are present. 

    Args:
        body_content: the body content of the website returned from the `extract_body_content` function. 

    Returns:
        cleaned_content: the cleaned body content of the website
    """    
    soup = BeautifulSoup(body_content, "html.parser") # parse HTML content using BeautifulSoup

    # loop through the parsed content and remove unwanted elements such as script and style tags
    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()  # remove script and style tags from the parsed HTML

    cleaned_content = soup.get_text(separator="\n") # convert cleaned HTML content to a string with newline characters as separators
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip()) # remove empty lines and strip leading/trailing whitespace from each line in the cleaned content if no newline characters are present

    return cleaned_content  # Return cleaned body content as a string


    
# task 3: Split the content into batches to limit the token length based on what the model can handle
# and the feed those characters into the LLM one batch at a time for easy processing
# 
def split_dom_content(dom_content, max_length=6000):
    """_summary_
    This function takes the cleaned body content of a website and splits it into chunks of size `max_length`. 
    It returns a list of chunks where each chunk is a string of length `max_length` or less. 

    Args:
        dom_content (_type_): the cleaned body content of a website
        max_length (int, optional): the maximum length of each chunk. Default set to 6000.

    Returns:
        list: a list of chunks where each chunk is a string of length `max_length` or less. 
    """    
    # split the body content into chunks of size max_length
    # first create batches of 6000 characters from index i to i+max_length 
    # the for loop steps by the max length up to the dom_content length and repeats until all characters are split into batches
    return [ dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length) ] # 





















