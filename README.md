# Job Scraper (Version 1)

This Python script (version 1) scrapes job data from a website and saves it into a CSV file.

## Requirements

- Python 3.x
- BeautifulSoup4 library (`pip install beautifulsoup4`)

## Usage

1. Clone the repository or download the script.
2. Ensure you have the required libraries installed.
3. Run the script by executing `python job_scraper.py`.
4. The script will scrape job data from [Real Python Fake Jobs](https://realpython.github.io/fake-jobs/) and save it into a file named `index.csv`.

## Script Details

- The script utilizes BeautifulSoup for parsing HTML content.
- It fetches job titles, company names, locations, and dates from the webpage.
- Data is stored in a CSV file with headers: 'Job Title', 'Company', 'Location', and 'Date'.
- If the CSV file is empty, the script adds a header row before writing job data.
