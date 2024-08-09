from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import shutil
import requests
# sudo apt update
# sudo apt install -y chromium-chromedriver

# PATH variable - ChromeDriver path
PATH = "/usr/bin/chromedriver"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(PATH)
# Define the driver with options
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL to the Instagram reel
url = 'https://www.instagram.com/reel/url/'
driver.get(url)

# Find the specific script tag containing the video URL
find = driver.find_element(by=By.XPATH, value='/html/head/script[3]')
text = find.get_attribute('innerText')
driver.close()

# Extract the video URL from the script content
start = text.index('"contentUrl":"')
end = text.index('","thumbnailUrl"', start + 14)
new_text = text[start + 14:end].replace('\/', '/')

# Print the extracted URL for verification
print('--------------')
print(new_text)

# Download the video from the extracted URL
response = requests.get(new_text, stream=True)
with open('output.mp4', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response
