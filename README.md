# AI Web Scraper

AI Web Scraper is a Streamlit-based application that allows users to scrape website content, clean and process the data, and extract specific information using an LLM (Large Language Model) via Ollama.

## Features

- **Web Scraping:** Uses Selenium and Bright Data proxy to scrape website content, including handling CAPTCHAs.
- **Content Cleaning:** Cleans and extracts the main body content from HTML using BeautifulSoup.
- **Chunking:** Splits large content into manageable chunks for LLM processing.
- **AI-Powered Parsing:** Uses an Ollama LLM to extract user-specified information from the scraped content.
- **Interactive UI:** Built with Streamlit for easy user interaction.

## Installation

1. **Clone the repository:**

   ```sh
   git clone <repository-url>
   cd AI-Web-Scraper
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file if needed for your proxy or LLM credentials.

## Usage

1. **Run the Streamlit app:**

   ```sh
   streamlit run main.py
   ```

2. **In the web UI:**
   - Enter the URL of the website you want to scrape.
   - Click "Scrape Site" to fetch and clean the content.
   - Enter a description of what information you want to extract.
   - Click "Parse Content" to extract the specified information using the LLM.

## Project Structure

```
AI-Web-Scraper/
│
├── main.py                # Streamlit app entry point
├── scrape.py              # Web scraping and content cleaning logic
├── content_parsing.py     # LLM-based content parsing logic
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md
```

## Requirements

- Python 3.8+
- Chrome browser (for Selenium)
- [Bright Data](https://brightdata.com/) proxy credentials (for advanced scraping)
- Ollama LLM and model access

## Notes

- This project is for educational and research purposes. Always respect website terms of service and robots.txt.
- For best results, ensure your proxy and LLM credentials are set up correctly.
