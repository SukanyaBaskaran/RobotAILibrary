from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# Define the URL to scrape
url = "https://accounts.lambdatest.com/login"  # Replace with your target URL

chromedriver_path = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\chromedriver.exe"

# Set up the Chrome service
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# Send a GET request to the webpage
#response = requests.get(url)
driver.get(url)

time.sleep(30)

page_source = driver.page_source

# Close the Selenium driver
driver.quit()
# Check if the request was successful

    # Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

    # Define the columns for the CSV
columns = ["element", "TAG", "ID", "TYPE", "CLASS", "NAME", "ARIA_AUTOCOMPLETE",
               "TITLE", "HREF", "TEXT", "VALUE", "ARIA_LABEL"]

    # Initialize an empty list to store row data
data = []

    # Find all elements in the HTML
elements = soup.find_all(True) # `True` finds all tags
element = []
    # Loop through each element and gather the required attributes
for element in elements:
    # Collect attributes, using `.get()` to avoid errors if the attribute is missing
    row = {
        "element": element.get("name") or element.get("id") or element.name,
        "TAG": element.name,
        "ID": element.get("id"),
        "TYPE": element.get("type"),
        "CLASS": " ".join(element.get("class", [])) if element.get("class") else None,
        "NAME": element.get("name"),
        "ARIA_AUTOCOMPLETE": element.get("aria-autocomplete"),
        "TITLE": element.get("title"),
        "HREF": element.get("href"),
        "TEXT": element.get_text(strip=True),
        "VALUE": element.get("value"),
        "ARIA_LABEL": element.get("aria-label")
    }
    data.append(row)

    # Convert the data into a DataFrame
df = pd.DataFrame(data, columns=columns)

    # Save the DataFrame to a CSV file
df.to_csv("Test.csv", index=False)
print("Data saved to web_scraped_data.csv")

