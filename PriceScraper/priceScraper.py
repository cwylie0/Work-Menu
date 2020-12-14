# import libraries
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import csv
import re
import os

iwmURLs = {
"iphone": "https://www.itsworthmore.com/sell/iphone",
"galaxy": "https://www.itsworthmore.com/sell/galaxy-s-series",
"galaxy-note": "https://www.itsworthmore.com/sell/galaxy-note-series",
"ipad-pro": "https://www.itsworthmore.com/sell/ipad-pro",
"ipad-air": "https://www.itsworthmore.com/sell/ipad-air",
"ipad-mini": "https://www.itsworthmore.com/sell/ipad-mini",
"ipad": "https://www.itsworthmore.com/sell/ipad-original"
}

a = [["DEVICE", 'ITSWORTHMORE']]
now = time.strftime("%m-%d-%Y")
here = os.path.dirname(os.path.realpath(__file__))
subdir = "pricing-output"
filename = "Pricing-Report-"+now+".csv"
filepath = os.path.join(here, subdir, filename)
#f = open(filename,'a')

def printOutputInfo():
    print ("")
    print ("*** MAX PRICE SCRAPER V 1.0 ***")    
    print ("")
    print("Pricing report being generated and will output to: ")
    print(filename)    


def pricit(paramURL):
    req = Request(paramURL, headers={'User-Agent': 'Mozilla/5.0'})
    web_page = urlopen(req).read()    
    soup = BeautifulSoup(web_page, 'html.parser')
    mydivs = soup.findAll("a", {"class": "box"})
    
    for link in mydivs:        
        link = str(link)
        device = link[(link.find('<br/>')+ 6) : (link.find('<br/>')+ 6) + 30]
        device = device.split("<", 1)
        device = device[0].strip()
        

        maxprice = link[(link.find('success-color')+ 38) : (link.find('success-color')+ 38) + 20]
        maxprice = maxprice.split("<", 1)
        maxprice = maxprice[0]
        maxprice = maxprice.replace(" ", "")
        
        #print(device + ", " + maxprice)
        b=[device, maxprice]
    
        a.append(b)

        #print(link)


def printTable(listoflists):
        for l in listoflists:
                for c in l:
                        print(c, end= " ")
                print() 

def outputCSV(tableData):
    # print(tableData)   
    with open(filepath, 'w', newline="") as csvfile:
        writer = csv.writer(csvfile)
        for line in tableData:
                writer.writerow(line)

def scrapePrices():
    printOutputInfo()  
    for lurl in iwmURLs:
       pricit(iwmURLs[lurl])
  
    printTable(a)   
    outputCSV(a)
