from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# Set up a Selenium browser instance
browser = webdriver.Firefox()  # You can also use Chrome()

# Load the webpage
browser.get('https://www.twinspires.com/bet/todays-races/time')

# Wait for the page to fully load
browser.implicitly_wait(10)

# Initialize URLs list
urls = []

# Initialize the index
index = 1

# Start an infinite loop
while True:
    try:
        # Try to find the div element at the current index
        div = browser.find_element(By.CSS_SELECTOR, f'#todays-races-time-view > cdux-todays-races-time-view > div > div.todays-all > .track.track-list--row.has-message.ng-star-inserted:nth-child({index})')

        # Scroll to the div
        browser.execute_script("arguments[0].scrollIntoView();", div)

        # Allow some time for scrolling
        sleep(1)

        # Click the div
        div.click()

        sleep(2)
        # Collect the URL
        urls.append(browser.current_url)

        # Go back to the previous page
        browser.back()

        # Give the page some time to load
        sleep(2)

        # Increase the index
        index += 1

    except NoSuchElementException:
        # No more elements to process, break the loop
        break

    except Exception as e:
        print(f"Skipping element due to error: {e}")
        # Increase the index
        index += 1

# Print all the collected URLs
for url in urls:
    print(url)

# Close the browser
browser.quit()