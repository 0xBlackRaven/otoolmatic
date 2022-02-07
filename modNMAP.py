from datetime import datetime
import os,argparse,re,sys
dir = ""
ip_target = ""
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
def scan(parameters,ip_target):
    print(bcolors.BOLD +"[INFO] Start of the information gathering phase."+bcolors.ENDC)
    print(bcolors.BOLD +"[INFO] Scanning",ip_target,"."+bcolors.ENDC)
    os.system(f"nmap {parameters}")
    print(bcolors.OKGREEN+"[SUCCESS] Scan completed."+bcolors.ENDC)

def newdir():
    global dir
    date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    dir = date+"-SCAN"
    os.system(f"mkdir ./{dir}/")
    return dir

def parameters(ip_target,dir):
    print(bcolors.WARNING+"If you are in a production/firewall protected environment, don't forget to put delay in the options! (--scan-delay)"+bcolors.ENDC)
    print(bcolors.BOLD +"[INFO] Leave the next information blank if you want the default settings"+bcolors.ENDC)
    option_nmap = input(bcolors.UNDERLINE+"What option do you want for nmap (-A and -oA are already included for the correct running of the app)?"+bcolors.ENDC)
    parameters = option_nmap+" "+ip_target+" "+f"-oA ./{dir}/otomatic_nmap"+" "+"-A"
    return parameters
def args():
    global ip_target
    parser = argparse.ArgumentParser(add_help=True, description='Otomatic Scanning Tool')
    required_args = parser.add_argument_group("Required argument")
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target_ip",help="Specify the target IP", required=True)
    args = parser.parse_args()
    ip_target=args.target_ip

    check = re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",ip_target)
    if check:
        ip = check.group()
    else:
        sys.exit(bcolors.FAIL + "[ERROR] Please fill the target field correctly."+bcolors.ENDC)
    return ip_target

def main():
    dir = newdir()
    ip_target = args()
    parameter = parameters(ip_target,dir)
    scan(parameter,ip_target)
    return ip_target,dir
