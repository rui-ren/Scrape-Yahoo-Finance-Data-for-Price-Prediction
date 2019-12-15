# get temperature for the calculation
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

URL = "https://sercc.com/climateinfo_files/monthly/Southeast_temp_DivNew_files/sheet001.htm"
reply = requests.get(URL)

with open('test.html', 'w') as f:
    f.write(reply.text)

data = {}
year = 2007
start = False

with open('test.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
    
    print(soup.find_all('td'))
    for a in soup.find_all('td'):
        print(a, '/n', '....')
        try:
            b = float(a.text)
        except:
            if start and a.text == '':
                break
            else:
                continue
        if b >= 2007 and b <= 2019:
            year = b
            start = True
        elif start:
            if year not in data.keys():
                data[year] = []
            data[year].append(b)


# 12 month          
for year in data.keys():
    if len(data[year]) == 13:
        data[year] = data[year][:-1]
        
        
x = []
y = []

for year in data.keys():
    for i, temp in enumerate(data[year]):
        x.append(year+0.08*i)
        y.append(temp)
