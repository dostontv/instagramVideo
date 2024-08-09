from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import shutil
import requests

PATH = "C:\Program Files (x86)\chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(PATH, options=chrome_options)

url = 'https://www.instagram.com/reel/url/'
# Open the YouTube video URL in the browser
driver.get(url)

find = driver.find_element(by=By.XPATH, value='/html/head/script[3]')
text = find.get_attribute('innerText')
driver.close()

start = text.index('"contentUrl":"')
end = text.index('","thumbnailUrl"', start + 14)
print(text)
new_text = text[start + 14:end].replace('\/', '/')

print('--------------')
print(new_text)
response = requests.get(new_text, stream=True)
with open('output.mp4', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response