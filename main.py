# AutoSetup for GTPS, Created by Aerial#1337

# Import library
from src.core.setup import *

def main():
    print("""
    ================================
    [?] GrowtopiaServer - Auto Setup
    [/] Created by Aerial
    ================================
    """)
    start = input("Are you sure you want to start? (Y/n) : ")
    if start == "y":
        choice = input("Download XAMPP? (Y/n) : ")
        if choice == "y":
            Setup.download_xampp()
        else:
            return
        choice2 = input("Turn off firewall (Y/n) : ")
        if choice2 == "y":
            Setup.turn_off_firewall()
        else:
            return
        choice3 = input("Add firewall port (Y/n) : ")
        if choice3 == "y":
            port = input("UDP Port : ")
            Setup.add_firewall_port(port)
        else:
            return
        choice4 = input("Create server_data and host (Y/n) : ")
        if choice4 == "y":
            ip = input("Server IP : ")
            gtport = input("Server Port : ")
            maint = input("Maintenance Message : ")
            Setup.create_host(ip)
            Setup.create_server_data(ip, gtport, maint)
        else:
            return

if __name__ == "__main__":
    main()