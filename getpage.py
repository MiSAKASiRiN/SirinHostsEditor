#!python3
#-*- coding:utf-8 -*-
#####Sirin Domain Address Searcher by MisakaSirin PAGEGET#####
#Pattern e3

from http.client import INSUFFICIENT_STORAGE
import sys
#import urllib.request 
import urllib.error
import urllib.request
import os
import time

def Schedule(a,b,c):
   '''
   a:已经下载的数据块
   b:数据块的大小
   c:远程文件的大小
   '''
   per = 100.0*a*b/c
   if per > 100:
      per = 100
   print('%.2f%%' % per)

try:
    target = str(sys.argv[1])
except IndexError:
    print('No args')
    sys.exit(10)

dir = os.path.abspath('.')  
work_path = os.path.join(dir,'temp.srntp')

try:
    ##headers = {'User_Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}
    #headers = {'User_Agent': "MisakaSirin bot :)"}
    #response = urllib.request.Request(site, headers=headers)
    #html = urllib.request.urlopen(response)
    #result = html.read().decode('utf-8')
    urllib.request.urlretrieve(target, work_path, Schedule)

except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
        print('%SIRINERR:' + str(e.reason))
        sys.exit(10086)
except urllib.error.HTTPError as e:
    if hasattr(e, 'code'):
        print('%SIRINERR:' + str(e.code))
        sys.exit(int(e.code))

else:

    print('done')