import os, modNMAP, modVULN
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
def main():
    print(bcolors.BOLD+"[INFO] A report file is being created."+bcolors.ENDC)
    os.system("touch ./{dir}/report.txt")
    file = open("./{dir}/report.txt", "a")
    file.write("\nThe NMAP scan found x open port ")
    if modVULN.http_discovered == 1:
        file.write("\nAn HTTP port has been discovered at the port {modVULN.http_port}.")
    elif modVULN.http_discovered > 1:
        file.write("\n{http_discovered} HTTP ports has been discovered. More information here on the otomatic_nmap.nmap file.")
    else:
        pass
    file.close()
    print(bcolors.BOLD+"[INFO] The report file has just been created, you can check it at the following path: ./{dir}/report.txt"+bcolors.ENDC)