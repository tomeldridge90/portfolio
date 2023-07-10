"""
This script is intended to scrape the Interface website to download
pictures of tiles along with some data about the images
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
import time
import re

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

    time.sleep(5)

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-event-click="confirm"]'))
        )
        element.click()
    except Exception as e:
        print(e)

access_main_page()

def get_type_link_list():
    """
    Collect all the links after loading the full product range
    """
    for i in range(10):
        element = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "a.b-button.m-white.m-has-icon.m-width_full")
                        )
                    )
        browser.execute_script("arguments[0].click();", element)
    time.sleep(5)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    links = soup.select('a.b-product_tile-link_wrapper:has(span.b-link-secondary.b-product_tile-link)')
    urls = [link.get('href') for link in links]

    return urls

def cycle_through_types(list_of_links: list):
    for link in list_of_links:
        try:
            browser.get(link)
        except Exception as e:
            print(f"Error accessing {link}: {e}")
        time.sleep(2)

        df = pd.DataFrame(collect_images_and_data(link))
        print(df)

def collect_images_and_data(html):

    response = requests.get(html)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')
    buttons = soup.find_all('button', {'class': 'b-variation_swatch m-swatch'})
    image_data = []

    collection_element = soup.find('a', {'class': 'b-link-secondary b-product_details-collection'})
    collection_name = collection_element.text.strip()

    for button in buttons:
        color_name = button.get('aria-label')
        color_value_element = button.find('span', {'class': 'b-variation_swatch-color_value'})
        style = color_value_element.get('style')

        # Extract URL from the style
        match = re.search(r"url\('(.+?)'\)", style)
        if match:
            url = match.group(1)
            image_data.append((color_name, url, collection_name))
    
    return image_data

 
cycle_through_types(get_type_link_list())



    

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
