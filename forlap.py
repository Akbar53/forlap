#created 31-08-2020,v4
#author Lumiere
#contact me : https://t.me/ardanf
try:
	import requests, os, time, sys
	from bs4 import BeautifulSoup
	from requests.packages import urllib3
	urllib3.disable_warnings()
except ImportError:
	print("\33[31;1m[!]\33[37;1m Can'timport module 'requests or BeautifulSoup'\n")
#warna
red = '\33[31;1m'
white = '\33[37;1m'
green= '\33[32;1m'
cyan='\33[0;36m'
#remove duplicate
def duplicate():
		with open(sv) as rm:
			rm_duplicate = set(rm.readlines())
			with open(sv,'w') as rmv:
				rmv.writelines(set(rm_duplicate))
#index code
def grab():
	try:
		
		global sv
		n = 0
		os.system('clear')
		print('''%s
   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \  %s- NIM GRABBER -%s
 ( F | o | r | l | a | p ) %sauthor :lumiere%s
  \_/ \_/ \_/ \_/ \_/ \_/  %scontact me : https://t.me/ardanf%s
'''%(green,red,green,cyan,green,cyan,white))
		url = input('Masukan url forlap : ')
		sv = input('Simpan nim di? : ')
		print()
		print('%s[ ! ]%s++++++++++%s[ ! ]%s RESULT %s[ ! ]%s++++++++++%s[ ! ]%s\n'%(red,white,red,green,red,white,red,white))
		r2 = requests.get(url,verify=False)
		scrap2 = BeautifulSoup(r2.text, 'html.parser')
		data = scrap2.find('div',attrs={'class':'tab-pane','id':'mahasiswa'})
		for href in data.find_all('a',href=True):
			link = href.get('href')
			for rng in range(0, 100000, 20):
				url = ('{}/{}'.format(link,rng))
				p = open(sv,'a')
				r = requests.get(url,verify=False)
				scrap = BeautifulSoup(r.text, 'html.parser')
				data = scrap.find_all('tr', {'class': 'tmiddle'})
				for get in data:
					table = get.findAll('td')[1]
					for nim in table:
						data_nim = nim.replace(" ","")
						n += 1
						sys.stdout.write('\r%s%s %s| Retrive nim ~>%s %s'%(red,n,green,white,data_nim))
						sys.stdout.flush()
						p.write('{}\n'.format(data_nim))
				if "<tr class='tmiddle'>" in r.text:
					continue
				else:
					break
		os.system('clear')
		print('\n%s[!]%s Sukses grab semua NIM!!, total ~> %s%s'%(red,white,green,n))
		duplicate()
		time.sleep(1.5)
		print('\n%s[!]%s Menghapus duplikat nim sukses....'%(red,white))
		print('%s[!]%s NIM tersimpan di ~>%s %s %s'%(red,white,green,sv,white))
	except FileNotFoundError:
		print('\n%s[!]%s File Not found!!'%(red,white))
	except (requests.exceptions.InvalidURL, requests.exceptions.MissingSchema):
		print('\n%s[!]%s Invalid URL'%(red,white))
	except NameError:
		print('\n%s[!]%s Pastikan URL benar!!'%(red,white))
		pass
	except AttributeError:
		print('\n%s[!]%s Pastikan url studi dari forlap!!'%(red,white))
	except requests.exceptions.ConnectionError:
		print('\n%s[!]%s Connection error!!'%(red,white))
		time.sleep(1.5)
		print('%s[!]%s Menghapus duplikat nim sukses....'%(red,white))
		duplicate()
	except KeyboardInterrupt:
		print('\n%s[!]%s KeyboardInterupt exiting....'%(red,white))
		time.sleep(1.5)
		print('%s[!]%s Menghapus duplikat nim sukses....'%(red,white))
		duplicate()
grab()