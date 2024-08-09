import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import shutil
import requests

# PATH variable - ChromeDriver path
PATH = "/usr/bin/chromedriver"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Define the service with the path to ChromeDriver
service = Service(PATH)

# Initialize the WebDriver with service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL to the Instagram reel
url = 'https://www.instagram.com/reel/url/'
driver.get(url)

# Wait for the page to load
time.sleep(5)  # Or use WebDriverWait for a better approach

# Find the specific script tag containing the video URL
try:
    find = driver.find_element(by=By.XPATH, value='/html/head/script[3]')
    text = find.get_attribute('innerText')
    driver.close()

    # Extract the video URL from the script content
    start = text.index('"contentUrl":"')
    end = text.index('","thumbnailUrl"', start + 14)
    new_text = text[start + 14:end].replace('\\/', '/')

    # Print the extracted URL for verification
    print('--------------')
    print(new_text)

    # Download the video from the extracted URL
    response = requests.get(new_text, stream=True)
    with open('output.mp4', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
except Exception as e:
    print(f"An error occurred: {e}")
    driver.quit()
