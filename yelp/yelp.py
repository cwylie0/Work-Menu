""" Input file: .csv with kw1, kw2, biz name, location, ST
Output: 160 chars or less of word-replaced random combo of 1st, 2nd, 3rd sentence. Length <= 160 chars
"""

import random
import csv
import sys

def printHeader():
	print ("")
	print ("*** YELP AUTORESPONDER V 3.4 ***")
	print ("")

def findPrice(argument):
    switcher = {
        "5": "$49.99",
        "5s": "$49.99",
        "5c": "$49.99",
        "6": "$59.99",
        "6+": "$69.99",
        "6s": "$69.99",
        "6s+": "$89.99",
        "se": "$49.99",
        "7": "$89.99",
        "7+": "$99.99",
		"8": "$99.99",
		"8+": "$109.99",
        "x": "$219.99",
        "xr": "219.99",
        "xs": "229.99",
        "xs max": "449.99",
        "11": "249.99",
        "11 pro": "349.99",
        "11 pro max": "349.99",
        "s7": "229.99",
        "s7e": "249.99",
        "s8": "259.99",
        "s8+": "279.99",
        "s9": "289.99",
        "s9+": "299.99"
    }
    return switcher.get(argument, "nothing")

def findURL(argument):
    switcher = {        
        "bro": "https://www.ifixyouri.com/content/128-brookline-ma",
        "wpb": "http://www.ifixyouri.com/content/102-palm-beach",
        "pga": "http://www.ifixyouri.com/content/105-palm-beach-gardens",
        "nor": "https://www.ifixyouri.com/content/147-ifixyouri-palm-beach-gardens-northlake",
        "don": "https://www.ifixyouri.com/content/149-ifixyouri-jupiter-donald-ross",
        "ucf": "http://www.ifixyouri.com/content/120-east-orlando",
        "dow": "http://www.ifixyouri.com/content/119-downtown-orlando",
        "alt": "http://www.ifixyouri.com/content/114-altamonte-springs",
        "mil": "http://www.ifixyouri.com/content/124-mall-at-millenia-orlando",
        "win": "https://www.ifixyouri.com/content/129-winter-park-fl",
        "lon": "http://www.ifixyouri.com/content/123-longwood",
		"ovi": "https://www.ifixyouri.com/content/153-oviedo-fl",
        "ind": "https://www.ifixyouri.com/content/154-ifixyouri-jupiter-indiantown",
        "all": "https://www.ifixyouri.com/content/11-locations"
    }
    return switcher.get(argument, "nothing")

def replace():
    templateOrig = "Hi NAME, thank you for contacting iFixYouri. Glass-only repair for the MODEL is $PRICE. It will be an additional $10 if your LCD display is not working. Our high-quality glass replacements come with a TIME warranty that covers everything but accidental damage. Repair times can vary depending on the current repair queue and part availability, but many model's screens can be replaced while-you-wait. Please schedule a repair appointment online for an instant $10 rebate. We are looking forward to helping you. URL";
    templateDiag= "Hi NAME, thank you for contacting iFixYouri. Sorry to hear about your device. Are you able to bring this device to one of our multiple walk-in locations? We'd like to diagnose the device and we'll need the model number to provide the most accurate repair quote. Our locations can be found at URL.";
    printHeader()
    location = ""
    while True:
        userName = input('Name (0 to exit): ')
        if userName == "0":
            break   
        model = input('Model (d for diagnose): ')
        
        if model == "d":
            template = templateDiag
            location = "all"
        else:
            template = templateOrig
            location = input('Location (3 char abbrev): ')
        
        
        price = findPrice(model)
        model = model.replace("+", " Plus")
        time = "90-day"
        if model[0] != ("s"):
            model = "iPhone " + model
            time = "1-year"
        else:
            model = model.replace("e", " Edge")
            model = "Samsung Galaxy " + model
            model = model.title()
            template = template.replace(", but many model's screens can be replaced while-you-wait.", ".")

        template = template.replace("NAME", userName)
        template = template.replace("MODEL", model)
        template = template.replace("PRICE", price)
        template = template.replace("TIME", time)
        template = template.replace("URL", findURL(location))
        print ("")
        print (price)
        print (template)
        print ("")
        print ("~~~~~")
        print ("")