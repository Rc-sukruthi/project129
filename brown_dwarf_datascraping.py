from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(start_url)
soup = BeautifulSoup(page.text, "html.parser")

#time.sleep(10)

star_table = soup.find_all("table", {"class" : "wikitable sortable"})
total_table = len(star_table)
table_row = star_table[0].find_all("tr")
temp_list = []

for row in table_row:
        table_cols = row.find_all('td')
        table_row = [i.text.rstrip() for i in table_cols]
        print(table_cols)   
        temp_list.append(table_row)

Star_names = []
Distance = []
Mass = []
Radius = []
    
for i in range(1, len(temp_list)):
        Star_names.append(temp_list[i][0])
        Distance.append(temp_list[i][5])
        Mass.append(temp_list[i][8])
        Radius.append(temp_list[i][9])
    

required_data = [Star_names, Distance, Mass, Radius]
temp_list.append(required_data)
print(temp_list)

headers = ['Star_names', 'Distance', 'Mass', 'Radius']
star_df_1 = pd.DataFrame(list(zip(Star_names, Distance, Mass, Radius,)), columns = headers)
star_df_1.to_csv('brown_dwarf_scraped_data.csv', index = True, index_label = "id")
