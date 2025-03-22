import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrap_website(website):
    '''
    this function allows us to grab the content from a website using selenium
    '''
    print('Launching chrome browser')

    chrome_driver_path = '/mnt/c/webdrivers/chromedriver.exe'  #specify where chrome-driver is
    options = webdriver.ChromeOptions() # specify the options of how the chrome driver should work i.e ignoring images or running it headless
    # options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
    # options.add_argument('--disable-gpu')  # Disable GPU to avoid graphical errors
    # options.add_argument('--no-sandbox')  # Allow Chrome to run without sandbox for better compatibility
    
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options) # set up driver #any browser you want
    # driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    
    try:
        driver.get(website) # uses the webdriver to go to the specific website mentioned
        print('page loaded')
        html = driver.page_source # get the HTML from the site
        time.sleep(10)
        return html

    finally:
        driver.quit()
