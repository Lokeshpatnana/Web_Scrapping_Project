import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Darling_(2010_film)")
soup = BeautifulSoup(html,"html.parser")
table = soup.findAll("table",{"class":"wikitable"})[0]
rows = table.findAll("tr")

with open("darlingfilmy.csv","wt+",newline="") as f:
    writer = csv.writer(f)
    for i in rows:
        row = []
        for cell in i.findAll(["td","td"]):
            row.append(cell.get_text())
        writer.writerow(row)

import pandas as pd
a = pd.read_csv("darlingfilmy.csv")
print(a)
print(a.shape)