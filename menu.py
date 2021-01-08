# Text menu in Python
from yelp.yelp import *
from reviewResponse.reviewResponse import *
#from RatingScraper.rating import *
from imageGenerator.imageGenerator import *
from contentWriterNew.contentWriterNew import runtings
#from chromebookWriter.chromebookWriter import chromebookWrite
from priceAdjuster.priceAdjuster import adjust
from PriceScraper.priceScraper import scrapePrices


# Arbus, Robert Frank, Lee Friedlander, Lisette Model, Garry Winogrand

def print_menu():  # Your menu design here
    print("")
    print("<<<<< IFIXYOURI SCRIPTS V 2.3 >>>>>")
    print("----------- by cwylie0 ------------")
    print("1. YELP AUTORESPONDER")
    print("2. 5-STAR REVIEW RESPONDER")
    #print("3. RATINGS SCRAPER")
    print("4. DEVICE SERVICE PAGE CREATOR") 
    print("5. SERVICE PAGE IMAGE GENERATOR")  
    #print("6. CHROMEBOOK SERVICE PAGE CREATOR")
    #print("7. COMPETITOR BUYBACK PRICE SCRAPER")     
    print("0. EXIT")
    print("-----------------------------------")

ans = True
while ans:
    print_menu()
    ans = input("What would you like to do? ")
    if ans == "1":
        replace()    
    elif ans == "2":
        generateResponse()
    elif ans == "3":
    #    scrape()
         print("")
    elif ans == "4":
        runtings()
    elif ans == "5":
        prettyPictures()
    elif ans == "6":
        #chromebookWrite()
        print("")
    #elif ans == "7":
    #    scrapePrices()    
    elif ans=="0":
        print("\n~~~~~ GOODBYE! ~~~~~")
        print("")
        quit()
    elif ans !="":
        print("\nNot Valid Choice Try again")