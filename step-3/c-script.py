from time import sleep

import urllib2, re

    ### Welcome to the Open Source Webcrawler

    ### A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings.
    ### For example the (?<=...) regular expression is called a positive lookbehind assertion.
    ### The syntax for regular expressions in python is re.findall(pattern, string, flags=0).

    ### Step-3 searches every product on Amazon in the run.txt file, and lets you know if the product is sold with prime and lets you know the product selling price.


def hasFreeShipping(url):
    headers = {'User-Agent' : 'Mozilla 5.10'}
    request = urllib2.Request(url,None,headers)
    sock = urllib2.urlopen(request)
    ch = sock.read()
    sock.close()
    price=re.findall('(?=bxgy-item-price)(.*)',ch)
    return 'Ships from and sold by Amazon.com' in ch, price[0]

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
    print >> outfile, ",".join(str(i).replace('\n','').replace('a-icon-star a-star-','').replace('<title dir="ltr">Amazon.com: Buying Choices: ','').replace('    ','').replace('\'','').replace('(','').replace(')','').replace('    ','').replace('\'','').replace('(','').replace(')','').replace('</title>','').replace('   ','').replace('"></i>','') for i in item)
outfile.close()
