#!/usr/bin/python3
# This Programm Write by Mr.nope
# Brecon v1.3.0
import os
import time
import sys
import platform
try:
    from colorama import Fore,init
    init()
except ImportError:
    os.system("pip3 install colorama")
try:
    from googlesearch import search
except ImportError:
    os.system("pip install googlesearch-python")
    os.system("pip3 install googlesearch-python")
system = platform.uname()[0]
run_Err = "\nPlease, Run This Programm on Linux, Windows, MacOS\n"
End = '\033[0m'
banner = Fore.LIGHTGREEN_EX + """
██████  ██       █████   ██████ ██   ██      ██████  ███████  ██████  ██████  ███    ██ 
██   ██ ██      ██   ██ ██      ██  ██       ██   ██ ██      ██      ██    ██ ████   ██  """ + Fore.RED + "Version: " + Fore.YELLOW + "1.4.0" + Fore.LIGHTGREEN_EX + """
██████  ██      ███████ ██      █████  █████ ██████  █████   ██      ██    ██ ██ ██  ██ 
██   ██ ██      ██   ██ ██      ██  ██       ██   ██ ██      ██      ██    ██ ██  ██ ██ 
██████  ███████ ██   ██  ██████ ██   ██      ██   ██ ███████  ██████  ██████  ██   ████ 
                                                                                        """ + End
line = "\n----------------------------------\n"
def title():
    if system == 'Linux':
        os.system("printf '\033]2;Black-Recon\a'")
    elif system == 'Windows':
        os.system("title Black-Tool")
    else:
        print(run_Err)
        sys.exit()
def cls():
    if system == 'Linux':
        os.system("clear")
    elif system == 'Windows':
        os.system("cls")
    else:
        print(run_Err)
        sys.exit()
def main():
    title()
    cls()
    print(banner)
    web = input(Fore.GREEN + "\nEnter: " + End)
    time.sleep(1)
    for http in search(web):
        print(Fore.BLUE + line + Fore.YELLOW + http + Fore.BLUE + line + End)
        try1()
def try1():
    try_again = input("\nDo you want to try again? [y/n] ")
    if try_again == 'y':
        main()
    elif try_again == 'n':
        try2()
    else:
        try1()
def try2():
    try_to_exit = input("\npress Enter...")
    if try_to_exit == '':
        ext()
    else:
        ext()
def ext():
    cls()
    print("Exiting...")
    sys.exit()
if __name__ == '__main__':
    try:
        try:
            main()
        except KeyboardInterrupt:
            print("\nCtrl + C")
            print("\nExiting...")
            sys.exit()
    except EOFError:
        print("\nCtrl + D")
        print("\nExiting...")
        sys.exit()
