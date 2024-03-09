    job_titles = [title.text.strip() for title in soup.find_all('h2', class_='jobTitle')]
    companies = [company.text.strip() for company in soup.find_all('span', class_='companyName')]
    locations = [location.text.strip() for location in soup.find_all('div', class_="companyLocation")]
    dates = [date.text.strip() for date in soup.find_all('span', class_="datePosted")]
