import selenium.webdriver as webdriver
# from selenium.webdriver.chrome.service import Service
import time


def scrap_website(website):
    """
    This function grabs the content from a website using Selenium.
    """
    print("Launching Chrome browser...")

    # Set Chrome options
    options = webdriver.ChromeOptions()
    # options.add_argument("--disable-gpu")  # Prevent graphical errors
    # options.add_argument("--no-sandbox")   # Improve stability
    # options.add_argument("--headless")     # Run without GUI (optional)

    # Initialize ChromeDriver directly (since it's in PATH)
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(website)
        print("Page loaded successfully!")
        time.sleep(10)
        return driver.page_source  # Return page HTML

    finally:
        driver.quit()  # Ensure driver quits properly