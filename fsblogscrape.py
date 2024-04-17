import requests
from bs4 import BeautifulSoup
import sys

# Step 1: Define the base URL and the range of pages to scrape
base_url = 'https://fs.blog/blog/page/'
page_range = range(2, 11)

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
        sys.stdout.buffer.write((title.get_text() + '\n').encode('utf-8'))