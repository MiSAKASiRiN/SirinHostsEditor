#!python3
#-*- coding:utf-8 -*-
#####Sirin Domain Address Searcher by MisakaSirin STARTER&ANALYZER#####

import sys
import getopt
import os
import re
from bs4 import BeautifulSoup as bs
import time

def execpy(file):
    c = 'python3 ' + file
    print('execute: ' + c)
    f = os.popen(c, "r")
    d = f.read()  # 读文件
    f.close()
    return(d)

usage = '''
Sirin Domain Address Searcher ver 1.0.2 Build4F3CE2D Developed by MisakaSirin
Usage: srndas <Target Domain Name>/[-h]/[-b]/[-r] [-w [FILENAME]]/[-t]/[-l]
    Target Domain Name: The domain name that you want to search(this shoud be the first arg)
    -h  --help:          Show this page
    -b  --backup:        Make a backup file for /etc/hosts before other progress
    -r  --restore        Restore /etc/hosts from a file (~/.sirin/bkup/srndas)
    -w  --write          Write result to a certain file 
    -t  --tohosts        Write result to /etc/hosts (this operation requires root permission)
    -l  --load           Force system to load /etc/hosts when the previous progress is done

Example: srndas www.sirin.net.cn -w ~/example.txt
HAVE FUN :)
'''

options = "-h-b-r-w:-t-l"
options_full = ["help", "backup", "restore", "write=", "tohosts", "load"]
 
secp = sys.argv[1]
if secp[0] == '-':
    opts, arg = getopt.getopt(sys.argv[1:], options, options_full)
    if len(arg) == 1:
        site = arg[0]

    else:
        if ('-h', '') in opts or ('--help', '') in opts:
            print(usage)
            sys.exit(0)

        if ('-r', '') in opts or ('--restore', '') in opts:
            site = '[RESTORE]'

        else:
            print('[-] Aborting. (Bad Args)')
            sys.exit(1)
else:
    opts, arg = getopt.getopt(sys.argv[2:], options, options_full)
    site = sys.argv[1]
    if ('-r', '') in opts or ('--restore', '') in opts:
        site = '[RESTORE]'
        sys.exit(0)

    if ('-h', '') in opts or ('--help', '') in opts:
        print(usage)
        sys.exit(0)
        

#handle_options = options.replace(':', '')
print('[*] Getting Page...')
target = site.replace('https://', '')
target = target.replace('http://', '')
site = 'https://websites.ipaddress.com/' + target

result = execpy('getpage.py ' + site)
if '%SIRINERR' in result:
    result = result.split(':')
    print('[-] Aborting (ERR: ' + str(result[1]) + ')')

else:
    print('[+] Page Get')

for o, a in opts:

    if o in ('-b', '--backup'):
        if site == '[RESTORE]':
            print('[-] Aborting. (Function RESTORE and BACKUP should not use together)')
            sys.exit(3)
        print('-Backup')

    if o in ('-w', '--write'):
        if site == '[RESTORE]':
            print('[-] Aborting. (Function RESTORE and WRITE should not use together)')
            sys.exit(4)
        dest = a
        print('-Write to: ', dest)
    
    if o in ('-t', '--tohosts'):
        if site == '[RESTORE]':
            print('[-] Aborting. (Function RESTORE and WRITETOHOSTS should not use together)')
            sys.exit(5)
        else:
            print('[*]Analyzing Page...')
            print(execpy('analyzepage ' + result))
        print('-Write to Hosts')

    if o in ('-l', '--load'):
        print('-Load')


