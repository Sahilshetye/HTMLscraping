# -*- coding: utf-8 -*-

import bs4 as bs
import csv
import codecs


#file= input("Enter the path for index.html:")
#sauce= open(unicode(file),'r')
#name= input("Enter the name for output file(.csv):")

sauce= open('/data1/Test folder/output/index.html','r')
soup = bs.BeautifulSoup(sauce,'lxml')



tabl= soup.find_all('table')[1]   # skipping first table


soup= bs.BeautifulSoup(str(tabl).replace("Δ","DEL-").replace("→",">").replace(" "," ").replace("←","<"),'lxml')

tabl1 = soup.find_all('tr')


otp=""

for tabs in tabl1:
    #print(tabs)
    trs = bs.BeautifulSoup(str(tabs), 'lxml')
    rows=trs.find_all('td')
    #print((rows))

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
    otp+=  unicode(u'\n')


temp=unicode(otp)
c = open("test.csv", "w")
#print(otp)
c.write(otp.encode("utf8"))


c.close()