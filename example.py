from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

try:
    # Wait until the meta tag with the video URL is present
    meta_tag = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//meta[@property="og:video"]'))
    )

    # Get the content of the meta tag, which contains the video URL
    video_url = meta_tag.get_attribute('content')

    # Print the extracted video URL
    print('--------------')
    print(video_url)

    # Download the video from the extracted URL
    response = requests.get(video_url, stream=True)
    with open('output.mp4', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
