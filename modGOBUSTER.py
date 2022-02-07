import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def scan(ip_target,port):
    print(bcolors.OKBLUE+"\nInitialization of gobuster in progress"+bcolors.ENDC)
    print(bcolors.WARNING+"If you are in a production/firewall protected environment, don't forget to put delay in the options! (--delay)"+bcolors.ENDC)
    path_wordlist = input("What is the path of the wordlist you want to use ? \n")
    print(bcolors.BOLD +"[INFO] Leave the next information blank if you want the default settings"+bcolors.ENDC)
    option_gobuster = input(bcolors.UNDERLINE+"What option do you want for gobuster ?"+bcolors.ENDC)
    print(f"[INFO] Start of the scan.")
    os.system(f"gobuster -u http://{ip_target}:631 -w {path_wordlist}")
    print(bcolors.OKGREEN+"[SUCCESS] Scan completed."+bcolors.ENDC)

def main(ip_target,port):
    scan(ip_target,port)
