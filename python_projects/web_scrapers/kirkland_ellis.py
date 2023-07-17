import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
 
urls = [
    'https://www.kirkland.com/lawyers?office=2ef6b233-eaab-45eb-b2a8-7115bbe6a5f4',
    'https://www.kirkland.com/lawyers?office=2b2425d0-bbaa-4fc2-ad3c-a4e60caa81e8',
    'https://www.kirkland.com/lawyers?office=180be944-e48a-41b0-ad42-94487adeef06'
]

df = pd.DataFrame()

for url in urls:

    driver.get(url)

    # Scroll to the bottom of the page
    SCROLL_PAUSE_TIME = 1.5  # You might need to adjust this time
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)  # Wait to load the page
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    data = []
    divs = driver.find_elements(By.CSS_SELECTOR, "div.person-result.person-result_transition-in")
    
    for div in divs:
        name = div.find_element(By.CSS_SELECTOR, "h3.person-result__name").text
        level = div.find_element(By.CSS_SELECTOR, "div.person-result__level").text
        email = div.find_element(By.CSS_SELECTOR, "a.person-result__email").text
        offices = div.find_elements(By.CSS_SELECTOR, "div.person-result__office")
        if offices:
            if len(offices) > 1:
                office1 = offices[0].find_element(By.CSS_SELECTOR, "h4.person-result__office-title").text
                phone1 = offices[0].find_element(By.CSS_SELECTOR, "a.person-result__title").text
                office2 = offices[1].find_element(By.CSS_SELECTOR, "h4.person-result__office-title").text
                phone2 = offices[1].find_element(By.CSS_SELECTOR, "a.person-result__title").text
            else:
                office1 = offices[0].find_element(By.CSS_SELECTOR, "h4.person-result__office-title").text
                phone1 = offices[0].find_element(By.CSS_SELECTOR, "a.person-result__title").text
                office2 = None
                phone2 = None
        else:
            office1 = None
            phone1 = None
            office2 = None
            phone2 = None

        data.append({'Name': name, 'Level': level, 'Email': email, 'Office1': office1,
                      'Phone1': phone1, 'Office2': office2, 'Phone2': phone2})

    df_new = pd.DataFrame(data)
    df = pd.concat([df, df_new], ignore_index=True)
    
driver.quit()
print(df)
df.to_csv('/home/tome/portfolio/test_data/candidates_output.csv')


