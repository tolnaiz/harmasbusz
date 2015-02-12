#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from BeautifulSoup import BeautifulSoup as Soup
from soupselect import select
import urllib2
response = urllib2.urlopen('http://www.tukebusz.hu/menetrend/3/naptipus/munkanap/megallo1/103')
html = response.read()

def no_html(strin):
	return re.sub('<[^<]+?>', '', strin)

soup = Soup(html)
print no_html(str(select(soup, '.menetrend_varhato_idopontok')))
