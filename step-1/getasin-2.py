from time import sleep

import urllib2, re

    ### Welcome to the Open Source Webcrawler

    ### A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings.
    ### For example the (?<=...) regular expression is called a positive lookbehind assertion.
    ### The syntax for regular expressions in python is re.findall(pattern, string, flags=0).

    ### Step-1 finds and lists the ASIN Amazon bar codes from any top 100 best sellers list on Amazon.
    

def findasin(url):
    headers = {'User-Agent' : 'Mozilla 5.10'}
    request = urllib2.Request(url,None,headers)
    sock = urllib2.urlopen(request)
    ch = sock.read()
    sock.close()
    print ch
    #asin=re.findall('(?=asins=)(.*)(?<=;bn=)',ch)
    var0=re.findall('(.*)(?<=_1)',ch)
    var1=re.findall('(.*)(?<=_21)',ch)
    var2=re.findall('(.*)(?<=_22)',ch)
    #ref=zg_bs_172541_
    return var0[0], var1[0], var2[0] ### Print these lines

f = open("audio.txt",'r')
l=[[line] for line in f.readlines()]
for line in l:
    try:
        line.append(findasin(line[0]))
        assert False
        sleep(3)
    except:
        pass
f.close()

outfile = open("results", "w")

for item in l:
    print >> outfile, ",".join(str(i) for i in item)
outfile.close()
