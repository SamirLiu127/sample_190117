# -*- coding: utf-8 -*-
import random
import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)


@app.route("/")
def urad_hello():
    return "<p>{}</p>".format(crawler_text())


def get_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }
    res = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(res.text.encode('utf-8'), "html.parser")
    return soup


def crawler_text():
    soup = get_soup('http://wiki.python.org.tw/The%20Zen%20Of%20Python')
    line = soup.select('p.line874')
    num = random.randint(1, len(line)-1)
    return str(line[num].next)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
