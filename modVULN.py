#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author             : @BlackRaven
# Date created       : 4 Feb 2022
import re,requests,time,modGOBUSTER
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
def portsvuln(dir,ip_target):
    with open(f"./{dir}/otomatic_nmap.nmap") as f:
        for line in f:
            match = re.search('(\d{1,5})\/(tcp|udp)[ \t]+open[ \t]+(\S+)[ \t]+(.*)', line)
            if match:
                print(bcolors.BOLD+"\n[INFO] The port",match.group(1),"is open."+bcolors.ENDC)
                print(bcolors.BOLD+"[INFO] The protocol used is",match.group(2)+bcolors.ENDC)
                print(bcolors.BOLD+"[INFO] The service used is",match.group(4)+bcolors.ENDC)
                port = match.group(1)
                services = match.group(4)
                if match.group(3).lower() == "http" or match.group(3).lower() == "https":
                    print(bcolors.BOLD +f"[INFO] {match.group(3)} service detected on port {match.group(1)}."+bcolors.ENDC)
                    good_answer = True
                    while good_answer:
                        answer = input(bcolors.UNDERLINE+"Do you want to perform a gobuster on this service? y/n \n"+bcolors.ENDC)
                        if answer == "y":
                            modGOBUSTER.main(ip_target,port)
                            good_answer = False
                        elif answer == "n":
                            print(bcolors.WARNING+"[INFO] The scan will not be performed."+bcolors.ENDC)
                            good_answer = False
                        else:
                            print(bcolors.FAIL+"[ERROR] Please answer with y or n."+bcolors.ENDC)
                serv = services
                serv = serv.replace(" ","")
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                cve_url = f"https://www.cvedetails.com/google-search-results.php?q={serv}&sa=Search"
                snyk_url = f"https://security.snyk.io/search?q={serv}"
                exploitdb_url = f"https://www.exploit-db.com/search?q={serv}"
                rapid7_url = f"https://www.rapid7.com/db/?q={serv}"
                nist_url = f"https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query={serv}&search_type=all&isCpeNameSearch=false"
                print(bcolors.BOLD+f"[INFO] Research proposal on vulnerability databases for {services}:"+bcolors.ENDC+f" \nCVE Details: {cve_url}\nSnyk: {snyk_url}\nExploit-DB: {exploitdb_url}\nRapid7: {rapid7_url}\nNVD (National Vulnerability Database): {nist_url}")
            else:
                pass
def main(dir,ip_target):
    portsvuln(dir,ip_target)
