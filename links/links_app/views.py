from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL_TEMPLATE = "https://www.youtube.com/watch?app=desktop&v=vtizH9w0V7c"
r = requests.get(URL_TEMPLATE)
print(r.status_code)
# print(r.text)

soup = bs(r.text, "html.parser")
# vacancies_names = soup.find_all('h2', class_='add-bottom-sm')
meta_tags = soup.find_all('meta', property=['og:title', 'og:image', 'og:type', 'og:description'])
for m_t in meta_tags:
    print(m_t['content'])
print(meta_tags)
