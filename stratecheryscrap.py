import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://stratechery.com/category/articles/page/'
page_range = range(2, 11)

all_titles = []

# Step 2: Loop through the page range and scrape each page
for page_num in page_range:
    # Construct the URL for the current page
    url = base_url + str(page_num) + '/'
    
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using `BeautifulSoup`
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the data you want
    # For example, find all the article titles
    titles = soup.find_all('article')
    for title in titles:
        all_titles.append(title.get_text())

# Create a DataFrame from the scraped data
df = pd.DataFrame({'Title': all_titles})

# Save the DataFrame to an Excel file
df.to_excel('scraped_data_stratechery.xlsx', index=False)