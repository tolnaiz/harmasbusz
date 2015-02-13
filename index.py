import os
from flask import Flask
import re
import soupselect
from BeautifulSoup import BeautifulSoup as Soup
from soupselect import select
import urllib2

app = Flask(__name__)

@app.route('/')
def index():
    response = urllib2.urlopen('http://www.tukebusz.hu/menetrend/3/naptipus/munkanap/megallo1/103')
    html = response.read()

    def no_html(strin):
    	return re.sub('<[^<]+?>', '', strin)

    soup = Soup(html)
    return no_html(str(select(soup, '.menetrend_varhato_idopontok')))
