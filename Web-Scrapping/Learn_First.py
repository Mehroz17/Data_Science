# Import required libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up Chrome driver
options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path=r"C:\Users\dell\Downloads\chromedriver.exe" , options=options)
url = 'https://www.backmarket.co.uk/en-gb/p/macbook-air-133-inch-2017-core-i5-8gb-ssd-256-gb-qwerty-english-uk/0ec68246-00a3-4924-945a-77b9a28dad02#l=12'
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Extract the HTML content of the page
html = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the elements and extract the required data
product_name = soup.select_one('h1.product-page__title').text.strip()
price = soup.select_one('div.product-page__price > span.value').text.strip()
condition = soup.select_one('span.product-page__tag').text.strip()
specs_list = soup.select('div.product-page__tech-specs > ul > li')
specs = {}
for spec in specs_list:
    key = spec.select_one('div.key').text.strip()
    value = spec.select_one('div.value').text.strip()
    specs[key] = value

# Print the extracted data
print('Product Name:', product_name)
print('Price:', price)
print('Condition:', condition)
print('Specifications:')
for key, value in specs.items():
    print(key, ':', value)

# Close the driver
driver.quit()
