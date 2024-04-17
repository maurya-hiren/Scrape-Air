import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
from bs4 import BeautifulSoup
import json
import os

import random
import combogen


json_save_dir = "./Json"

os.makedirs(json_save_dir, exist_ok=True)

def generate_unique_numbers():
    return random.randint(1000, 9999)


def open_browser(url):
    # Setup Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Initialize the driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # Open the specified URL
    driver.get(url)
    # if combo[k] or combo[k+midpoint]:
    #     print(combo[k] if combo[k] else combo[k+midpoint])
    # else:
    #     print("Url Problem...........")
    # print()
    time.sleep(12)
    start_time = time.time()
    
    while time.time() - start_time < 10:
        driver.execute_script("window.scrollBy(0, 1000)")
        time.sleep(1)
        
    flight_Details = driver.find_elements("css selector","a.dF.alignItemsCenter.curPointFlt.alignItemsCenter.fr")
    for element in flight_Details:
        element.click()
    time.sleep(5)
    
    element_soup = driver.find_element("css selector", ".seo-srp-layoutstyles__RightWrap-sc-11ypfer-3")
    element_html = element_soup.get_attribute('outerHTML')
    soup = BeautifulSoup(element_html, 'html.parser')
    # print(soup)
    flight_cards = soup.find_all("div", class_="srp-card-uistyles__SeoCard-sc-3flq99-4")

    flights_data_with_tagline = []

    for index, card in enumerate(flight_cards, start=1):
        
        flight_info = {
            "Division": f"Element division {index}",
            "Type of Flight": card.find("span", class_="font14 padL5").text.strip(),
            "Start (Departure)": " ".join(span.text for span in card.find("div", class_="greyCntLt").find_all("span")),
            "Departure timing": card.find("span", class_="srp-card-uistyles__Time-sc-3flq99-15").text.strip(),
            "Total timing (Duration)": card.find("span", class_="srp-card-uistyles__DurTime-sc-3flq99-16").text.strip(),
            "End (Arrival)": " ".join(span.text for span in card.find_all("div", class_="greyCntLt")[-1].find_all("span")),
            "End-Time": card.find_all("span", class_="srp-card-uistyles__Time-sc-3flq99-15")[-1].text.strip(),
            "Price": card.find("div", class_="srp-card-uistyles__Price-sc-3flq99-17").text.strip(),
            "Flight Unique Number": card.find("span", class_="db greyCnt").text.strip() 
        }
    
        layover_info = card.find("div", class_="greyCnt")
        flight_info["Layover"] = layover_info.text.strip() if layover_info else "No layover"

        flights_data_with_tagline.append(flight_info)

    json_data_with_tagline = json.dumps(flights_data_with_tagline, indent=4)
    print("Date :- "+date)
    print(url)
    print(json_data_with_tagline)
    
    unique_numbers = generate_unique_numbers()
    
    filename = f"{json_save_dir}/flight_data_{date}_id_{unique_numbers}.json"
    with open(filename, 'w') as file:
        json.dump(flights_data_with_tagline, file, indent=4)
    
    print(f"Saved data to {filename}")
   
   
   
    driver.quit()

extract_duration = 60; # Days
Airport_Codes = ["DEL", "BOM", "BLR", "HYD", "MAA", "CCU", "AMD", "COK", "GOI", "PNQ"]

combo = combogen.generate_combinations(Airport_Codes)
# print(combo[0])
combo_len = len(combo)
print(f"Total number of combinations: {(combo_len)}")
run_script = str(combo_len*extract_duration)
print(f"Script will run {run_script} times")

midpoint = len(combo) // 2

for k in range(combo_len):

    for i in range(1,extract_duration):
        date = str(i)
        print(combo[k])
        print(combo[k+midpoint])
        url1 = "https://www.goibibo.com/flights/air-"+combo[k]+"-2024030"+date+"--1-0-0-E-D?"
        url2 = "https://www.goibibo.com/flights/air-"+combo[k+midpoint]+"-2024030"+date+"--1-0-0-E-D?"
        
        thread1 = threading.Thread(target=open_browser, args=(url1,))
        thread2 = threading.Thread(target=open_browser, args=(url2,))
        thread1.start()
        thread2.start()
        
        thread1.join()
        thread2.join()