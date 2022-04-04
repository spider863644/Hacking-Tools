import time as t
import colorama
from colorama import *
colorama.init(autoreset=True)
import os
x = "Enter a valid option!"
os.system("clear")
print(Fore.RED +"""Warning:Use this tool for educational purposes only
Spider Anongreyhat won't be responsible for any misuse  of this tool!""")
t.sleep(3)
def loop():
    os.system("clear")
    print(Fore.GREEN)
    os.system("figlet Hacking-Tools")
    print(Fore.YELLOW + """
  Tool Name:H4ck1n9 700l 
  Creator:Spider Anongreyhat
  Team:TermuxHackz Society
  Github:https://github.com/spider863644
  WhatsApp:+2349052863644
  """)
    print(Fore.GREEN +Back.RED + "<<<<<<>>>>>>>>>>Tools to Run<<<<<<<<<>>>>>")
    print(Fore.BLUE + """
[1]Social Media Hack
[2]CCTV Hack
[3]Information Gathering
[4]Website Hacking
[5]Update
""")
    print(Fore.GREEN + "Choose a tool to run")
    c = input("~#: ")
    os.system("clear")
    os.system("figlet Hacking-Tools")
    if c == "1":
      print(Fore.BLUE + """
  [1]SET
  [2]Brute force(Facebook)
  [3]Bruteforce(Instagram)
  [4]Hack a random facebook
  [5]Others""")
      c2 = input(Fore.GREEN + "Choose one: " + Style.RESET_ALL)
      os.system("clear")
      if c2 == "1":
        os.system("""sudo apt update
    sudo apt upgrade
    git clone https://github.com/trustedsec/social-engineer-toolkit
    cd social-engineer-toolkit
    pip3 install -r requirements.txt
    python setup.py
    """)
      elif c2 == "2":
        os.system("""sudo apt update
    git clone https://github.com/4anonz/fblookup
    cd fblookup
    gcc fblookup.c -o fblookup -lssl -lcrypto
    ./fblookup
    """)
      elif c2 == "3":
        os.system("""
    sudo apt update
    sudo apt upgrade
    sudo pip install lolcat
    git clone https://github.com/dark-player/igbrute
    bash setup
    bash igbrute.setup""")  
      elif c2 == "4":
        os.system("""
    sudo apt update
    sudo apt upgrade
    git clone https://github.com/MrShadow404/W-Login
    cd w-login
    python2 SHADOW.py""")
      elif c2 == "5":
        print(Fore.YELLOW + "Installing metasploit-Framework...")
        os.system("""sudo apt install metasploit-framework
    msfvenom -h""")
    elif c == "2":
      print(Fore.BLUE + """[1]Target CCTV Hack
  [2]Random CCTV Hack""")
      c3 = input(Fore.GREEN + "Choose a valid one: " + Style.RESET_ALL)
      if c3 == "1":
        os.system("""sudo apt update
    sudo apt install pip2
    pip3 install git+https://github.com/EntrySec/CamOver
    camover""")
      elif c3 == "2":
        os.system("""sudo apt update
    sudo apt install python
    git clone https://github.com/U-dambaiwa/CCTV-HACKING
    cd CCTV-HACKING
    python cctv-hack.py
    """)
    elif c == "3":
      print(Fore.BLUE + """
  [1]Website Information Gathering(WIG)
  [2]Phone Number Information Gathering
  [3]Facebook Information Gathering
  [4]Instagram Information Gathering
  [5]Email Havester
  [6]Phone Number Tracking
  [7]Phone Tracker
  [8]Osint-Framework
  """)
      c4 = input(Fore.GREEN + "Choose an option: " + Style.RESET_ALL)
      os.system("""clear
  """)
      if c4 == "1":
        os.system("""
    sudo apt update
    sudo apt upgarde
    sudo apt install php
    git clone https://github.com/Tuhinshubhra/RED_HAWK
    cd RED_HAWK
    php rhawk.php""")
      elif c4 == "2":
        os.system("""
    sudo apt update
    sudo apt upgarde
    sudo apt install pip
    git clone https://github.com/la-deep-web/Phoneinfoga
    cd Phoneinfoga
    python3 -m pip install -r requirements.txt
    python3 phoneinfoga.py --help""")
      elif c4 == "3":
        os.system("""
    sudo apt update
    sudo apt upgrade
    git clone https://github.com/xHak9x/fbi
    cd fbi
    pip2 install -r requirements.txt
    python2 fbi.py
    """)
      elif c4 == "4":
        os.system("""sudo apt update
    sudo apt upgrade
    git clone https://github.com/th3unkn0n/osi.ig
    cd osi.ig
    python3 -m pip install -r requirements.txt
    python3 main.py -h""")
      elif c4 == "5":
        os.system("""sudo apt update
    sudo apt upgrade
    sudo apt install go
    git clone https://github.com/alpkeskin/mosint
    cd mosint
    pip3 install -r requirements.txt
    """)
        print(Fore.YELLOW + """
    
    Type -h to see how to use this tool""")
      elif c4 == "6":
        os.system("""sudo apt update
    sudo apt install pip2
    sudo pip2 install requests
    sudo pip2 install mechanize
    git clone https://github.com/ShuBhamg0sain/phone-nuber-tracker
    cd phone-number-tracker
    clear""")
        print(Fore.RED + """WARNING!:Phone-number-tracker logins are below coz u will be ask
    Tool Name:tracker
    password:g0sain
    
    
    If its incorrect,kindly find Shubamg0sain""")
        t.sleep(7)
        os.system("python2 tracker.py")
      elif c4 == "7":
        os.system("""
    sudo apt update
    git clone https://github..com/TermuxHackz/TrackIp
    cd TrackIp
    bash trackip,sh""")
      elif c4 == "8":
        print("redirecting to osint-framework")
        t.sleep(3)
        os.system("xdg-open https://osintframework.com")
        loop()
    elif c == "4":
      os.system("""sudo apt update
  sudo apt install sqlmap
  sqlmap -h""")
    elif c == "5":
      print(Fore.YELLOW + "Updating hacking tools...")
      os.system("""
  rm -f -r Hacking-Tools
  git clone https://github.com/spider863644/Hacking-Tools""")
      print(Fore.BLUE + """
  type:
  cd
  cd Hacking-Tools
  python3 hacking-tools.py""")
    else:
      print(Fore.RED + """
      Invalid option!
  choose a valid one""")
      t.sleep(2)
      loop()
loop()