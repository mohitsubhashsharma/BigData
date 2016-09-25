# Importing required Packages
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv

# Getting data from Databaseolympics website using request package
r  = requests.get("http://www.databaseolympics.com/games/gamesyear.htm?g=47")

data = r.text

# Getting data into HTML format
soup = BeautifulSoup(data,"html.parser")

#Finding the HTML table which contains data we need
table = soup.find('table', {'class': 'pt8'})

# Extracting the scrapped Data into CSV File        
with open('Olympics2008.csv', 'w') as f:
    csvwriter = csv.writer(f)
    for row in table.findAll('tr'):
        cells = [c.text for c in row.findAll('td')]
        if len(cells) == 5: 
            csvwriter.writerow(cells)
