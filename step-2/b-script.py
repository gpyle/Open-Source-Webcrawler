from time import sleep

import urllib2, re

def hasFreeShipping(url):
    headers = {'User-Agent' : 'Mozilla 5.10'}
    request = urllib2.Request(url,None,headers)
    #request2 = urllib2.Request(url,None,headers)
    sock = urllib2.urlopen(request)
    #sock2 = urllib2.urlopen(request)
    ch = sock.read()
    #ch2 = sock2.read()
    #ch2 = sock.read()
    sock.close()
    #sock2.close()
    ### < ... "> 208 customer reviews </a>
    ### (?<=...) regular expression is called a positive lookbehind assertion
    ### re.findall(pattern, string, flags=0)
      #### Returns all non-overlapping matches of pattern in string, as a list of strings.
    ## Think (\S+) finds symbols and numbers, ex. 555-1212
    reviews=re.findall('(.*)(?<=customer review)',ch)
    # Find Title
    # <title dir="ltr">Amazon.com: Buying Choices: 15" Standard Wooden Chess Set</title>
    #title=re.findall
    title=re.findall('(.*)(?<=</title>)',ch)
    #title[25:-6]
    # Next find number of stars
    # Note that ?=  is for positive look ahead
    # Search for string <i class="a-icon a-icon-star a-star-3"></i>
    # <div id="olpProductByline" class="a-section a-spacing-mini"> by Epson </div>
    #vendor=re.findall('(?=olpProductByline)(.*)',ch)
    #stars=[4]
    ##stars=re.search(r'a-star-. (\S+)',ch2)
    stars=re.findall('(?=a-icon-star)(.*)',ch)
    #stars[18:]
    #print ch ###debug mode
    ### <span class="a-size-base a-color-secondary"> 4.4 out of 5 stars </span>
    #stars=re.findall('(.*)(?<=out of 5 star)',ch)
    return 'Offers with FREE Shipping by Amazon (0)' in ch,reviews[0],stars[0],title[0]  #,vendor[0]  #title[0]  ### Print these lines
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
