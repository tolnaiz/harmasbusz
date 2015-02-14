import os
import re
import soupselect
from bs4 import BeautifulSoup
from soupselect import select
import urllib2

class Harmas:
	def get(self):
		menetrend_url = 'http://www.tukebusz.hu/menetrend/3/naptipus/munkanap/megallo1/103'
		response = urllib2.urlopen(menetrend_url)
		html = response.read()
		soup = BeautifulSoup(html)
		return Harmas.remove_html(str(select(soup, '.menetrend_varhato_idopontok')[0]))

	@staticmethod
	def remove_html(string):
		return re.sub('<[^<]+?>', '', string)