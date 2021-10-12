#!python3
#-*- coding:utf-8 -*-
#####Sirin Domain Address Searcher by MisakaSirin ANALYZER#####

from bs4 import BeautifulSoup as bs
import sys
import re
import time



ipv4s = []
ipv6s = []

print('[*] Analyzing Page')

try:
    with open('file.txt', 'r') as f:
        result = f.open()
except Exception:
    pass

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

print(ipv6s)
print(ipv4s)