import os, sys
from colorama import *
import wget
import time
init()

class Setup:
    def download_xampp():
        print(f"{Fore.WHITE}[ {Fore.YELLOW}LOADING {Fore.WHITE}] Downloading XAMPP...")
        time.sleep(3)
        url = "https://www.apachefriends.org/xampp-files/7.4.27/xampp-windows-x64-7.4.27-2-VC15-installer.exe"
        wget.download(url)
        print(f"\n{Fore.WHITE}[ {Fore.GREEN}INFO {Fore.WHITE}] XAMPP Downloaded!")
    
    def create_server_data(ip, port, maint):
        print(f"{Fore.WHITE}[ {Fore.YELLOW}LOADING {Fore.WHITE}] Creating server_data.php")
        time.sleep(3)
        file = open("./src/result/server_data.php", "w")
        file.write(f"server|{ip}\nport|{port}\ntype|1\n#maint|{maint}\n\nbeta_server|127.0.0.1\nbeta_port|17091\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001")
        file.close()
        print(f"{Fore.WHITE}[ {Fore.GREEN}INFO {Fore.WHITE}] server_data.php has been created!")

    def turn_off_firewall():
        print(f"{Fore.WHITE}[ {Fore.YELLOW}LOADING {Fore.WHITE}] Turning off firewall...")
        time.sleep(3)
        os.system("netsh Advfirewall set privateprofile state off")
        os.system("netsh Advfirewall set publicprofile state off")
        print(f"{Fore.WHITE}[ {Fore.GREEN}INFO {Fore.WHITE}] Firewall has been turned off!")

    def add_firewall_port(port):
        print(f"{Fore.WHITE}[ {Fore.YELLOW}LOADING {Fore.WHITE}] Adding HTTP and Game port!")
        time.sleep(3)
        os.system("netsh firewall add portopening TCP 80 80")
        os.system(f"netsh firewall add portopening UDP {port} {port}")
        print(f"{Fore.WHITE}[ {Fore.GREEN}INFO {Fore.WHITE}] Added HTTP and Game port!")

    def create_host(ip):
        host = open("./src/result/host.txt", "w")
        host.write(f"{ip} growtopia1.com\n{ip} growtopia2.com")
        print(f"{Fore.WHITE}[ {Fore.GREEN}INFO {Fore.WHITE}] Host created!")