

from bs4 import BeautifulSoup
import sys, optparse, socket, os
from colorama import Fore, Back, Style
import urllib3
import certifi
import threading
from socket import *
import time
import scan_ports



def webreq(server):
    print(Fore.GREEN + '[+] ', server, end='\n')
    print()
    http = urllib3.PoolManager()
    r = http.request('GET', server)
    stringg = str(r.data)
    new = stringg.split(' ')
    for j in new:
        print(j)
    #print(new, end='\n')
    print()



def main():
    parser = optparse.OptionParser(sys.argv[0] + ' ' + '-u <single url> -i <file_with URLs> ')
    parser.add_option('-u', dest='singleurl', type='string', help='specify single URL in format http(s)://url:port')
    (options, args) = parser.parse_args()
    singleurl = options.singleurl
    if singleurl is None:  
        print(parser.usage, end='\n')  
        print()
        sys.exit(0)

  


    if singleurl is not None:

        webreq(singleurl)



startTime = time.time()

def ports():
    target = 'localhost'
    t_IP = gethostbyname(target)
    print ('Starting scan on host: ', t_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if(conn == 0) :
            print ('Port %d: OPEN' % (i,))
        print(time.time() - startTime)
        s.close()




if __name__ == '__main__':
    main()
