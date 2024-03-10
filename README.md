# Job Scraper

This repository contains Python scripts for scraping job data from a fake job website and saving it into a CSV file.

## Requirements

- Python 3.x
- BeautifulSoup4 library (`pip install beautifulsoup4`)

## Usage

1. Clone the repository or download the scripts.
2. Ensure you have the required libraries installed.
3. Run the script by executing `python job_scraper.py`.
4. The script will scrape job data from [Real Python Fake Jobs](https://realpython.github.io/fake-jobs/) and save it into a file named `index.csv`.

## Project Structure

The project directory contains the following files:

- **BeautifulSoup**: This directory contains the script `job_scraper_bs4.py`, which utilizes BeautifulSoup for web scraping.
- **Selenium**: This directory contains the script `job_scraper_selenium.py`, which utilizes Selenium WebDriver for web scraping.

## Script Details

### BeautifulSoup Version

- This Python script (version 1) scrapes job data from a website using BeautifulSoup and saves it into a CSV file.
- It fetches job titles, company names, locations, and dates from the webpage.
- Data is stored in a CSV file with headers: 'Job Title', 'Company', 'Location', and 'Date'.
- If the CSV file is empty, the script adds a header row before writing job data.

### Selenium Version

- This Python script (version 2) scrapes job data from a website using Selenium WebDriver and saves it into a CSV file.
- It fetches job titles, company names, locations, and dates from the webpage.
- Data is stored in a CSV file with headers: 'Job Title', 'Company', 'Location', and 'Date'.
- If the CSV file is empty, the script adds a header row before writing job data.

## Fake Job Website

The scripts scrape job data from [Real Python Fake Jobs](https://realpython.github.io/fake-jobs/), a website that hosts fake job listings for demonstration purposes.
