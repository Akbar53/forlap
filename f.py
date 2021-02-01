try:
	import requests, os, time, sys
	from bs4 import BeautifulSoup
	from requests.packages import urllib3
	urllib3.disable_warnings()
except ImportError:
	print("\33[31;1m[!]\33[37;1m Can'timport module 'requests or BeautifulSoup'\n")
	exit()
#grabbing nim from forlap url
def get_data():
  try:
    global link
    url = raw_input('Url forlap : ')
    r1 = requests.get(url,verify=False).text
    scrap1 = BeautifulSoup(r1,'html.parser')
    data1 = scrap1.find('div',attrs={'class':'tab-pane','id':'mahasiswa'})
    for href in data1.find_all('a',href=True):
      link = href.get('href')
      for grab in range(0, 1000000, 20):
        url = '%s/%s'%(link,grab)
        r2 = requests.get(url,verify=False).text
        if "<tr class='tmiddle'>" in r2:
          scrap2 = BeautifulSoup(r2, 'html.parser')
          data2 = scrap2.find_all('tr', {'class': 'tmiddle'})
          for database in data2:
			      usr = database.find('a').string
			      nim = database.findAll('td')[1].string
			      u123 = usr.split()[0]
			      print '%s:%s123'%(nim,u123.title())
        else:
          break
  except Exception as e:
    print e
get_data()