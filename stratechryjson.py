import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://stratechery.com/category/articles/page/'
page_range = range(2, 54)

all_articles = []

for page_num in page_range:
   
    url = base_url + str(page_num) + '/'
    
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article')

    for article in articles:
        title_tag = article.find('h1').get_text()
        title_link = article.find('h1').find('a').get('href')
        
        posted_on_tag = article.find('span', class_='posted-on')
        date_tag = posted_on_tag.find('time', class_='published').get_text()
        updated_tag = posted_on_tag.find('time', class_='updated')
        updated_date = updated_tag.get_text() if updated_tag else None
        
        time_tag = article.find('span').find('span').get_text()
        p_tag = article.find('p').get_text()

        specific_page_response = requests.get(title_link)
        specific_page_soup = BeautifulSoup(specific_page_response.content, 'html.parser')
        specific_page_content = specific_page_soup.find('div', class_='entry-content').get_text() if specific_page_soup else None

        article_data = {
            'Title': title_tag,
            'Title Link': title_link,
            'Date': date_tag,
            'Updated Date': updated_date,
            'Time': time_tag,
            'Content': p_tag,
            'Specific Page Content': specific_page_content,
            'Page': page_num  
        }

        all_articles.append(article_data)

json_data = json.dumps(all_articles, indent=2)

print(json_data)

with open('stratechery_data.json', 'w') as json_file:
    json_file.write(json_data)