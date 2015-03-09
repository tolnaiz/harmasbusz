import os
import re
import soupselect
from bs4 import BeautifulSoup
from soupselect import select
import urllib2
import urllib
import datetime

class Harmas:
	def idopontok(self):
		day = datetime.datetime.today().weekday()
		if day == 6:
			naptipus = "szabadnap"
		elif day == 4:
			naptipus = "utolso"
		else:
			naptipus = "munkanap"

		menetrend_url = 'http://www.tukebusz.hu/menetrend/3/naptipus/'+naptipus+'/megallo1/103'
		response = urllib2.urlopen(menetrend_url)
		html = response.read()
		soup = BeautifulSoup(html)
		return Harmas.remove_html(str(select(soup, '.menetrend_varhato_idopontok')[0]))

	def kovetkezo_erkezes(self):
		menetrend_url = 'http://menobusz.tukebusz.hu/php/sql.php'
		data = urllib.urlencode({'id' : 'online_erkezes|27907'})
		response = urllib2.urlopen(menetrend_url, data)
		for x in response.read().split("\n"):
			sor = x.split("|")
			if sor[6].strip() == '3':
				kov_p = int(float(sor[3]))
				kov_m = int((float(sor[3]) - kov_p ) * 60)
				return [kov_p,kov_m]

	@staticmethod
	def remove_html(string):
		return re.sub('<[^<]+?>', '', string)