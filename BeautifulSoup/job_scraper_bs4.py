from bs4 import BeautifulSoup
import urllib.request
import csv
import os

# URL of the website to scrape
quote_page = "https://realpython.github.io/fake-jobs/"

# Open the webpage and create BeautifulSoup object
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, 'lxml')

try:
    # Extract job details using BeautifulSoup
    job_titles = [title.text for title in soup.find_all('h2', class_="title is-5")]
    companies = [company.text for company in soup.find_all('h3', class_="subtitle is-6 company")]
    locations = [location.text.strip() for location in soup.find_all('p', class_="location")]
    dates = [date.text.strip() for date in soup.find_all('time')]

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'index.csv')

    # Open the CSV file with append mode, so old data will not be erased
    with open(csv_path, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['Job Title', 'Company', 'Location', 'Date'])
        
        # If the file is empty, write the header
        if csv_file.tell() == 0:
            writer.writeheader()
        
        # Write each job as a separate row
        for title, company, location, date in zip(job_titles, companies, locations, dates):
            writer.writerow({'Job Title': title, 'Company': company, 'Location': location, 'Date': date})
            
    print("CSV file saved successfully.")

except Exception as e:
    print("An error occurred:", e)
