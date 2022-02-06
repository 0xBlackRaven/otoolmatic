#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author             : @BlackRaven
# Date created       : 4 Feb 2022

import threading,re,time,sys,os,time,argparse
from argparse import ArgumentParser
from datetime import datetime

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

date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
dir = date+"-SCAN"
os.system(f"mkdir ./{dir}/")
parser = argparse.ArgumentParser(add_help=True, description='Otomatic Scanning Tool')
parser.add_argument("-pmin", "--port-min", dest="port_min", help="Select the minimum port")
parser.add_argument("-pmax", "--port-max", dest="port_max", help="Select the maximum port")
required_args = parser.add_argument_group("Required argument")
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", dest="target_ip",help="Specify the target IP", required=True)
args = parser.parse_args()
ip_target=args.target_ip




print("              ,---------------------------,")
print("              |  /---------------------\  |")
print("              | |                       | |")
print("              | |     Otomatic          | |")
print("              | |      Tool             | |")
print("              | |       By BlackRaven   | |")
print("              | |     Version: 1.1      | |")
print("              |  \_____________________/  |")
print("              |___________________________|")
print("            ,---\_____     []     _______/------,")
print("          /         /______________\           /|")
print("        /___________________________________ /  | ___")
print("        |                                   |   |    )")
print("        |  _ _ _                 [-------]  |   |   (")
print("        |  o o o                 [-------]  |  /    _)_")
print("        |__________________________________ |/     /  /")
print("    /-------------------------------------/|      ( )/")
print("  /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /")
print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(bcolors.WARNING +"Do not use this tool to attack, monitor or enter any computer / network / device that does not belong to you or for which you do not have authorization to perform the above. \nI take no responsibility for your actions."+ bcolors.ENDC)

def scan(parameters):
    os.system(f"nmap {parameters}")

check = re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",ip_target)

if check:
    ip = check.group()
else:
    sys.exit(bcolors.FAIL + "[ERROR] Please fill in the target field correctly."+bcolors.ENDC)

option_nmap = input("What option do you want for nmap (-A and -oA are already included for the correct running of the app)?")
parameters = option_nmap+" "+ip_target+" "+f"-oA ./{dir}/otomatic_nmap"+" "+"-A"
print(bcolors.BOLD +"[INFO] Start of the information gathering phase."+bcolors.ENDC)
print(bcolors.BOLD +"[INFO] Scanning",ip_target,"."+bcolors.ENDC)
scan(parameters)
print(bcolors.GREEN+"[INFO] Scan completed."+bcolors.ENDC)

content = str(open(f"./{dir}/otomatic_nmap.nmap"))

check2 = re.match(r"^([0-9]{1,5}\/)$",content)
