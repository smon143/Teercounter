import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

def results():
    # Collect and parse first page
    final = []
    page = requests.get('https://www.teernightindia.com/')
    soup = BeautifulSoup(page.text, 'html.parser')
    h = soup.find('h2')
    table_body = soup.find('table')
    table_list = soup.findAll('td')
    for date in table_list:
        cal = date.text.strip()
        final.append(cal)
    h2 = h.text.strip()
    test = final[0]
    print(test)




results()