import urllib.request as url
import sys
import re
import datetime

def fr(elem):
    return (int(re.sub(r'&nbsp;','',elem)))
renum = re.compile(r'''<li class="girl(\d)\s*number(\d*)''',re.DOTALL)
retir = re.compile(r'''<h1>Результаты тиража № (\d*),\s*(\d*)\s*(\w*)\s*(\d*)\s*в\s*(.*?)</h1>''',re.DOTALL)
reres = re.compile(r''' 
    <tbody>\s*
        \s*<tr>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        </tr>\s*
        <tr>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        </tr>\s*
        <tr>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        </tr>\s*
        <tr>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        </tr>\s*
        <tr>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        <td>\s*(.*?)\s*</td>\s*
        </tr>\s*
        </tbody> 
        ''', re.DOTALL | re.VERBOSE)

#tirag = 1
mon={'января':'01','февраля':'02','марта':'03','апреля':'04','мая':'05','июня':'06','июля':'07','августа':'08','сентября':'09','октября':'10','ноября':'11','декабря':'12'}
for tirag in range(1900,2050):
    fh = url.urlopen('http://www.stoloto.ru/6x45/archive/' +str(tirag))
    htm = fh.read().decode("utf8")
    num = renum.findall(htm)
    tir = retir.findall(htm)
    r = reres.findall(htm)
    result = {}
    for i in range (0,20,4):
        result['w'+r[0][i]]={'q_win':fr(r[0][i+1]),'rub_win':fr(r[0][i+2]),'sum_w':fr(r[0][i+3])}
    ntir = tir[0][0]
    dtir = datetime.datetime.strptime(tir[0][1]+'.'+mon[tir[0][2]]+'.'+tir[0][3]+' '+tir[0][4],"%d.%m.%Y %H:%M")
    balls = (int(num[0][1]),int(num[1][1]),int(num[2][1]),int(num[3][1]),int(num[4][1]),int(num[5][1]))
    print (ntir, datetime.datetime.date(dtir), balls, result['w6']['rub_win'])

    #print (result)
