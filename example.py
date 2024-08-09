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
# Check for another possible source of video URL
try:
    video_tag = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'video'))
    )
    video_url = video_tag.get_attribute('src')

    print('--------------')
    print(video_url)

    response = requests.get(video_url, stream=True)
    with open('output.mp4', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
