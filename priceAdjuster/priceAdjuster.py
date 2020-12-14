"""
Device Service Page Content Generator

INPUT: user input device name
OUTPUT: .csv version of a set of unique service cateogory pages for a specific device, in the following template:

"""

import random
import csv

inboundShipping = {
    "UPS Ground Label. FREE!        ":0.00,
    "UPS 2nd Day Air Label. +$10.00 ":12.00,
    "UPS Next Day Air Label. +$20.00":22.00
}

outboundShipping = {
    "UPS Ground. FREE!        ":0.00,
    "UPS 2nd Day Air. +$13.50 ":15.50,
    "UPS Next Day Air. +$23.50":25.50
}

insurance = {
    "$100 - FREE!    ":0.00,
    "$250 - +$5.00   ":5.00,
    "$500 - +$10.00  ":10.00,
    "$750 - +$15.00  ":15.00,
    "$1,000 - +$20.00":20.00
}

def printwriterheader():
    print("")
    print("SERVICE PAGE PRICE ADJUSTER V 1.0")
    print("---------------------------------")
    print("")

# ***************** New STUFF for Shopify

option1 = 'Inbound Shipping'
option2 = 'Outbound Shipping'
option3 = 'Insurance'

# ***************** END New STUFF

def createpages(cost):   
    cost = float(cost)
    count = 0
    for outbound in outboundShipping:
        for ins in insurance:            
            for inbound in inboundShipping:
                variantPrice = cost + inboundShipping[inbound] + outboundShipping[outbound] + insurance[ins]     
                print(inbound, outbound, ins, variantPrice)  
                if count == 14:
                    print('-----------------')
                    count = 0
                else:
                    count = count + 1                                   
                         
def adjust():
    printwriterheader() 
    global cost  
    cost = input("ENTER COST: ")   
    createpages(cost)