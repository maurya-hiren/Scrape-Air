import requests
from bs4 import BeautifulSoup

url = 'https://www.makemytrip.com/flight/search?itinerary=DEL-BOM-07/02/2024&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng&cmp=SEM|D|DF|G|Generic|Generic-Generic_DT|DF_Generic_Exact|RSA|Offer3|673438880765'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.content, 'html.parser')

links = []
for div in soup.find_all('srp-card-uistyles__SeoCard-sc-3flq99-4'):
    links.append(div)
print(links)