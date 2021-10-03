#####Sirin Hosts Autoreditor by MisakaSirin#####

import urllib.request
import urllib.error
from bs4 import BeautifulSoup as bs
import sys
import re
import os
import getopt

print('Sirin Domain Address Searcher  ver. 1.0.2 Build4F3CE2D')

ipv4s = []
ipv6s = []
l = []

usage = '''
Sirin Domain Address Searcher ver 1.0.2 Build4F3CE2D Developed by MisakaSirin
Usage: srndas <Target Domain Name>/[-h]/[-b]/[-r] [-w [FILENAME]]/[-e]/[-l]
    Target Domain Name: The domain name that you want to search
    -h --help:          Show this page
    -b --backup:        Make a backup file for /etc/hosts
    -r --restore        Restore /etc/hosts from a file (Normally ~/.SirinDAS)
    -w --write          Write result to a certain file (Normally /etc/hosts, this operation requires root permission)
    -l --load           Force system to load /etc/hosts when the previous progress is done

Example: srndas www.sirin.net.cn -w ~/example.txt
HAVE FUN :)
'''

#后续加入功能，不完善
'''
def aligns(string, length=20):
    difference = length - len(string)  # 计算限定长度为20时需要补齐多少个空格
    if difference == 0:  # 若差值为0则不需要补
        return string
    elif difference < 0:
        print('[!] Error! IntE_6_Tab')
        sys.exit(10)
    new_string = ''
    space = '　'
    for i in string:
        #print("Current: " + str(i))
        #codes = ord(i)  # 将字符转为ASCII或UNICODE编码
        #if codes <= 126:  # 若是半角字符
            #new_string = new_string + chr(codes+65248) # 则转为全角
        #else:
        new_string = new_string + i  # 若是全角，则不转换
    return new_string + space*(difference)  # 返回补齐空格后的字符串

def tabulator(inputlist, column, length=20):
    p = ''
    num = 0
    sum = len(inputlist)
    for i in inputlist:
        p = p + aligns(i,length)
        num = num + 1
        sum = sum - 1
        if num >= column:
            print(p)
            p = ''
            num = 0
        elif sum <= 0:
            print(p)
'''

if os.geteuid() != 0:
    print("[!] Aborting. (No Permission)")
    sys.exit(2)

args = sys.argv[]
if len(args) == 0:
    print('[!] Aborting. (Bad Args)')
    sys.exit(15)

print('[*] Getting Page: ' + input + ' --> ' + site)
site = 'https://' + site

try:
    #headers = {'User_Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}
    headers = {'User_Agent': "MisakaSirin bot"}
    response = urllib.request.Request(site, headers=headers)
    html = urllib.request.urlopen(response)
    result = html.read().decode('utf-8')
except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print('[-] Aborting. ' + str(e.reason))
        sys.exit(10086)
except urllib.error.HTTPError as e:
    if hasattr(e, 'code'):
        print('[-] Aborting. ERR' + str(e.code))
        sys.exit(int(e.code))
else:
    print('[+] Page Get')

print('[*] Analyzing Page')
soup = bs(result, features="lxml")
ipv4 = soup.find_all("a", href=re.compile("https://www.ipaddress.com/ipv4/"))

#print(ipv4)
ipv6 = soup.find_all("a", href=re.compile("https://www.ipaddress.com/ipv6/"))
ipv6 = list(set(ipv6))

#print(ipv6)

for i in range(0, len(ipv4)):
    t = str(ipv4[i])
    stpce = t.find('>') + 1
    edpce = t.find('<', stpce) - 1
    ipv4s.append(t[stpce:edpce])

for i in range(0, len(ipv6)):
    t = str(ipv6[i])
    stpce = t.find('>') + 1
    edpce = t.find('<', stpce) - 1
    ipv6s.append(t[stpce:edpce])

ipv6s = list(set(ipv6s))  #去除重复项
ipv4s = list(set(ipv4s))  #去除重复项

print('[+] Result:')
print('     Find ' + str(len(ipv4s)) + ' IPv4', end = '')
print(', ' + str(len(ipv6s)) + ' IPv6' , end = '')
print('for ' + input)
print('      No.   IP Address | Domain Name')
print('     ---------------------------------------------')
if len(ipv4) == 0:
    print('     [===No IPv4 Found]===')
else:
    #TabAuto
    '''
    for i in range(0, len(ipv4)):
        l.append(str(i))
        l.append(ipv4s[i])
        l.append(input)
    #print(l)
    tabulator(l, 3, 10)
    '''

    for i in range(0, len(ipv4s)):
        print("     ", 4*10 + i, "  ", ipv4s[i], "  ", input)

print()
if len(ipv6) == 0:
    print('     [===No IPv6 Found===]')
    if len(ipv4s) == 0:
        print('[!] No IP found. Exiting.')
else:
    for i in range(0, len(ipv6s)):
        print("     ", 6*10 + i, "  ", ipv6s[i], "  ", input)
'''
r = input('[?] Write to hosts file? (y/n)')

if r == 'y' or r == 'Y':
    pass
else:
    print('[-] Aborting.(Operate by User)')
    sys.exit(0)
'''