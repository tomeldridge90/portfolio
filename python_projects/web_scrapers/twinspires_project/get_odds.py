from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)


retry_count = 3

for i in range(retry_count):
    try:
        driver.get('https://www.twinspires.com/bet/program/classic/uk-gh-perry-barr/pr1/Greyhound/5/advanced')

        time.sleep(3)

        # use explicit wait
        wait = WebDriverWait(driver, 10)

        entry_container = driver.find_element(By.CLASS_NAME, 'entry-container')

        runners = entry_container.find_elements(By.TAG_NAME, 'cdux-program-entry')

        runner_data = []

        for runner in runners:
            horse_name_element = runner.find_element(By.CLASS_NAME, 'entry-runner-name')       
            horse_name = horse_name_element.get_attribute('innerHTML').split('<!---->')[0].strip()
            # Locate the odds element
            odds_element = runner.find_element(By.CLASS_NAME, 'odds-main-detail')
            odds_html = odds_element.get_attribute('innerHTML').strip()
            soup = BeautifulSoup(odds_html, 'html.parser')

            # Extract the odds text
            odds = soup.get_text().strip()

            # Locate the trainer element
            trainer_element = runner.find_element(By.CLASS_NAME, 'entry-trainer-name')

            # Extract the trainer text
            trainer = trainer_element.get_attribute('innerHTML').strip()

            # Print the runner details
            print("Runner: ", horse_name)
            print("Odds: ", odds)
            print("Trainer: ", trainer)
            print()

        driver.quit()

        # if no exception is thrown, break the loop
        break

    except TimeoutException:
        print(f"TimeoutException caught, retrying ({i+1}/{retry_count})")
        continue

