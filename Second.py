import bs4 as bs
import csv
import codecs

sauce= open('C:\\Users\\sahil.shetye\\Desktop\\Test folder\\output\\index.html','r')
soup = bs.BeautifulSoup(sauce,'lxml')



tabl= soup.find_all('table')[1]   # skipping first table


soup= bs.BeautifulSoup(str(tabl),'lxml')

tabl1 = soup.find_all('tr')


otp=""

for tabs in tabl1:
    #print(tabs)
    trs = bs.BeautifulSoup(str(tabs), 'lxml')
    rows=trs.find_all('td')
    #print(rows)
    count=0
    for row in rows:
        #print('End of row <<<<<<<<<')

        soup= bs.BeautifulSoup(str(row),'lxml')
        if (row.a != None):
            otp += row.a['href']
            otp += str('    ')


        otp+=soup.td.text.replace(",","")
        otp+=str('  ')
        count+=1
    otp+=  str('\n')


temp=str(otp.encode('utf-8'))
c = open("MYFILE.csv", "w")
print(otp)
c.write(temp)


c.close()