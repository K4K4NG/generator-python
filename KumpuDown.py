import pytube
import colorsys
import requests,bs4,sys,os,datetime,re,time,json
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
from bs4 import BeautifulSoup as bs
from datetime import datetime
from rich.panel import Panel as nel
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
P2 = "[#FFFFFF]" # PUTIH
def loo():
	print(f"\t____  __.________  ________________.___.\n\t|    |/ _|\______ \ \_   _____/\__  |   |\n\t|      <   |    |  \ |    __)   /   |   |\n\t|    |  \  |    `   \|     \    \____   |\n\t|____|__ \/_______  /\___  /    / ______|\n\t\/        \/     \/     \/ ") 
	cetak(nel(f"\t\tAuthor : {H2}YTeTeA{P2}\n\t\tVersion : {H2}0.1{P2}\n\t\tGithub : {H2}K4K4NG{P2}")) 
	cetak(f" {H2}Jika Ada Kesalahan Dalam Script Ini tolong di maaf kan karena\n\t\t    masih tahap percobaan{P2}")
def pilihan():
	os.system('clear') 
	loo() 
	print("") 
	cetak(f"\t{M2}[ ──────────── [  {P2}{H2}Menu Pilihan{P2}  {M2}] ──────────── ]{P2}") 
	print("") 
	prints(f"\t1. Downloader Video Lagu You Tube \t[ {H2}Aman{P2} ]\n\t2. Auto Bom Chat Fb \t\t\t[ {H2}Aman{P2} ]\n\t3. Auto Coment Fb \t\t\t[ {H2}Aman{P2} ]\n\t4. Auto Post Poto Fb \t\t\t[ {H2}Aman{P2} ]\n")
	cetak(f"\t{M2}[ ──────────── [  {P2}{H2}Menu Pilihan{P2}  {M2}] ──────────── ]{P2}") 
	print("") 
	su = input(f"\t└──╭➣ Pilihan 1 Sampai 4 : ") 
	if su in ["1"]:
		ah() 
	elif su in ["2"]:
		strr() 
	elif su in ["3"]:
		mainw() 
	elif su in ["4"]:
		ciah() 
	elif su in ["5"]:
		warna() 
	else:
		exit()
def ciah():
	bajigan()
def ah():
	suuu() 
def ti():
	clear()
	start()
	login()
	akhir()
def strr():
	clear()
	mula()
	main()
	akhir()
#pelangi edan

	
	
#bom chat fb

# -->  Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

# --> Ubah Bahasa
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = bs(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"}
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

# --> Waktu
def mula():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        prints('\n[bold red] Program Selesai Dalam Waktu %s Menit %s Detik[white]\n'%(Menit,Detik))
    except Exception as e:
        prints('\n[bold green]Program Selesai Dalam Waktu 0 Detik[white]\n')

# --> Login
class main:
    def __init__(self):
        self.xyz = requests.Session()
        self.cek_cookies()
    def cek_cookies(self):
        try:
            self.token  = open('login/token.json','r').read()
            self.cookie = {'cookie':open('login/cookie.json','r').read()}
            language(self.cookie)
            get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token),cookies=self.cookie)
            jsx = json.loads(get.text)
            nama = jsx["name"]
            clear()
            print('Login Sebagai %s\n'%(nama))
            auto_chat_messenger()
        except Exception as e:
            self.cookie_invalid()
    def cookie_invalid(self):
        print('\nCookie Invalid!')
        time.sleep(2)
        clear()
        self.insert_cookie()
    def insert_cookie(self):
        loo()
        print('Selamat Datang Di tools Bot Chat Fb ')
        ciko = input('Masukkan Cookie : ')
        toke = self.generate_token(ciko)
        try:os.mkdir("login")
        except:pass
        open('login/cookie.json','w').write(ciko)
        open('login/token.json','w').write(toke)
        self.cek_cookies()
    def generate_token(self,cok):
        try:
            url = 'https://business.facebook.com/business_locations'
            req = self.xyz.get(url,cookies={'cookie':cok})
            tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
            return(tok)
        except Exception as e:exit(main())

class auto_chat_messenger:
    
    # --> Trigger
    def __init__(self):
        self.gagal    = 0
        self.berhasil = 0
        self.for_loop = 0
        self.tararget = []
        self.listchat = []
        self.datapend = {}
        self.all_history = []
        self.xyz = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.token  = self.generate_token()
        self.menu()

    # --> Generate Token
    def generate_token(self):
        try:
            url = 'https://business.facebook.com/business_locations'
            req = self.xyz.get(url,cookies=self.cookie)
            tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
            return(tok)
        except Exception as e:exit('\nCookies Invalid\n')

    # --> Main Menu Chat
    def menu(self):
        print('[ Menu Spam Chat ]')
        print('[1] Manual')
        print('[2] Otomatis (Banyak)')
        print('[3] Hapus Chat')
        xa = input('Pilih : ')
        print('')
        if xa in ['1','01','a']:
            print('[ Menu Spam Chat Manual ]')
            print('[1] Input Target Berdasar ID')
            print('[2] Pilih Target Dari Riwayat Chat')
            print('[3] Pilih Target Dari Daftar Teman')
            xb = input('Pilih : ')
            print('')
            if   xb in ['1','01','a']: self.manual_input(); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            elif xb in ['2','02','b']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('Dapunta'); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            elif xb in ['3','03','c']: self.choice_input_graph('https://graph.facebook.com/me?fields=friends.fields(id,name)&limit=5000&access_token='+self.token); self.pilih_riwayat_graph('Dapunta'); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            else:exit('\nIsi Yang Benar !\n')
        elif xa in ['2','02','b']:
            print('[ Menu Spam Chat Otomatis ]')
            print('[1] Spam Chat Semua Riwayat Chat')
            print('[2] Spam Chat Semua Daftar Teman')
            xc = input('Pilih : ')
            print('')
            if   xc in ['1','01','a']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('SuciMHR'); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            elif xc in ['2','02','b']: self.choice_input_graph('https://graph.facebook.com/me?fields=friends.fields(id,name)&limit=5000&access_token='+self.token); self.pilih_riwayat_graph('SuciMHR'); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            else:exit('\nIsi Yang Benar !\n')
        elif xa in ['3','03','c']:
            print('[ Menu Hapus Chat ]')
            print('[1] Hapus Semua Riwayat Chat')
            print('[2] Hapus Chat Pilihan')
            print('[3] Hapus Chat Kecuali')
            xd = input('Pilih : ')
            print('')
            if   xd in ['1','01','a']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('SuciMHR'); self.sortir_delete()
            elif xd in ['2','02','b']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('Dapunta'); self.sortir_delete()
            elif xd in ['3','03','c']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('Rancay');  self.sortir_delete()
            else:exit('\nIsi Yang Benar !\n')
        else:
            exit('\nIsi Yang Benar !\n')

    # --> Input Manual Berdasar ID
    def manual_input(self):
        print('Banyak Target? Pisahkan Dengan Koma (,)')
        id  = input('Masukkan ID Target : ').split(',')
        for x in id:
            self.tararget.append(x) # --> Array ID

    # --> Pilih Berdasar Riwayat Chat
    def choice_input_scrap(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for x in req.find_all('h3'):
                try:
                    y = x.find('a',href=True)
                    if str(y) == 'None': pass
                    else:
                        z = re.search('tid=(.*?)&amp',str(y)).group(1).split('.')[2].split('%')[0]
                        self.for_loop += 1
                        print('[%s] %s'%(str(self.for_loop),y.text[:30]))
                        self.all_history.append(z)
                        self.datapend.update({str(self.for_loop):z})
                except Exception as e:pass
            net = 'https://mbasic.facebook.com' + req.find('a',string='Lihat Pesan Sebelumnya')['href']
            self.choice_input_scrap(net)
        except Exception as e:pass
    def pilih_riwayat_scrap(self,tp):
        if tp == 'Dapunta':
            print('\nBanyak Target? Pisahkan Dengan Koma (,)')
            xd = input('Pilih : ').split(',')
            for x in xd:
                self.tararget.append(self.datapend[x]) # --> Array ID
        elif tp == 'Rancay':
            print('\nKecualikan Chat? Pisahkan Dengan Koma (,)')
            xx = input('Pilih : ').split(',')
            for d in xx:
                self.all_history.remove(str(self.datapend[d]))
            self.tararget = self.all_history # --> Array ID
        else:
            self.tararget = self.all_history # --> Array ID
    
    # --> Pilih Berdasar Daftar Teman
    def choice_input_graph(self,url):
        try:
            req = self.xyz.get(url,cookies=self.cookie).json()
            for x in req['friends']['data']:
                try:
                    self.for_loop += 1
                    print('[%s] %s'%(str(self.for_loop),x['name'][:30]))
                    self.all_history.append(x['id'])
                    self.datapend.update({str(self.for_loop):x['id']})
                except Exception as e:pass
        except Exception as e:exit('\nTeman Tidak Ditemukan')
    def pilih_riwayat_graph(self,tp):
        if tp == 'Dapunta':
            print('\nBanyak Target? Pisahkan Dengan Koma (,)')
            xd = input('Pilih : ').split(',')
            for x in xd:
                self.tararget.append(self.datapend[x]) # --> Array ID
        else:
            self.tararget = self.all_history # --> Array ID

    # --> Pilihan Opsi Lain
    def tulis_chat(self):
        print('\nBanyak Chat? Pisahkan Dengan (<>)')
        chat = input('Tulis Chat : ').split('<>')
        for x in chat:
            self.listchat.append(x) # --> Array Chat
        if len(chat) > 1:self.choice_chat()
        else:self.urut_chat = False
    def jumlah_chat(self):
        self.jc = input('\nJumlah Kelipatan Tiap Chat : ') # --> Jumlah Masing² Chat
    def choice_chat(self):
        print('\n[ Pilih Urutan Chat ]')
        print('[1] A, B, A, B, A, B')
        print('[2] A, A, A, B, B, B')
        xd = input('Pilih : ')
        if   xd in ['1','01','a']: self.urut_chat = 'bolak'
        elif xd in ['2','02','b']: self.urut_chat = 'balik'
        else:exit('\nIsi Yang Benar !\n')
    def kalkulasi(self):
        print('\n[ Kalkulasi ]')
        print('Jenis Chat            : %s'%(str(len(self.listchat))))
        print('Jumlah Penerima       : %s'%(str(len(self.tararget))))
        print('Jumlah Kelipatan Chat : %s'%(str(int(self.jc))))
        print('Total %s Chat Akan Dikirim\n'%(str(len(self.listchat)*len(self.tararget)*int(self.jc))))

    # --> Sortir Chat & Target
    def sortir(self):
        if self.urut_chat == 'balik':
            for x in self.tararget:
                self.perorangan_berhasil = 0
                self.perorangan_gagal    = 0
                for y in self.listchat:
                    for s in range(int(self.jc)):
                        self.exec(x,y)
                try:
                    print('\rSpam Chat %s                      '%(self.nama[:20]))
                    print('\r   • Berhasil : %s                      '%(str(self.perorangan_berhasil)))
                    print('\r   • Gagal    : %s                      '%(str(self.perorangan_gagal)))
                    print('\r')
                except Exception as e:pass
        else:
            for x in self.tararget:
                self.perorangan_berhasil = 0
                self.perorangan_gagal    = 0
                for s in range(int(self.jc)):
                    for y in self.listchat:
                        self.exec(x,y)
                try:
                    print('\rSpam Chat %s                      '%(self.nama[:20]))
                    print('\r   • Berhasil : %s                      '%(str(self.perorangan_berhasil)))
                    print('\r   • Gagal    : %s                      '%(str(self.perorangan_gagal)))
                    print('\r')
                except Exception as e:pass

    # --> Requests Post Message
    def exec(self,id,cet):
        url = 'https://mbasic.facebook.com/messages/thread/'+id
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            fom = req.find('form',{'method':'post'})
            try:
                data = {
                    'fb_dtsg'      : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                    'jazoest'      : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                    'tids'         : re.search('name="tids" type="hidden" value="(.*?)"',   str(fom)).group(1),
                    'csid'         : re.search('name="csid" type="hidden" value="(.*?)"'   ,str(fom)).group(1),
                    'cver'         : 'legacy',
                    'ids[%s]'%(id) : id,
                    'wwwupp'       : 'C3',
                    'platform_xmd' : ''}
            except Exception as e:
                data = {
                    'fb_dtsg'      : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                    'jazoest'      : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                    'ids[%s]'%(id) : id}
            data.update({'body':cet,'send':'Kirim'})
            nek = 'https://mbasic.facebook.com' + fom['action']
            cuy = bs(self.xyz.post(nek,data=data,cookies=self.cookie).content,'html.parser').find('title').text
            if cuy == 'Kesalahan':
                self.gagal += 1
                self.perorangan_gagal += 1
                print('\r[Proses] [Berhasil:%s] [Gagal:%s]'%(str(self.berhasil),str(self.gagal)),end='');sys.stdout.flush()
            else:
                self.berhasil += 1
                self.perorangan_berhasil += 1
                self.nama = cuy
                print('\r[Proses] [Berhasil:%s] [Gagal:%s]'%(str(self.berhasil),str(self.gagal)),end='');sys.stdout.flush()
        except Exception as e:pass

    # --> Delete Chat
    def sortir_delete(self):
        self.delchat = 0
        for id in self.tararget:
            url = 'https://mbasic.facebook.com/messages/thread/'+id
            self.delete1(url)
    def delete1(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            fom = req.find_all('form',{'method':'post'})[1]
            data = {
                'fb_dtsg'      : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                'jazoest'      : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                'delete'       : 'Hapus'}
            nek = 'https://mbasic.facebook.com' + fom['action']
            self.delete2(nek,data)
        except Exception as e:pass
    def delete2(self,url,data):
        try:
            req = bs(self.xyz.post(url,data=data,cookies=self.cookie).content,'html.parser')
            got = req.find('a',string='Hapus')['href']
            nok = 'https://mbasic.facebook.com'+got
            roq = bs(self.xyz.get(nok,cookies=self.cookie).content,'html.parser')
            self.delchat += 1
        except Exception as e:
            pass
        print('\rBerhasil Menghapus %s Chat'%(str(self.delchat)),end='');sys.stdout.flush()





import youtube_dl

def suuu():
	os.system('clear') 
	loo() 
	print(f"Selamat Datang Di tool install video atau lagu you tube") 
	video_url = input("url video  :")
	video_inpo = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
	filename = f"{video_inpo['title']}.mp3"
	options={'format':'bestaudio/best','keepvideo':False,'outtmpl':filename}
	with youtube_dl.YoutubeDL(options) as ydl:
		ydl.download([video_inpo['webpage_url']])
	print("Download complete... {}".format(filename))
    
    
    




#bot auto comen
import os,requests,json,time,sys,random
r_get = requests.get
r_pos = requests.post
js_lo = json.loads
url1_ = 'https://graph.facebook.com/'
url2_ = '?access_token='
url3_ = '?fields=feed&access_token='
post_dev = []
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")
def logo():
	loo() 
	print(f"Selamat Datang Di Bot Auto Comen") 
def login():
    os.system('rm -rf token.txt');clear();logo()
    tok_dev = input('Masukkan Token : ')
    try:re_gex = r_get("%sme%s%s"%(url1_,url2_,tok_dev));re_jso = js_lo(re_gex.text);re_num = re_jso['name'];with_ = open("token.txt", "w");with_.write(tok_dev);with_.close();mainw()
    except (KeyError,IOError):print('Token Invalid');os.system('rm -rf token.txt');login()
    except requests.exceptions.ConnectionError:print('Koneksi Bermasalah');exit()
def mainw():
    clear();logo()
    try:tok_dev = open("token.txt","r").read();re_gex = requests.get("%sme%s%s"%(url1_,url2_,tok_dev));re_jso = json.loads(re_gex.text);re_num = re_jso['name']
    except (KeyError,IOError):print('Token Invalid');os.system('rm -rf token.txt');login()
    except requests.exceptions.ConnectionError:print('Koneksi Bermasalah');exit()
    print('Komentar Post Target Harus Publik');print('Apabila Target Grup');print('Harus Bergabung Ke Dalam Grup');print('\nPisahkan ID Target Dengan \',\'')
    id_dev = input('Masukkan ID : ').split(',')
    print('\nPisahkan Komentar Acak Dengan \',,\'');print('Ganti Baris Komentar Dengan \'===\'');kom_dev = input('Masukkan Komentar : ').replace('===','\n').split(',,');print('');personal(id_dev,kom_dev,tok_dev)
def personal(id_dev,kom_dev,tok_dev):
    try:
        for id in id_dev:
            re_dev  = r_get('%s%s%s%s'%(url1_,id,url3_,tok_dev));js_dev  = js_lo(re_dev.text)
            for post in js_dev['feed']['data']:
                id_post = post['id'];post_dev.append(id_post);time.sleep(10);re_dev_kom = r_pos('%s%s/comments?message=%s&access_token=%s'%(url1_,id_post,random.choice(kom_dev),tok_dev));js_dev_kom = js_lo(re_dev_kom.text)
                if 'id' in js_dev_kom:print('Komentar Ke %s Berhasil'%(len(post_dev)))
                elif 'error' in js_dev_kom:print('Komentar Ke %s Gagal'%(len(post_dev)))
        print('Proses Selesai');exit()
    except (KeyError,IOError):print('Token Invalid / ID Tidak Ditemukan');exit()
    except requests.exceptions.ConnectionError:print('Koneksi/Sinyal Bermasalah');exit() 





#auto post poto
###----------[ MODULES ]---------- ###
import requests,bs4,sys,os,re,time,random,json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bs

###----------[ CLEAR TERMINAL ]---------- ###
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

###----------[ CHANGE LANGUAGE ]---------- ###
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = bs(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get('https://business.facebook.com/business_locations', headers = {
            "user-agent"                :'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
            "referer"                   : 'https://www.facebook.com/',
            "host"                      : "business.facebook.com",
            "origin"                    : 'https://business.facebook.com',
            "upgrade-insecure-requests" : "1",
            "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control"             : "max-age=0",
            "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type"              : "text/html; charset=utf-8"},
            cookies = {"cookie":cookie})
        return(re.search('(\["EAAG\w+)', get_tok.text).group(1).replace('["',''))

###----------[ MENU UTAMA ]---------- ###
class bajigan:
    def __init__(self):
        self.xyz = requests.Session()
        self.cek_cookies()
    def cek_cookies(self):
        try:
            self.token  = open('login/token.json','r').read()
            self.cookie = {'cookie':open('login/cookie.json','r').read()}
            language(self.cookie)
            get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token),cookies=self.cookie)
            jsx = json.loads(get.text)
            nama = jsx["name"]
            clear()
            print('Login Sebagai %s\n'%(nama))
            exit(self.menu())
        except Exception as e:
            self.cookie_invalid()
    def cookie_invalid(self):
        print('Cookie Invalid!')
        time.sleep(2)
        clear()
        self.insert_cookie()
    def insert_cookie(self):
        print('Selamat Datang Di Auto Post')
        print("") 
        loo() 
        print("") 
        print('https://business.facebook.com/business_locations')
        print('Untuk Memasukkan Kode Autentikasi')
        print("") 
        ciko = input('Masukkan Cookie : ')
        toke = clotox(ciko)
        try:os.mkdir("login")
        except:pass
        open('login/cookie.json','w').write(ciko)
        open('login/token.json','w').write(toke)
        self.cek_cookies()
    def menu(self):
        print('[1] Link URL\n[2] Galeri\n[3] Unsplash\n[4] Freepik\n[5] Anime')
        xd = input('Pilih : ')
        print('')
        if xd in ['1','01','a']:link_url(self.token,self.cookie)
        elif xd in ['2','2','b']:galeri(self.token,self.cookie)
        elif xd in ['3','3','c']:unsplash();random_post_foto(self.token,self.cookie)
        elif xd in ['4','4','d']:freepik();random_post_foto(self.token,self.cookie)
        elif xd in ['5','5','e']:myanime();random_post_foto(self.token,self.cookie)
        else:print('Isi Yg Benar!');exit()

###----------[ DUMP IMAGE LINK URL ]---------- ###
class link_url:
    def __init__(self,token,cookie):
        global data_image
        print('Pisahkan Dengan Koma (,)')
        data_image = input('Masukkan URL Gambar : ').split(',')
        df = input('\nPosting Urut/Random [u/r] : ').lower()
        if df in ['1','01','a','u']:
            album = input('Masukkan ID Album : ')
            pesan = input('Tulis Pesan Teks : ')
            jumlah = int(input('Berapa Unggahan Per Foto : '))
            print('Jumlah Foto Yg Akan Diunggah : %s'%(str(jumlah*len(data_image))))
            with ThreadPoolExecutor(max_workers=35) as TPE:
                for gambar in data_image:
                    TPE.submit(ordinal_post_foto,album,pesan,gambar,jumlah,token,cookie)
        elif df in ['2','02','b','r']:
            random_post_foto(token,cookie)

###----------[ DUMP IMAGE FILE/GALERY ]---------- ###
class galeri:
    def __init__(self,token,cookie):
        global data_image
        print('Pisahkan Dengan Koma (,)')
        data_image = input('Masukkan Lokasi Penyimpanan Gambar : ').split(',')
        df = input('\nPosting Urut/Random [u/r] : ').lower()
        if df in ['1','01','a','u']:
            album = input('Masukkan ID Album : ')
            pesan = input('Tulis Pesan Teks : ')
            jumlah = int(input('Berapa Unggahan Per Foto : '))
            print('Jumlah Foto Yg Akan Diunggah : %s'%(str(jumlah*len(data_image))))
            with ThreadPoolExecutor(max_workers=35) as TPE:
                for gambar in data_image:
                    TPE.submit(ordinal_post_foto,album,pesan,gambar,jumlah,token,cookie)
        elif df in ['2','02','b','r']:
            random_post_foto(token,cookie)  

###----------[ DUMP IMAGE UNSPLASH ]---------- ###
class unsplash:
    def __init__(self):
        url = 'https://unsplash.com/'
        self.xyz = requests.Session()
        self.scrasp(url)
    def scrasp(self,url):
        global data_image
        data_image = []
        req = bs(self.xyz.get(url).content,'html.parser')
        for x in req.find_all('img'):
            try:
                if 'images.unsplash.com/photo' in str(x['src']):
                    data_image.append(x['src'])
            except Exception as e:pass

###----------[ DUMP IMAGE FREEPIK ]---------- ###
class freepik:
    def __init__(self):
        url = 'https://www.freepik.com/free-photos-vectors/colorful-backgrounds'
        self.xyz = requests.Session()
        self.scrasp(url)
    def scrasp(self,url):
        global data_image
        data_image = []
        head = {'user-agent' : 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'}
        req = bs(self.xyz.get(url,headers=head).content,'html.parser')
        for x in req.find_all('figure'):
            try:
                if 'img.freepik.com' in str(x['data-image']):
                    data_image.append(x['data-image'])
            except Exception as e:pass

###----------[ DUMP IMAGE MYANIMELIST ]---------- ###
class myanime:
    def __init__(self):
        url = 'https://myanimelist.net/character.php'
        self.xyz = requests.Session()
        self.scrasp(url)
    def scrasp(self,url):
        global data_image
        data_image = []
        req = bs(self.xyz.get(url).content,'html.parser')
        for x in req.find_all('img'):
            try:
                if 'cdn.myanimelist.net/r' in str(x['data-src']):
                    data_image.append(x['data-src'])
            except Exception as e:pass

###----------[ POST ACTION ORDINAL ]---------- ###
class ordinal_post_foto:
    def __init__(self,album,pesan,gambar,jumlah,token,cookie):
        loop = 0
        for x in range(int(jumlah)):
            try:
                url = f'https://graph.facebook.com/{album}/photos?'
                data = {
                    'method' : 'POST',
                    'message' : pesan + ' ' + str(loop+1),
                    'url' : gambar,
                    'access_token' : token
                    }
                req = requests.Session().post(url,data=data,cookies=cookie)
                if 'error' in str(req.json()):
                    loop += 1
                    print('\rAkun Spam %s'%(str(loop)),end='');sys.stdout.flush()
                else:
                    loop += 1
                    print('\rBerhasil Posting %s Gambar'%(str(loop)),end='')
                sys.stdout.flush()
            except Exception as e:
                print('\rAkun Spam',end='');sys.stdout.flush()

###----------[ POST ACTION RANDOM ]---------- ###
class random_post_foto:
    def __init__(self,token,cookie):
        self.token = token
        self.cookie = cookie
        self.xyz = requests.Session()
        self.takon()
    def takon(self):
        self.album = input('Masukkan ID Album : ')
        self.jumla = input('Berapa Jumlah Foto : ')
        self.pesan = input('Tulis Pesan Teks : ')
        self.requ()
    def requ(self):
        loop = 0
        for x in range(int(self.jumla)):
            try:
                url = f'https://graph.facebook.com/{self.album}/photos?'
                data = {
                    'method' : 'POST',
                    'message' : self.pesan + ' ' + str(loop+1),
                    'url' : random.choice(data_image),
                    'access_token' : self.token
                    }
                req = self.xyz.post(url,data=data,cookies=self.cookie)
                if 'error' in str(req.json()):
                    loop += 1
                    print('\rAkun Spam %s'%(str(loop)),end='');sys.stdout.flush()
                else:
                    loop += 1
                    print('\rBerhasil Posting %s Gambar'%(str(loop)),end='')
                sys.stdout.flush()
            except Exception as e:
                print('\rAkun Spam',end='');sys.stdout.flush()
                

#auto  unfriend


# --> Modules
import requests,bs4,sys,os,datetime,re,time,json
from bs4 import BeautifulSoup as bs
from datetime import datetime

# -->  Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

# --> Ubah Bahasa
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = bs(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"}
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

# --> Waktu
def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\nProgram Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\n\nProgram Selesai Dalam Waktu 0 Detik\n')

# --> Login
class login:
    def __init__(self):
        self.xyz = requests.Session()
        self.cek_cookies()
        main_dump()
    def cek_cookies(self):
        try:
            self.cookie     = {'cookie':open('login/cookie.json','r').read()}
            self.token_eaag = open('login/token_eaag.json','r').read()
            self.token_eaab = open('login/token_eaab.json','r').read()
            language(self.cookie)
            req1 = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()['name']
            req2 = self.xyz.get('https://graph.facebook.com/me/friends?fields=summary&limit=0&access_token=%s'%(self.token_eaab),cookies=self.cookie).json()['summary']['total_count']
            clear()
            print('Login Sebagai %s\n'%(req1))
        except Exception as e:
            self.insert_cookie()
    def insert_cookie(self):
        print('\nCookie Invalid!')
        time.sleep(2)
        clear()
        print('Apabila Akun A2F On, Pergi Ke')
        print('https://business.facebook.com/business_locations')
        print('Untuk Memasukkan Kode Autentikasi')
        ciko = input('Masukkan Cookie : ')
        self.token_eaag = self.generate_token_eaag(ciko)
        self.token_eaab = self.generate_token_eaab(ciko)
        try:os.mkdir("login")
        except:pass
        open('login/cookie.json','w').write(ciko)
        open('login/token_eaag.json','w').write(self.token_eaag)
        open('login/token_eaab.json','w').write(self.token_eaab)
        self.cek_cookies()
    def generate_token_eaag(self,cok):
        url = 'https://business.facebook.com/business_locations'
        req = self.xyz.get(url,cookies={'cookie':cok})
        tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
        return(tok)
    def generate_token_eaab(self,cok):
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = self.xyz.get(url,cookies={'cookie':cok})
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = self.xyz.get(nek,cookies={'cookie':cok})
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        return(tok)

class main_dump:
    # --> Trigger
    def __init__(self):
        self.xyz         = requests.Session()
        self.token_eaag  = open('login/token_eaag.json','r').read()
        self.token_eaab  = open('login/token_eaab.json','r').read()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        self.pilih()
    # --> Menu Dump
    def pilih(self):
        print('[ Pilih Interaksi Berdasar ]')
        print('[1] React')
        print('[2] Comment')
        print('[3] React + Comment')
        xb = input('Pilih : ')
        print('')
        if   xb in ['1','01','a']: self.pilih2(); self.friendlist(); self.dump(); dump_react();         self.sortir(); unfriend()
        elif xb in ['2','02','b']: self.pilih2(); self.friendlist(); self.dump(); dump_comment();       self.sortir(); unfriend()
        elif xb in ['3','03','c']: self.pilih2(); self.friendlist(); self.dump(); dump_react_comment(); self.sortir(); unfriend()
        else: exit('\nIsi Yang Benar !\n')
    def pilih2(self):
        print('[ Pilih Privasi Post ]')
        print('[1] Semua')
        print('[2] Publik')
        print('[3] Teman')
        print('[4] Hanya Saya')
        xc = input('Pilih : ')
        print('')
        if   xc in ['1','01','a']: self.privacy = 'ALL'         # Semua Privasi
        elif xc in ['2','02','b']: self.privacy = 'EVERYONE'    # Publik
        elif xc in ['3','03','c']: self.privacy = 'ALL_FRIENDS' # Teman
        elif xc in ['4','04','d']: self.privacy = 'SELF'        # Hanya Saya
        else: exit('\nIsi Yang Benar !\n')
    def tempo(self):
        print('[ Postingan Setelah ]')
        print('Format : Tgl-Bln-Thn')
        print('Contoh : 29-10-2022')
        self.tempo = int(input(''))
        print('')
    # --> Execute Dump
    def dump(self):
        global tamp1
        self.tamp1 = []
        tamp1 = self.tamp1
        url = 'https://graph.facebook.com/me/posts?fields=id,created_time,privacy&limit=10000&access_token='+self.token_eaag
        req = self.xyz.get(url,cookies=self.cookie).json()
        if self.privacy == 'ALL': # Semua Privasi
            for x in req['data']: self.tamp1.append(x)
        elif self.privacy == 'EVERYONE': # Publik
            for x in req['data']:
                if x['privacy']['value'] == 'EVERYONE': self.tamp1.append(x)
        elif self.privacy == 'ALL_FRIENDS': # Teman
            for x in req['data']:
                if x['privacy']['value'] == 'ALL_FRIENDS': self.tamp1.append(x)
        elif self.privacy == 'SELF': # Hanya Saya
            for x in req['data']:
                if x['privacy']['value'] == 'SELF': self.tamp1.append(x)
        print('Mendapatkan %s Postingan'%(str(len(tamp1))))
    # --> Dump Friendlist
    def friendlist(self):
        self.tamp3 = []
        url = 'https://graph.facebook.com/me/friends?fields=id,name&limit=5000&access_token=%s'%(self.token_eaab)
        req = self.xyz.get(url,cookies=self.cookie).json()
        try:
            for y in req['data']:
                try:
                    if y['id']+'|'+y['name'] in self.tamp3: pass
                    else:self.tamp3.append(y['id']+'|'+y['name'])
                except Exception as e:continue
        except Exception as e:pass
        print('Mendeteksi %s Teman'%(str(len(self.tamp3))))
    # --> Sortir ID
    def sortir(self):
        global tamp3
        tamp3 = self.tamp3
        for z in tamp2:
            try:self.tamp3.remove(z)
            except Exception as e:pass
        print('Mendeteksi %s Teman Yg Tidak Pernah Berinteraksi\n'%(str(len(self.tamp3))))

class dump_react:
    def __init__(self):
        global tamp2
        self.tamp2       = []
        tamp2            = self.tamp2
        self.xyz         = requests.Session()
        self.token_eaag  = open('login/token_eaag.json','r').read()
        self.token_eaab  = open('login/token_eaab.json','r').read()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        for x in tamp1:
            url = 'https://graph.facebook.com/%s/reactions?limit=10000&access_token=%s'%(x['id'],self.token_eaab)
            self.main_dump(url)
        print('')
    def main_dump(self,url):
        req = self.xyz.get(url,cookies=self.cookie).json()
        try:
            for y in req['data']:
                try:
                    if y['id']+'|'+y['name'] in self.tamp2: pass
                    else:
                        self.tamp2.append(y['id']+'|'+y['name'])
                        print('\rMendeteksi %s Interaksi'%(str(len(tamp2))),end='');sys.stdout.flush()
                except Exception as e:continue
        except Exception as e:pass

class dump_comment:
    def __init__(self):
        global tamp2
        self.tamp2       = []
        tamp2            = self.tamp2
        self.xyz         = requests.Session()
        self.token_eaag  = open('login/token_eaag.json','r').read()
        self.token_eaab  = open('login/token_eaab.json','r').read()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        for x in tamp1:
            url = 'https://graph.facebook.com/%s/comments?limit=10000&access_token=%s'%(x['id'],self.token_eaab)
            self.main_dump(url)
        print('')
    def main_dump(self,url):
        req = self.xyz.get(url,cookies=self.cookie).json()
        try:
            for y in req['data']:
                try:
                    if y['from']['id']+'|'+y['from']['name'] in self.tamp2: pass
                    else:
                        self.tamp2.append(y['from']['id']+'|'+y['from']['name'])
                        print('\rMendeteksi %s Interaksi'%(str(len(tamp2))),end='');sys.stdout.flush()
                except Exception as e:continue
        except Exception as e:pass

class dump_react_comment:
    def __init__(self):
        global tamp2
        self.tamp2       = []
        tamp2            = self.tamp2
        self.xyz         = requests.Session()
        self.token_eaag  = open('login/token_eaag.json','r').read()
        self.token_eaab  = open('login/token_eaab.json','r').read()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        for x in tamp1:
            url = 'https://graph.facebook.com/%s/reactions?limit=10000&access_token=%s'%(x['id'],self.token_eaab)
            self.main_dump1(url)
        for x in tamp1:
            url = 'https://graph.facebook.com/%s/comments?limit=10000&access_token=%s'%(x['id'],self.token_eaab)
            self.main_dump2(url)
        print('')
    def main_dump1(self,url):
        req = self.xyz.get(url,cookies=self.cookie).json()
        try:
            for y in req['data']:
                try:
                    if y['id']+'|'+y['name'] in self.tamp2: pass
                    else:
                        self.tamp2.append(y['id']+'|'+y['name'])
                        print('\rMendeteksi %s Interaksi'%(str(len(tamp2))),end='');sys.stdout.flush()
                except Exception as e:continue
        except Exception as e:pass
    def main_dump2(self,url):
        req = self.xyz.get(url,cookies=self.cookie).json()
        try:
            for y in req['data']:
                try:
                    if y['from']['id']+'|'+y['from']['name'] in self.tamp2: pass
                    else:
                        self.tamp2.append(y['from']['id']+'|'+y['from']['name'])
                        print('\rMendeteksi %s Interaksi'%(str(len(tamp2))),end='');sys.stdout.flush()
                except Exception as e:continue
        except Exception as e:pass

class unfriend:
    def __init__(self):
        self.loop = 0
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        for fg in tamp3:
            id   = fg.split('|')[0]
            name = fg.split('|')[1]
            url  = 'https://mbasic.facebook.com/removefriend.php?friend_id=%s'%(id)
            self.scrap1(url,id,name)
    def scrap1(self,url,id,name):
        with requests.Session() as xyz:
            req = bs(xyz.get(url,cookies=self.cookie).content,'html.parser')
            fom = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                'confirm' : 'Konfirmasi'}
            nek = 'https://mbasic.facebook.com%s'%(fom['action'])
            pos = xyz.post(nek,data=dat,cookies=self.cookie)
            if '<Response [200]>' in str(pos):
                self.loop += 1
                print('\r[Dihapus] %s | %s          '%(id,name))
            else:
                print('\r[ Gagal ] %s | %s          '%(id,name))
            print('\rBerhasil Menghapus %s Teman'%(str(self.loop)),end='');sys.stdout.flush()


                
                
                
if __name__=='__main__':
	pilihan() 