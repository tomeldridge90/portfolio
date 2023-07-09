"""
This script is intended to scrape the Interface website to download
pictures of tiles along with some data abuot the images
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

def download_image(image_url, target_path):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(target_path, 'wb') as f:
            f.write(response.content)

# Instantiate a browser
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://shop.interface.com/AU/en-AU/carpet-tile/'
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

# Empty DataFrame to store results
results = pd.DataFrame(columns=['name', 'color', 'image_path'])

# Find product elements and iterate over them
products = soup.find_all('div', class_='product-tile')
for product in products:
    name = product.find('div', class_='product-name').text
    color = product.find('div', class_='product-color').text
    image_url = product.find('img')['src']
    image_path = os.path.join('/path/to/save/images', f'{name}_{color}.jpg')
    download_image(image_url, image_path)
    results = results.append({'name': name, 'color': color, 'image_path': image_path}, ignore_index=True)

# Save DataFrame to CSV
results.to_csv('results.csv', index=False)

# Close the browser
driver.quit()

