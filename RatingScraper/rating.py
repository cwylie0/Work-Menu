# import libraries
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import csv
import re
import os

# specify the url
yelpURLs = {
# Orlando Stores
"Altamonte Springs": "https://www.yelp.com/biz/ifixyouri-iphone-ipad-and-ipod-repair-altamonte-springs-2",
"Downtown Orlando": "https://www.yelp.com/biz/i-fix-your-i-orlando-9",

#Palm Beach Stores
"Donald Ross": "https://www.yelp.com/biz/ifixyouri-iphone-ipad-and-ipod-repair-jupiter",
"Indiantown": "https://www.yelp.com/biz/i-fix-your-i-smart-device-repair-jupiter-6",
"Northlake": "https://www.yelp.com/biz/i-fix-your-i-palm-beach-gardens-5",
"West Palm": "https://www.yelp.com/biz/ifixyouri-iphone-ipad-and-ipod-repair-west-palm-beach-5"
}

# specify the url
googURLs = {
#Orlando Stores
"Altamonte Springs": "https://www.google.com/search?q=iFixYouri+Altamonte+Springs",
"Downtown Orlando": "https://www.google.com/search?q=iFixYouri+Colonial+Dr",

#Palm Beach Stores
"Donald Ross": "https://www.google.com/search?q=iFixYouri+Donald+Ross",
"Indiantown": "https://www.google.com/search?q=iFixYouri+Indiantown+Road",
"Northlake": "https://www.google.com/search?q=iFixYouri+Northlake",
"West Palm": "https://www.google.com/search?q=iFixYouri+West+Palm"
}

# specify the url
fbURLs = {
#Orlando Stores
"Altamonte Springs": "https://www.facebook.com/IFixYouriAltamonteSprings/reviews/",
"Downtown Orlando": "https://www.facebook.com/Ifixyouri.Downtown.Orlando/reviews/",

#Palm Beach Stores
"Donald Ross": "https://www.facebook.com/iFixYouri.Jupiter.DonaldRoss/reviews/",
"Indiantown": "https://www.facebook.com/iFixYouriJupiterIndiantown/reviews/",
"Northlake": "https://www.facebook.com/iFixYouri.Northlake/reviews/",
"West Palm": "https://www.facebook.com/ifixyouri.west.palm.beach/reviews/"
}

a = [["LOCATION", 'YELP RATING', 'YELP REVIEWS','GOOGLE RATING','GOOGLE REVIEWS', 'FB RATING', 'FB REVIEWS']]
now = time.strftime("%m-%d-%Y")
here = os.path.dirname(os.path.realpath(__file__))
subdir = "rating-output"
filename = "Ratings-Report-"+now+".csv"
filepath = os.path.join(here, subdir, filename)
#f = open(filename,'a')

def printOutputInfo():
    print ("")
    print ("*** RATINGS SCRAPER V 2.3 ***")    
    print ("")
    print("Ratings report being generated and will output to: ")
    print(filename)    

def printHeader(SocialNetwork):
    print("\n")
    header = SocialNetwork + " Ratings"
    print(header)
    print('-' * len(header)) 

def yelpify():
    for key in yelpURLs:
        # query the website and return the html to the variable ‘page’
        quote_page = yelpURLs[key]
        page = urllib.request.urlopen(quote_page)
    
        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page, 'html.parser')
    
        # get the rating
        # rating_box = soup.find('div', attrs={'class':'i-stars'})    
        rating = str(soup) #convert the bs4 to class str  
        rating = rating[(rating.find('"@type": "AggregateRating", "ratingValue":')+ 43) : (rating.find('"@type": "AggregateRating", "ratingValue":')+ 43) + 3]


        review_count_box = soup.find('span', attrs={'itemprop':'reviewCount'})    
        review_count = str(review_count_box) #convert the bs4 to class str   
    
        reviewCount = review_count[(review_count.find('Count')+ 7) : (review_count.find('Count')+ 7) + 3]
        reviewCount = reviewCount.replace("<", "")
        reviewCount = reviewCount.replace("/", "")

        print(key + ", " + rating + ", " + reviewCount)
        b=[key, rating, reviewCount]
    
        a.append(b)

def googlify():
    c = 1
    for key in googURLs:
        # query the website and return the html to the variable ‘page’
        quote_page = googURLs[key]
        req = Request(quote_page, headers={'User-Agent': 'Mozilla/5.0'}) #adds a user agent to not get blocked
        page = urlopen(req).read()        

        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page, 'html.parser')
    
        # get the rating
        rating = str(soup) #convert the bs4 to string
        
        print(soup.encode("utf-8"))
        
        #since google changes div names, it takes two slices to get to the rating 
        firstSlice = rating[(rating.find('class="oqSTJd">')+15) : (rating.find('class="oqSTJd">')+15) + 3]             
        #rate = firstSlice[(firstSlice.find('.')-1) : (firstSlice.find('.')-1) + 3]

        #since google changes div names, it takes two slices to get to the rating 
        secondSlice = rating[(rating.find('role="img"><span style="width:63px"></span></div> <span>(')+57) : (rating.find('role="img"><span style="width:63px"></span></div> <span>(')+57) + 3]          
              
        
        if secondSlice == "set" or key == "Winter Park":
            print("FLAG")
            secondSlice = rating[(rating.find('out of 5" class=')+88) : (rating.find('out of 5" class=')+88) + 3]

        secondSlice = secondSlice.replace(")", "")
        secondSlice = secondSlice.replace(" ", "")

        print(key + ", " + firstSlice + ", " + secondSlice)        
        #time.sleep(1) #add a pause to not get blocked  
    
        a[c].append(firstSlice)
        a[c].append(secondSlice)
        c = c + 1

def fbify():
    c = 1
    for key in fbURLs:
        # query the website and return the html to the variable ‘page’
        quote_page = fbURLs[key]
        req = Request(quote_page, headers={'User-Agent': 'Mozilla/5.0'}) #adds a user agent to not get blocked
        page = urlopen(req).read()        

        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page, 'html.parser')
    
        # get the rating
        rating = str(soup) #convert the bs4 to string
               
        rate = rating[(rating.find('lightweight_score_explainer')) - 51 : (rating.find('lightweight_score_explainer')) - 48]
        rate = rate.replace(" ", "")
        rate = re.sub('[^0-9.]','', rate)
        if rate == "": 
                rate = "0"
        
        
        secondSlice = rating[(rating.find('on the opinion of')) + 17 : (rating.find('on the opinion of')) + 21]   
        secondSlice = secondSlice.replace(" ", "")
        secondSlice = re.sub('[^0-9]','', secondSlice)
        if secondSlice == "": 
                secondSlice = "0"
        
        
        print(key + ", " + rate + ", " + secondSlice)       
    
        a[c].append(rate)
        a[c].append(secondSlice)
        c = c + 1

def printTable(listoflists):
        for l in listoflists:
                for c in l:
                        print(c, end= " ")
                print() 

def outputCSV(tableData):
    # print(tableData)   
    with open(filepath, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for line in tableData:
                writer.writerow(line)

def scrape():
    printOutputInfo()
    printHeader("Yelp")
    #yelpify()
    printHeader("Google")
    googlify() 
    printHeader("Facebook")
    #fbify()
    # printTable(a)   
    outputCSV(a)

scrape()