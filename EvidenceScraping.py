#!/usr/bin/python3
# -*- coding: utf-8 -*-

import bs4 as bs
import sys, getopt
import os
import re

class EvidenceModel:
    seqid=""
    pos=""
    ref=""
    new=""
    freq=""
    score=""
    reads=""
    annotation=""
    gene=""
    product=""
    refbase=""
    newbase=""
    total=""
    fisher=""
    smirnov=""

def main(argv):
    ev=EvidenceModel()
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

    otp=""
    file= input_html

    fname= os.path.basename(file)
    print(fname)
    matchobj= re.search("^([A-Z]+)_([0-9]+).html$",fname)
    if matchobj and not matchobj.group(1)=="JC":
        sauce = open(file, 'r')
        soup = bs.BeautifulSoup(sauce, 'lxml')
        tablecount= soup.findAll('table').__len__()
        print(tablecount)
        if tablecount==4:
            table=soup.select('table')[1]
            row1=table.select('tr')[2]
            ev.seqid= row1.select('td')[1].text
            ev.pos=row1.select('td')[2].text.replace(",","")
            ev.ref=row1.select('td')[4].text
            ev.new=row1.select('td')[5].text
            ev.freq=row1.select('td')[6].text
            ev.score=row1.select('td')[7].text
            ev.reads=row1.select('td')[8].text
            ev.annotation=row1.select('td')[9].text
            ev.gene=row1.select('td')[10].text
            ev.product=row1.select('td')[11].text
            row2=table.select('tr')[3]
            mo2= re.search("ref base (.+) \((.+)\);",row2.text)
            #new base (.+) \((.+)\);  total \((.+)\)
            if mo2:
                ev.refbase=mo2.group(2)
            mo2 = re.search("new base (.+) \((.+)\);", row2.text)
            if mo2:
                ev.newbase=mo2.group(2)
            mo2 = re.search("total \((.+)\)$", row2.text)
            if mo2:
                ev.total=mo2.group(1)

            row3=table.select('tr')[4]
            mo3 = re.search("p-value = (.+)$", row3.text)
            if mo3:
                ev.fisher = str(float(mo3.group(1)))


            row4 = table.select('tr')[5]
            mo4 = re.search("p-value = (.+)$", row4.text)
            if mo4:
                ev.smirnov = str(float(mo4.group(1)))
            #otp+=ev.seqid+"\t"+ev.pos+"\t"+ev.ref+"\t"+ev.new+"\t"+ev.freq+"\t"+ev.score+"\t"+ev.reads+"\t"+ev.annotation+"\t"+ev.gene+"\t"+ev.product+"\t"+ev.refbase+"\t"+ ev.newbase+"\t"+ ev.total+"\t"+ ev.fisher+"\t"+ev.smirnov+"\n"
        elif tablecount==3:
            table=soup.select('table')[0]
            row1 = table.select('tr')[2]
            ev.seqid = row1.select('td')[1].text
            ev.pos = row1.select('td')[2].text.replace(",", "")
            ev.ref = row1.select('td')[4].text
            ev.new = row1.select('td')[5].text
            ev.freq = row1.select('td')[6].text
            ev.score = row1.select('td')[7].text
            ev.reads = row1.select('td')[8].text
            ev.annotation = row1.select('td')[9].text
            ev.gene = row1.select('td')[10].text
            ev.product = row1.select('td')[11].text
            row2 = table.select('tr')[3]
            mo2 = re.search("ref base (.+) \((.+)\);", row2.text)
            # new base (.+) \((.+)\);  total \((.+)\)
            if mo2:
                ev.refbase = mo2.group(2)
            mo2 = re.search("new base (.+) \((.+)\);", row2.text)
            if mo2:
                ev.newbase = mo2.group(2)
            mo2 = re.search("total \((.+)\)$", row2.text)
            if mo2:
                ev.total = mo2.group(1)

            row3 = table.select('tr')[4]
            mo3 = re.search("p-value = (.+)$", row3.text)
            if mo3:
                ev.fisher = str(float(mo3.group(1)))

            row4 = table.select('tr')[5]
            mo4 = re.search("p-value = (.+)$", row4.text)
            if mo4:
                ev.smirnov = str(float(mo4.group(1)))
        otp += ev.seqid + "\t" + ev.pos + "\t" + ev.ref + "\t" + ev.new + "\t" + ev.freq + "\t" + ev.score + "\t" + ev.reads + "\t" + ev.annotation + "\t" + ev.gene + "\t" + ev.product + "\t" + ev.refbase + "\t" + ev.newbase + "\t" + ev.total + "\t" + ev.fisher + "\t" + ev.smirnov + ""
        otp=otp.replace(u'\n','').replace(u'\u2011','').replace(u'\xc2','').replace(u'\xa0','').replace(u'\u2192','>').replace("Δ","DEL-").replace("←","<")
        #otp+=u"\n"
        print(otp.encode("646"))
        c = open(output_file, "w")

        c.write(otp)

        c.close()





    else:
        print ("Error")
        #print("no")
if __name__ == "__main__":
   main(sys.argv[1:])


