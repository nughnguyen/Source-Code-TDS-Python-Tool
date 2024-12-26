#Author: Nguyen Quoc Hung (NughNguyen)
#©️  Do Not Reup File
import requests,os,sys, time
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
import json
import requests
import time
from time import strftime
import os
import requests
import urllib.parse
from time import strftime
import os
from datetime import datetime
from time import sleep, strftime
import datetime
#Color
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
#Đánh Dấu Bản Quyền
Nugh_Tool = trang + " " + trang + "[" + do + "+_+" + trang + "] " + trang + "=> "
quochung = trang + " " + trang + "[" + do + "÷_+" + trang + "] " + trang + "=> "

# Thanh phân cách
thanh = trang + "-------------------------------------------------------------------------"

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Gọi hàm để xóa màn hình
clear_screen()

# Định nghĩa các thanh xấu và đẹp
thanh_xau=trang+'~'+do+'['+vang+'⟨⟩'+do+'] '+trang+'➩  '+xanhnhat
thanh_dep=trang+'~'+do+'['+xanh_la+'✓'+do+'] '+trang+'➩  '+xanhnhat
# Hàm lấy địa chỉ IP từ URL
def get_ip_from_url(url):
     response = requests.get(url)
     ip_address = socket.gethostbyname(response.text.strip())
     return ip_address
     return "127.0.0.1"
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url
import os
import requests
from time import strftime
now = datetime.datetime.now()
thu = now.strftime('%A')
ngay_hom_nay = now.strftime('%d')
thang_nay = now.strftime('%m')
nam_ = now.strftime('%Y')
now = datetime.datetime.now()
gio_hien_tai = now.strftime('%H:%M:%S')
System.Clear()
System.Title("NughToolVip")
System.Size(170, 60)
banner = r"""


                            © Copyright NughNguyen          

 ███╗   ██╗██╗   ██╗ ██████╗ ██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗       ║
 ████╗  ██║██║   ██║██╔════╝ ██║  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║       ║ Author: Nguyễn Quốc Hưng
 ██╔██╗ ██║██║   ██║██║  ███╗███████║       ██║   ██║   ██║██║   ██║██║       ║ Zalo: 0923056036
 ██║╚██╗██║██║   ██║██║   ██║██╔══██║       ██║   ██║   ██║██║   ██║██║       ║ Youtube: NughNguyen
 ██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗  ║ Version: 1.0
 ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝  ║
                                                                
                                                                                 
                             ENTER ĐỂ VÀO TOOL                                
"""
Anime.Fade(Center.Center(banner), Colors.rainbow, Colorate.Vertical, enter=True)
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_key_to_file(key, filename='NUGHTOOL-key.txt'):
    with open(filename, 'w') as file:
        file.write(str(key))


def load_key_from_file(filename='NUGHTOOL-key.txt'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read().strip()
    return None





def main():
    clear_screen()

if __name__ == "__main__":
    main()
banner = ''' 
  \x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;46m═╗
  \033[1;31m║                                        \033[1;33m║ \x1b[38;5;207mAuthor: \033[1;37mNguyễn Quốc Hưng \033[1;31m║                           
  \033[1;36m║  ███╗   ██╗██╗   ██╗ ██████╗ ██╗  ██╗  \033[1;33m║ \x1b[38;5;207mFB: \x1b[38;5;46mfb.com/hungnq188.2k5 \033[1;36m║                          
  \033[1;32m║  ████╗  ██║██║   ██║██╔════╝ ██║  ██║  \033[1;33m║ \x1b[38;5;207mZalo Support: \033[1;37m0923056036 \033[1;32m║
  \033[1;34m║  ██╔██╗ ██║██║   ██║██║  ███╗███████║  \033[1;33m║ \033[1;31mYoutube: \033[1;37m NughNguyen     \033[1;34m║
  \033[1;35m║  ██║╚██╗██║██║   ██║██║   ██║██╔══██║  \033[1;33m║                          \033[1;35m║
  \033[1;31m║  ██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║  \033[1;33m║        \033[0;36mChú Thích:        \033[1;31m║
  \033[0;33m║  ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝  \033[1;33m║      \033[1;37mBạn không ngu,      \033[0;33m║
  \033[1;36m║                                        \033[1;33m║     \033[1;37mDo tôi quá giỏi.     \033[1;36m║
  \x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;46m═╝
 \033[1;32m ═════════════════════════════════════════════════════════════════════
 \033[1;36m                             TOOL VIP v1.0                            
 \033[1;32m ═════════════════════════════════════════════════════════════════════
'''

for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.00130)
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
#thanh_xau= print(f"{red}┌─────┬────────────────────────────────────┬─────────┬─────────┐")
#thanh_dep= print(f"{red}│{vang}      {red}│    {vang}      {red}        │ {vang}STATUS {red} │{vang} VERSION {red}│")
#thanh_cuoi=print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")


#here you can change the color of the text and text that you want to display

Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║  TOOL Trao Đổi Sub  ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('[x.x]➩ Nhập Số [1] TDS TIKTOK MAX SPEED [VIP] \n',Colors.white,interval=0.0001)
Write.Print('[x.x]➩ Nhập Số [2] TDS BẰNG PAGE PRO5 [TẠM] \n',Colors.white,interval=0.0001)
Write.Print('[x.x]➩ Nhập Số [3] TDS FACEBOOK FULL JOD [VIP] \n',Colors.white,interval=0.0001)
Write.Print('[x.x]➩ Nhập Số [4] TDS INSTAGRAM MAX SPEED  [MỚI] \n',Colors.white,interval=0.0001)
Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║ TOOL TƯƠNG TÁC CHÉO ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
print(f'{hong}[x.x]➩ \033[1;32mNhập Số [5]  TTC PRO5 [ỔN] \n')
print(f'{hong}[x.x]➩ \033[1;32mNhập Số [6] TTC INSTAGRAM MAX SPEED  [MỚI] \n')
Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║    TOOL FACEBOOK    ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
print(f'{hong}[x.x]➩ {lam}Nhập Số [0.1] TOOL BUFF VIEW FB BẰNG PRO5 \033[1;31m[BẢO TRÌ]\n')
print(f'{hong}[x.x]➩ {lam}Nhập Số [0.2] TOOL SHARE ẢO FB \033[1;31m[BẢO TRÌ ]\n')
print(f'{hong}[x.x]➩ {lam}Nhập Số [0.3] TOOL NUÔI FB V1 [NGON]\n')
print(f'{hong}[x.x]➩ {lam}Nhập Số [0.4] TOOL NUÔI FB V2 [NGON]\n')
print(f'{hong}[x.x]➩ {lam}Nhập Số [0.5] TOOL LIKE BÀI VIẾT DẠO [NGON]\n')
Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║     TOOL GOLIkE     ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
print(f'{hong}[x.x]➩ \033[1;95mNhập Số [6] TOOL TƯƠNG TÁC CHÉO IG [VIP] \n')
print(f'{hong}[x.x]➩ \033[1;95mNhập Số [7] TOOL GỘP GOLKIE TIKTOK [VIP] \n')
print(f'[x.x]➩ \033[1;95mNhập Số [7.1] TOOL GOLKIE TIKTOK [VIP] \n')
Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║     TOOL TIKTOK     ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
print(f'{hong}[x.x]➩ \033[1;32mNhập Số [10] TOOL BUFF TIKTOK[NGON]\n')
Write.Print('╔═════════════════════╗ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║    TOOL SPAM SMS    ║ \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════╝ \n',Colors.yellow,interval=0.0001,end='\r')
print(f'{hong}[x.x]➩ \033[1;35mNhập Số [12] TOOL SPAM SMS V1[NGON]\n')
import requests


chon = str(input('\033[1;31m[\033[1;3⟨🐢\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;37m: \033[1;33m'))

#change your mocky link here

if chon == '1':
    exec(requests.get('https://run.mocky.io/v3/3554e674-578f-4428-9e13-d7959cc5e855').text)
elif chon == '2':
    exec(requests.get('https://run.mocky.io/v3/08e0a323-54a9-46c2-acb7-b9e110062bec').text)
elif chon == '3':
    exec(requests.get('https://run.mocky.io/v3/07086278-4e93-4923-b039-ce8a0209e4a2').text)
elif chon == '4':
    exec(requests.get('https://run.mocky.io/v3/766563e5-c39b-4312-8d26-aee4349ef839').text)
elif chon == '5':
	exec(requests.get('https://run.mocky.io/v3/355add71-abee-4ffc-a7c3-0bcb2dc55d36').text)
elif chon == '0.3':
	exec(requests.get('https://run.mocky.io/v3/bedc013d-ff2c-4f14-9d75-ee39b817ed64').text)
elif chon == '0.4':
	exec(requests.get('https://run.mocky.io/v3/bc045a0c-312d-43ba-90db-a94ebe9e3dec').text)
elif chon == '6':
	exec(requests.get('https://run.mocky.io/v3/2ab28035-0cb4-400f-b628-f22bfde42cef').text)
elif chon == '0.5':
	exec(requests.get('https://run.mocky.io/v3/c9527dc9-f264-4ecb-a1a3-cc2aac4a667a').text)
elif chon == '10':
	exec(requests.get('https://run.mocky.io/v3/10bf2418-b53a-43f6-98c7-95ca54835c8a').text)
elif chon == '7.1':
	exec(requests.get('https://run.mocky.io/v3/2f095ac9-618d-473c-8891-9ccebabd5be3').text)
elif chon == '7':
	exec(requests.get('https://run.mocky.io/v3/03fe1b39-0b31-4259-90e0-ea1e437c0617').text)
elif chon == '12':
	exec(requests.get('https://run.mocky.io/v3/988e7083-5ebb-461b-a54e-26bce533fbc4').text)
elif chon == '3.1':
	exec(requests.get('accc').text)
else:
    print("Sai Lựa Chọn")
    exit()
    
