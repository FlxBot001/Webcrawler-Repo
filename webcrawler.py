#My imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

#Requsting data from the website
html = requests.get("http://www.worldometer.info/coronavirus")

#Checking to verify downloaded contents
html.content()

#Parse th HTML file and find the code
html_parsed = BeautifulSoup(html.content)

#Pass the HTML code and find the requred table
table = html_parsed.find('table', attrs={id:'main_table_countries_today'})

#Check results
table()

#Get all rows
rows = table.find_all('tr')

#First row
rows[0]

#Remove all markers from HTML code on the first row
rows[0].text.strip()

#Tokenization
rows[9].text.strip().split("\n")

#Store rows into a list
data = []
for x in rows:
    data.append(x.text.strip().split("\n")[1:15]) #Get the first 9 column

#Convert data into DataFrame
df.head()

#Set first row as header and delete second rows
df.pd.Data_Frame(data[9:], columns=data[0])

#Check DataFrame
df.head()

#save csv file
df.to_csv('Covid19.csv')

#Get required columns
df.plot_df[['country', 'Other', 'TotalCases']]

#Get first 10 rows
df.plot = df_plot[:10]
df_plot.head()

#Remove commas to digits
df_plot['TotalCases'] = df_plot['TotalCases'].apply(lambda x: x.replace(',',''))
df_plot.head

#Plot
df_plot.head()
df_plot.plot(kind='bar', x = 'country', 'other', y = TotalCases')
