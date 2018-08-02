# keys are year, value are average
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

page = requests.get('https://www.baseball-reference.com/teams/BOS/batteam.shtml')
# page.content
soup = BeautifulSoup(page.content, 'html.parser')

list(soup.children)
[type(item) for item in list(soup.children)]

html = list(soup.children)[3]
body = list(html.children)[3]

batting_avg = body.find_all('td', attrs={'data-stat': 'batting_avg'})
year = body.find_all('th', attrs={'data-stat': 'year_ID'})

averages = []
years = []

for i in batting_avg:
    all_averages = i.get_text()
    averages.append(all_averages)

averages_dict = {}
averages_dict['Batting Average'] = averages

year.pop(0)
for item in year:
    all_years = item.get_text()
    years.append(all_years)

averages_dict['Year'] = years
# print(averages_dict)


df = pd.DataFrame(averages_dict)
df['Year'] = df['Year'].astype(int)
df['Batting Average'] = df['Batting Average'].astype(float)

plt.figure(figsize=(20, 10))
values = averages_dict.values()

keys = averages_dict.keys()
plt.scatter(df['Year'], df['Batting Average'])
plt.ylabel('Batting Average')
plt.xlabel('Year')
plt.legend()
plt.title('Year by Year Averages for the Red Sox')
plt.show()