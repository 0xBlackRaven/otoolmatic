import re,requests,time
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
def findports(dir):
    a=0
    with open(f"./{dir}/otomatic_nmap.nmap") as f:
        for line in f:
            match = re.search('(\d{1,5})\/(tcp|udp)[ \t]+open[ \t]+(\S+)[ \t]+(.*)', line)
            if match:
                print(bcolors.BOLD+"\n[INFO] The port",match.group(1),"is open."+bcolors.ENDC)
                print(bcolors.BOLD+"[INFO] The protocol used is",match.group(2)+bcolors.ENDC)
                print(bcolors.BOLD+"[INFO] The service used is",match.group(4)+bcolors.ENDC)
                services = match.group(4)
                serv = services
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                snyk_url = f"https://security.snyk.io/search?q={services}"
                snyk = requests.get(snyk_url,headers=headers)
                print(bcolors.BOLD+f"\n[INFO] Search for vulnerability in this service: {services}"+bcolors.ENDC)
                for lines in snyk.iter_lines():
                    pat = re.search("(No results found)", snyk.text)
                    if pat:
                        a+=1
                        pass
                    else:
                        print(bcolors.OKGREEN+"[SUCCESS] Snyk found a vulnerability at the following url",snyk_url+bcolors.ENDC)
                if a > 0:
                    serv = serv.replace(" ","-")
                    print(bcolors.FAIL+f"[FAIL] No vulnerability uncovered for the service {services}"+bcolors.ENDC)
                    print(bcolors.BOLD+f"You should search on google, because a false negative is always possible: https://www.google.com/search?q={serv}+vulnerabilities"+bcolors.ENDC)
                    a-=1
            else:
                pass
def main(dir):
    findports(dir)
