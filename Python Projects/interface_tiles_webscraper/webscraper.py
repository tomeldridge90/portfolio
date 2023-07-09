"""
This script is intended to scrape the Interface website to download
pictures of tiles along with some data abuot the images
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium import webdriver

browser = webdriver.Firefox()

def access_main_page():
    """
    Launch the browser and navigate through the cookie and location popups
    """
    browser.get('https://shop.interface.com/AU/en-AU/carpet-tile/')

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-event-click="accept"]'))
        )
        element.click()
    except Exception as e:
        print(e)

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-event-click="confirm"]'))
        )
        element.click()
    except Exception as e:
        print(e)

access_main_page()

def get_type_link_list():

    for i in range(10):
        element = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "a.b-button.m-white.m-has-icon.m-width_full")
                        )
                    )
        browser.execute_script("arguments[0].click();", element)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    links = soup.select('a.b-product_tile-link_wrapper:has(span.b-link-secondary.b-product_tile-link)')
    urls = [link.get('href') for link in links]
    for url in urls:
        print(url)

get_type_link_list()

def cycle_through_types(list_of_links: list):
    pass

"""

def download_image(image_url, target_path):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(target_path, 'wb') as f:
            f.write(response.content)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://shop.interface.com/AU/en-AU/carpet-tile/'
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup)

# Empty DataFrame to store results
results = pd.DataFrame(columns=['name', 'color', 'image_path'])
results.show()



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

"""
