from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
#from scrape import results

app = Flask(__name__, template_folder='tamplates')

@app.route('/')


def hello_world():
    # Collect and parse first page
    final = []
    page = requests.get('http://teertoday.com')
    soup = BeautifulSoup(page.text, 'html.parser')
    h = soup.find('h2')
    table_body = soup.find('table')
    table_list = soup.findAll('td')
    for date in table_list:
        cal = date.text.strip()
        final.append(cal)
    h2 = h.text.strip()
    dateup = h2
    t1 = final[0]
    t2 = final[1]
    fr = final[2]
    sr = final[3]

    return render_template('index.html', frist=fr, secund=sr, tim1=t1, tim2=t2, deup=dateup)

if __name__ == '__main__':
    app.run(debug=True)