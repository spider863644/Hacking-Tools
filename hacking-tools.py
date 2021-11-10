import time as t
import os
x = "\033[1;91mChoose a valid option!"
t.sleep(3)
print("""\033[1;91mDisclaimer:Use this tool  for educational purposes only

Spider Anongreyhat Won't be responsible for any misuse of this tool!
""")
t.sleep(8)
os.system("clear")
t.sleep(4)
print("""\x1b[1;92m
                   HACKING TOOLS""")
t.sleep(5)
print("""
============================================================

                LINUX DISTRIBUTION
                
============================================================
""")
t.sleep(4)
def loop():
    print("""\x1b[1;92m
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[+]Tool name: Hacking Tools
[+]Creator: Spider Anongreyhat aka Anonspidey
[+]Team:Termuxhackz Society
[+]WhatsApp:+2349052863644
[+]GitHub:https://github.com/spider863644
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
""")
    t.sleep(3)
    name = input("Username: ")
    pwd = input("Password: ")
    t.sleep(4)
    print("Checking Username and Password...")
    t.sleep(7)
    if name == "Hacking Tools" and pwd == "Termuxhackz Society":
      print("Successfully logged in as Hacking Tools")
      t.sleep(4)
    else:
      print("\033[1;91m Incorrect Username or Password!")
      t.sleep(5)
      print("Follow me on GitHub for username and password and message me WhatsApp(+2349052863644)With screenshot")
      t.sleep(6)
      os.system("xdg-open https://github.com/spider863644")
      os.system("clear")
      loop()
loop()
  
print("<<<<<>>>>>>>>>>>>>>>>CHOOSE A TOOL TO RUN:<<<<<<<<<<>>>>>>>")
print("""
[1]Social Media Hack
[2]CCTV Hacking
[3]Information Gathering
[4]Website Hacking
[5]Update
""")
choose = input("~#: ")
os.system("clear")
if choose == "1":
  print("""CHOOSE A METHOD FOR HACKING
  [1]Phishing
  [2]Cracking/Bruteforcing
  [3]Others
     """)
  p = input("~#: ")
  os.system("clear")
  if p == "1":
    os.system("""
    sudo apt update
    sudo apt upgrade
    git clone https://github.com/Termuxhackz/anonphisher
    cd anonphisher
    bash anonphisher.sh
     """)
  elif p == "2":
    print("""CHOOSE A SOCIAL ACCOUNT TO BRUTEFORCE/CRACK
    [1] Facebook
    [2] Instagram
    """ )
    b = input("~#: ")
    os.system("clear")
    if b == "1":
      os.system("""
      sudo apt update
      sudo apt upgrade
      git clone https://github.com/mkdirlove/FBTOOL
      cd FBTOOL
      python2 FBTOOL.py
      """)
    elif b == "2":
      print("Installing requirements...")
      t.sleep(4)
      os.system("""apt-get update -y
      apt-get upgrade -y
      apt install pip
      pip install lolcat""")
      t.sleep(2)
      print("Running tools")
      os.system("""git clone https://github.com/evildevill/instahack
      cd instahack
      pip install -r requirements.txt
      bash setup.sh
      bash instahack.sh""")
    else:
      print(x)
      os.system("python3 hacking-tools.py")
  elif p == "3":
    print("Installing Metasploit-framework")
    t.sleep(3)
    os.system("""sudo apt update 
    sudo apt upgrade
    sudo apt install metasploit-framework""")
    print("Running..")
    t.sleep(3)
    os.system("msfconsole")
  else:
    print(x)
    os.system("python3 hacking-tools.py")
elif choose == "2":
  print("""[1]Target and Random CCTV Hack
  [2]Random CCTV Hack
  [3]Shodan Search Engine
  """)
  cc = input(">>>>Choose an option<<<<")
  if cc == "1":
    print("Installing requirements...")
    t.sleep(4)
    os.system("""sudo apt update
    sudo apt upgrade
    sudo apt install pip2
    pip3 install git+https://github.com/EntySec/CamOver
    """)
    print("Running tool...")
    t.sleep(3)
    print("Kindly read how to use this tool below!")
    t.sleep(5)
    os.system("camover")
  elif cc == "2":
    print("Installing Requirements...")
    t.sleep(4)
    os.system("""apt update
    
    apt upgrade
    
    apt install git
    
    apt install python
    
    apt inatall python2
    
    apt install figlet
    
    git clone https://github.com/U-danbaiwa/CCTV-HACKING.git
    """)
    print("running tool")
    os.system("""
    cd
    
    ls
    
    cd CCTV-HACKING
    
    python cctv-hack.py
   """) 
  else:
    print(x)
    os.system("python3 hacking-tools.py")
elif choose == "3":
  print("""
  [1]Website Information Gathering
  [2]Phone Number Information Gathering
  [3]Facebook Information Gathering
  [4]Instagram Information Gathering
  [5]Email Osint
  [6]Phone Number tracking
  [7]Phone Tracker
  [8]Osint-Framework
  """)
  inn = input(">>><Choose an option<<<< ")
  if inn == "1":
    print("Installing Requirements...")
    t.sleep(5)
    os.system("""
    apt update
    apt upgrade
    apt install php
    git clone https://github.com/Tuhinshubhra/RED_HAWK
    cd RED_HAWK
    """)
    print("""Running...""")
    t.sleep(3)
    os.system("php rhawk.php")
  elif inn == "2":
    print("Installing Requirements...")
    t.sleep(5)
    os.system("""
    apt update
    apt upgrade
    apt install pip
    git clone https://github.com/la-deep-web/Phoneinfoga
    cd Phoneinfoga
    python3 -m pip install -r requirements.txt
    """)
    print("Running..")
    t.sleep(4)
    os.system("python3 phoneinfoga.py --help")
  elif inn == "3":
    print("Installing requirements...")
    t.sleep(4)
    os.system("""
    apt update
    apt upgrade
    git clone https://github.com/xHak9x/fbi.git
    cd fbi
    pip2 install -r requirements.txt
    """)
    print("Running...")
    t.sleep(5)
    os.system("python2 fbi.py")
  elif inn == "4":
    print("Installing requirements...")
    t.sleep(4)
    os.system("""apt update
    apt upgrade
    git clone https://github.com/th3unkn0n/osi.ig.git && cd osi.ig
    python3 -m pip install -r requirements.txt
    """)
    print("""running...
    
    READ THE INFORMATION BELOW CAREFULLY""")
    t.sleep(5)
    os.system("python3 main.py -h")
  elif inn == "5":
    print("Installing Requirements...")
    t.sleep(6)
    os.system("""
    apt update && apt upgrade
    apt install go
    git clone https://github.com/alpkeskin/mosint.gitIU
    cd mosint
    pip3 install -r requirements.txt
    """)
    print("Type -h to see how to use this tool")
  elif inn == "6":
    print("Installing Requirements...")
    t.sleep(4)
    os.system("""
    apt update
    apt upgrade
    apt install pip2
    pip2 install requests
    
    pip2 install mechanize
    
    git clone https://github.com/ShuBhamg0sain/phone-number-tracker
    
    cd phone-number-tracker
    """)
    print("Running...")
    t.sleep(3)
    os.system("python2 tracker.py number")
  elif inn == "7":
    print("Installing requirements...")
    t.sleep(5)
    os.system("""
    apt update
    apt upgrade
    git clone https://github.com/TermuxHackz/TrackIp
    cd TrackIp
    """)
    print("Running...")
    os.system("bash trackip.sh")
  elif inn == "8":
    print("Redirecting Osint-framework")
    t.sleep(7)
    os.system("""
    xdg-open https://osintframework.com
    """)
  else:
    print(x)
    os.system("python3 hacking-tools.py")
elif choose == "4":
  os.system("""apt update
  sudo apt install sqlmap
  sqlmap --help""")
elif choose == "5":
  print("Updating tool...")
  t.sleep(5)
  os.system("""rm -f -r Hacking-Tools
  git clone https://github.com/spider863644/Hacking-Tools
  """)
  print("""Type:
  cd
  cd Hacking-Tools
  python3 hacking-tools.py
  """)
else:
  print(x)