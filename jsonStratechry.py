import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://stratechery.com/category/articles/page/'
page_range = range(2, 54)

all_articles = []

# Step 2: Loop through the page range and scrape each page
for page_num in page_range:
    # Construct the URL for the current page
    url = base_url + str(page_num) + '/'
    
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using `BeautifulSoup`
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the article elements
    articles = soup.find_all('article')

    # Extract the data you want for each article
    for article in articles:
        title_tag = article.find('h1').get_text()
        title_link = article.find('h1').find('a').get('href')
        
        # Extract posted on and updated on information
        posted_on_tag = article.find('span', class_='posted-on')
        date_tag = posted_on_tag.find('time', class_='published').get_text()
        updated_tag = posted_on_tag.find('time', class_='updated')
        updated_date = updated_tag.get_text() if updated_tag else None
        
        time_tag = article.find('span').find('span').get_text()
        p_tag = article.find('p').get_text()

        article_data = {
            'Title': title_tag,
            'Title Link': title_link,
            'Date': date_tag,
            'Updated Date': updated_date,
            # 'Time': time_tag,
            'Content': p_tag,
            'Page': page_num  # Add the 'Page' information
        }

        all_articles.append(article_data)

# Convert the list of dictionaries to a JSON object
json_data = json.dumps(all_articles, indent=2)

# Print or save the pretty-printed JSON
print(json_data)

# If you want to save it to a file
with open('scraped_data_stratechery.json', 'w') as json_file:
    json_file.write(json_data)
