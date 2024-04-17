from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up ChromeOptions to run in headless mode
chrome_options = Options()
# chrome_options.add_argument("--headless")

# Initialize the Chrome driver with the ChromeOptions
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the desired website
driver.get("https://www.example.com")

# Print the page title
print(driver.title)

# Close the browser
driver.quit()