# -*- coding: utf-8 -*-

import bs4 as bs
import csv
import codecs

file= input("Enter the path for summary.html:")
sauce= open(str(file),'r')
name=input("Type the name of output file: ")

#sauce= open('C:\\Users\\sahil.shetye\\Desktop\\Test folder\\output\\summary.html','r')
soup = bs.BeautifulSoup(sauce,'lxml')

tabl= soup.find_all('table')[2]




soup= bs.BeautifulSoup(unicode(tabl),'lxml')

tabl1 = soup.find_all('tr')
#print(tabl)

otp=""

for tabs in tabl1:
    #print(tabs)
    trs = bs.BeautifulSoup(unicode(tabs), 'lxml')
    rows=trs.find_all('td')
    #print(rows)
    count=0
    for row in rows:
        #print('End of row <<<<<<<<<')

        soup= bs.BeautifulSoup(unicode(row),'lxml')
        if (row.a != None):
            otp += row.a['href']
            otp += unicode(u',')


        otp+=soup.td.text.replace(",","")
        otp+=unicode(u',')
        count+=1
    otp+=  unicode('\n')

#print(otp)
c = open(str(name+".csv"), "w")
#print(otp)
c.write(otp.encode("utf8"))


c.close()
