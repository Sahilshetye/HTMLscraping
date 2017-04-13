#!/usr/bin/python3
# -*- coding: utf-8 -*-

import bs4 as bs
import csv
import codecs
import sys, getopt

def main(argv):
    input_html = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=", "ofile="])
    except getopt.GetoptError:
        print ('Indexscript.py -i <index.html file path> -o <output file name>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('Indexscript.py -i <index.html file path> -o <output file name>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_html = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
#    print ('Input file is ', input_html)
#    print ('Output file is ', output_file)

    file= input_html
    sauce= open(file, 'r')
    #sauce= open('C:\\Users\\sahil.shetye\\Desktop\\Test folder\\output\\index.html','r')
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
                otp += str("\t")


            otp+=soup.td.text
            otp+=str('\t')
            count+=1
        otp = otp[:-1]
        otp+=  ('\n')


    temp=otp.replace(',',"").replace(u'\u2011',"").replace("Δ","DEL-").replace("→",">").replace(u" "," ").replace("←","<").replace(u'\xa0','')
    c = open(output_file, "w")
    print(temp)
    c.write(temp)


    c.close()

if __name__ == "__main__":
   main(sys.argv[1:])