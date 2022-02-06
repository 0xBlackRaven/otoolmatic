def scan(parameters):
      print(bcolors.BOLD +"[INFO] Start of the information gathering phase."+bcolors.ENDC)
      print(bcolors.BOLD +"[INFO] Scanning",ip_target,"."+bcolors.ENDC)
      os.system(f"nmap {parameters}")
      print(bcolors.OKGREEN+"[INFO] Scan completed."+bcolors.ENDC)

def parameters():
    date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    dir = date+"-SCAN"
    os.system(f"mkdir ./{dir}/")
    parser = argparse.ArgumentParser(add_help=True, description='Otomatic Scanning Tool')
    required_args = parser.add_argument_group("Required argument")
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target_ip",help="Specify the target IP", required=True)
    args = parser.parse_args()
    ip_target=args.target_ip
    option_nmap = input("What option do you want for nmap (-A and -oA are already included for the correct running of the app)?")
    parameters = option_nmap+" "+ip_target+" "+f"-oA ./{dir}/otomatic_nmap"+" "+"-A"
    return parameters


def main():
    parameters()
    scan(parameters)
