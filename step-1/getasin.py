from time import sleep

import urllib2, re

def findasin(url):
    headers = {'User-Agent' : 'Mozilla 5.10'}
    request = urllib2.Request(url,None,headers)
    sock = urllib2.urlopen(request)
    ch = sock.read()
    sock.close()
    #print ch
    asin=re.findall('(?=asins=)(.*)(?<=;bn=)',ch)
    return asin[0] ### Print these lines

f = open("camping.txt",'r')
l=[[line] for line in f.readlines()]
for line in l:
    try:
        line.append(findasin(line[0]))
        assert False
        sleep(18)
    except:
        pass
f.close()

outfile = open("results", "w")

for item in l:
    print >> outfile, ",".join(str(i).replace('asins=','').replace(';bn=','') for i in item)
outfile.close()
