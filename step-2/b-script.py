from time import sleep

import urllib2, re

def hasFreeShipping(url):
    headers = {'User-Agent' : 'Mozilla 5.10'}
    request = urllib2.Request(url,None,headers)
    sock = urllib2.urlopen(request)
    ch = sock.read()
    sock.close()

    ### Welcome to the Open Source Webcrawler

    ### A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings.
    ### For example the (?<=...) regular expression is called a positive lookbehind assertion.
    ### The syntax for regular expressions in python is re.findall(pattern, string, flags=0).

    ### Step-2 searches every product on Amazon in the run.txt file, and returns the number of reviews, the number of stars, and the product title.


    #### Returns all non-overlapping matches of pattern in string, as a list of strings.
    ### Find Number Customer Reviews:< ... "> 208 customer reviews </a>
    reviews=re.findall('(.*)(?<=customer review)',ch)

    # Find Title: <title dir="ltr">Amazon.com: Buying Choices: 15" Standard Wooden Chess Set</title>
    title=re.findall('(.*)(?<=</title>)',ch)
    # Next find number of stars
    # Note that ?=  is for positive look ahead
    # Search for string <i class="a-icon a-icon-star a-star-3"></i>
    # <div id="olpProductByline" class="a-section a-spacing-mini"> by Epson </div>
    #vendor=re.findall('(?=olpProductByline)(.*)',ch)
    #stars=[4]
    ##stars=re.search(r'a-star-. (\S+)',ch2)
    stars=re.findall('(?=a-icon-star)(.*)',ch)
    #print ch ###debug mode
    ### <span class="a-size-base a-color-secondary"> 4.4 out of 5 stars </span>
    #stars=re.findall('(.*)(?<=out of 5 star)',ch)
    return reviews[0],stars[0],title[0] ### Print these lines


f = open("run.txt",'r')
l=[[line] for line in f.readlines()]
for line in l:
    try:
        line.append(hasFreeShipping(line[0]))
        assert False
        sleep(1)
    except:
        pass
f.close()

outfile = open("results", "w")

for item in l:
    #print >> outfile, ",".join(str(i) for i in item)
    print >> outfile, ",".join(str(i).replace('\n','').replace('a-icon-star a-star-','').replace('<title dir="ltr">Amazon.com: Buying Choices: ','').replace('    ','').replace('\'','').replace('(','').replace(')','').replace('    ','').replace('\'','').replace('(','').replace(')','').replace('</title>','').replace('   ','').replace('"></i>','') for i in item)
outfile.close()
