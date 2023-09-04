from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import os

page_url = "https://emojipedia.org/apple"
output_directory = "emojis"
os.makedirs(output_directory, exist_ok=True)

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

if not os.path.exists("emoji_links.txt"):
    print("Please run the first script to get the emoji links")
    exit()

# if the file exists, dont open the browser
# just read the links from the file
with open("emoji_links.txt", "r") as file:
    emoji_links = file.read().splitlines()

print(emoji_links)

driver = webdriver.Chrome()
# Open the webpage
driver.get(page_url)

# Scroll down to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# sleep for 10 seconds
time.sleep(10)

# Get the page source after scrolling
page_source = driver.page_source

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Get all the anchor tags that has .Emoji_emoji__P7Lkz class
emojis = soup.find_all("a", class_="Emoji_emoji__P7Lkz")

# get their href attribute
emoji_links = [emoji["data-src"] for emoji in emojis]

print(emoji_links)

# save emoji links into a file
with open("emoji_links.txt", "w") as file:
    for link in emoji_links:
        file.write(link + "\n")

driver.quit()
