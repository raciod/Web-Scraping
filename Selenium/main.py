from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
import csv
from selenium.webdriver.common.by import By
import os

url = "https://realpython.github.io/fake-jobs/"

# Set up Firefox WebDriver
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Open the webpage
driver.get(url)
time.sleep(10)  

try:
    # Find elements using Selenium
    job_titles = [title.text for title in driver.find_elements(By.CSS_SELECTOR, 'h2.title.is-5')]
    companies = [company.text for company in driver.find_elements(By.CSS_SELECTOR, 'h3.subtitle.is-6.company')]
    locations = [location.text.strip() for location in driver.find_elements(By.CSS_SELECTOR, 'p.location')]
    dates = [date.text.strip() for date in driver.find_elements(By.CSS_SELECTOR, 'time')]

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'index_selenium.csv')

    # Write data to a CSV file
    with open(csv_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['Job Title', 'Company', 'Location', 'Date'])
        writer.writeheader()
        for title, company, location, date in zip(job_titles, companies, locations, dates):
            writer.writerow({'Job Title': title, 'Company': company, 'Location': location, 'Date': date})

    print("CSV file saved successfully.")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()
