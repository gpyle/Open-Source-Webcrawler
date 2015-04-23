from time import sleep

import urllib2, re

def hasFreeShipping(url):
    headers = {'User-Agent' : 'Mozilla 5.10'}
    request = urllib2.Request(url,None,headers)
    sock = urllib2.urlopen(request)
    ch = sock.read()
    sock.close()
    #print ch    #### debug mode
    price=re.findall('(?=bxgy-item-price)(.*)',ch)
    #rank=re.findall('(.*)(?<= in Sports &amp; Outdoors )',ch)
    return 'Ships from and sold by Amazon.com' in ch, price[0]#, rank[0]
    #return 'Offers with FREE Shipping by Amazon (0)' in ch,reviews[0],stars[0],title[0]  #,vendor[0]  #title[0]  ### Print these lines
    #return stars[0]

f = open("run.txt",'r')
l=[[line] for line in f.readlines()]
for line in l:
    try:
        line.append(hasFreeShipping(line[0]))
        assert False
        sleep(35)
    except:
        pass
f.close()

outfile = open("results", "w")

for item in l:
    #for m in item:
    #    print m
    #print >> outfile, ",".join(str(i) for i in item)
    print >> outfile, ",".join(str(i).replace('\n','').replace('a-icon-star a-star-','').replace('<title dir="ltr">Amazon.com: Buying Choices: ','').replace('    ','').replace('\'','').replace('(','').replace(')','').replace('    ','').replace('\'','').replace('(','').replace(')','').replace('</title>','').replace('   ','').replace('"></i>','') for i in item)
outfile.close()


#write = open("results-formatted", "w")
#for item in l:
#    print >>


###### scp ~/Desktop/atlassian-jira-6.3.9-x32.bin root@107.170.237.162:~/JIRA/
###
