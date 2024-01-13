import pandas as pd
import requests
from bs4 import BeautifulSoup

def getdata(url):
    r = requests.get(url)
    return r.text

# Get HTML data from the provided URL
htmldata = getdata("https://www.goodreturns.in/petrol-price.html")

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(htmldata, 'html.parser')

# Find all div elements with class "gold_silver_table"
result = soup.find_all("div", class_="gold_silver_table")
print(result)  # This will print the extracted HTML content, mostly for debugging purposes

mydatastr = ''
result = []

# Iterate through all table rows (tr elements) in the HTML data
for table in soup.find_all('tr'):
    mydatastr += table.get_text()

# Remove the initial newline character and split the data into a list of items
mydatastr = mydatastr[1:]
itemlist = mydatastr.split("\n\n")

# Split each item into separate lines and store them in the result list
for item in itemlist[:-5]:
    result.append(item.split("\n"))

# Create a DataFrame from the result list, excluding the last 8 items
df = pd.DataFrame(result[:-8])

# Print the resulting DataFrame
print(df)
