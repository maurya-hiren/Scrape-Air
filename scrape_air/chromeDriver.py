from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from bs4 import BeautifulSoup
import json

sys.stdout.reconfigure(encoding='utf-8')

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.goibibo.com/flights/air-BOM-DEL-20240206--1-0-0-E-D?")
time.sleep(12)

start_time = time.time()

while time.time() - start_time < 10:
    driver.execute_script("window.scrollBy(0, 1000)")
    time.sleep(1)
    

flight_Details = driver.find_elements("css selector","a.dF.alignItemsCenter.curPointFlt.alignItemsCenter.fr")


for element in flight_Details:
    element.click()


elements = driver.find_elements("css selector", ".srp-card-uistyles__SeoCard-sc-3flq99-4.cPIUAK")

html_contents = [element.get_attribute('outerHTML') for element in elements]

print("\n ---------------------- Elements ----------------------\n".join(html_contents))



element_count = len(elements)

print("The total number of div elements with the specified class is:", element_count)



#! Type of Flight :- font14 padL5
#! Place of AIRPORT :- greyCntLt <span> ,
#! Departure timing :- srp-card-uistyles__Time-sc-3flq99-15 iHpsco padT10 f600
#!  if exist := Layover :- greyCnt  
#! greyCntLt
#! End-Time :- srp-card-uistyles__Time-sc-3flq99-15 iHpsco f500  padT10
#! Price :- srp-card-uistyles__Price-sc-3flq99-17 kxwFaC alignItemsCenter dF f600


#? If = mid_station - srp-card-uistyles__Lcity-sc-3flq99-19 kkhkOs txtUpper
#? if<mid_station> = time - srp-card-uistyles__DurTime-sc-3flq99-16 cSxcBC f500 padT10



element_soup = driver.find_element("css selector", ".seo-srp-layoutstyles__RightWrap-sc-11ypfer-3.gFaPPt")


element_html = element_soup.get_attribute('outerHTML')  
soup = BeautifulSoup(element_html, 'html.parser')

flight_cards = soup.find_all("div", class_="srp-card-uistyles__CardWrap-sc-3flq99-7")

flights_data_with_tagline = []

for index, card in enumerate(flight_cards, start=1):

    flight_info = {
        "Division": f"Element division {index}",
        "Type of Flight": card.find("span", class_="font14 padL5").text.strip(),
        "Place of AIRPORT": card.find("div", class_="greyCntLt").text.strip(),
        "Departure timing": card.find("span", class_="srp-card-uistyles__Time-sc-3flq99-15").text.strip(),
        "End-Time": card.find_all("span", class_="srp-card-uistyles__Time-sc-3flq99-15")[-1].text.strip(),
        "Price": card.find("div", class_="srp-card-uistyles__Price-sc-3flq99-17").text.strip()
    }
    
    layover_info = card.find("div", class_="greyCnt")
    flight_info["Layover"] = layover_info.text.strip() if layover_info else "No layover"

    flights_data_with_tagline.append(flight_info)

json_data_with_tagline = json.dumps(flights_data_with_tagline, indent=4)

print(json_data_with_tagline)
time.sleep(100)
driver.quit()

