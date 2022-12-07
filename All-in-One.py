#!/usr/bin/python3
import os
import time
import sys

os.system("clear")

print('''\033[91m 
╔═╦═╗    .╔╗     ╔═╦═╦╗  ╔╗
║╬║═╬╦╦═╣╚╦═╗║║║║╠╬═╣╠╦═╦╦╗
║╔╬═║║║═╣║║╬║║║║║║║═╣═╣╩╣║║
╚╝╚═╬╗╠═╩╩╩═╝╚╩═╩╩╩═╩╩╩═╬╗║
      .╚═╝                           ╚═╝
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

print (''' \033[95m
+--------------------------------------+
| This Tool Install Main Packages |
+--------------------------------------+
| Tool created By Psycho Mickey | version 1|
+--------------------------------------+''')

slowprint(''' \033[93m
[01] python
[02] python2
[03] lolcat
[04] python3
[05] php
[06] cowsay
[07] git
[08] perl
[09] bash
[10] nano
[11] curl
[12] sudo
[13] openssh
[14] wget
[15] ruby''')
slowprint('''\033[96m
This Command for access Storage in Termux
[00] termux-setup-storage''')
print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update && upgrade")
os.system ("pkg install python -y")
os.system ("pkg install python2 -y")
os.system ("pkg install php -y")
os.system ("pkg install python3 -y")
os.system ("pkg install git -y")
os.system ("pkg install perl -y")
os.system ("pkg install bash")
os.system ("pkg install cowsay")
os.system ("pkg install sudo -y")
os.system ("pkg install ruby -y")
os.system ("pkg install nano -y")
os.system ("pkg install openssh -y")
os.system ("pkg install wget -y")
os.system ("pkg install lolcat -y")



def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
slowprint(
"\033[95m         +-------------------------------------------------+")
print('''\033[95m
                                         _      _
                ___ ___  _ __ ___  _ __ | | ___| |_ ___
               / __/ _ \| '_ ` _ \| '_ \| |/ _ \ __/ _ \
              | (_| (_) | | | | | | |_) | |  __/ ||  __/
               \___\___/|_| |_| |_| .__/|_|\___|\__\___|
                                  |_|
''')
slowprint("        +-------------------------------------------------+")
