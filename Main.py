import bs4 as bs
import urllib.request
import pandas as pd
#sauce= urllib.request.urlopen(").read()
import os
import json

'''sauce= open('C:\\Users\\sahil.shetye\\Desktop\\Test folder\\output\\index.html','r')
soup = bs.BeautifulSoup(sauce,'lxml')

tabl= soup.table   # skipping first table

for tabs in tabl.find_next('table'):
    print(tabs)
    print("This table is done")
   '''

rootdir="M:\\variant_analysis"

mutationdic= {}
def fcheck( st ):
    if st not in mutationdic:
        mutationdic[st]= 1
        #print(" mutationdic is= ",mutationdic)
        print(st)
        json.dump(mutationdic,"Outputlist.txt")


f=[]
for (dirpath, dirnames, filenames) in os.walk(rootdir):
    f.extend(dirnames)
    break

mainpath=[]
count=0
for path in f:
    try:
        mp=os.path.join(rootdir,path+'\\output\\index.html')
        #print(mp)
        count +=1
        #print ("Count is ")
        #print(count)
        dfs= pd.read_html(mp,header=1) # make header to be 1 and ignore which does not have 1
        list=dfs[0].mutation
        for l in list:
            fcheck(l)
            #print (l)
    except Exception as e:
        print("Output folder not found ",str(e),"Test running")




print(" RESULT is as follows: ------------------------>")
for mu in mutationdic:
    print (mu)