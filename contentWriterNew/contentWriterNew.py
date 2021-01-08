"""
Device Service Page Content Generator

INPUT: user input device name
OUTPUT: .csv version of a set of unique service cateogory pages for a specific device, in the following template:

optional video, h2 title, optional disclaimer, intro paragraph, diagnostic paragraph, shipping paragraph, warranty paragraph

POSSIBLE EDITS: Replace 90-day with 1-year for device contains iPad or iPhone
lowercase handle
add collections

"""

import random
import csv

servicesB = {
    'Diagnostic Service', 'Glass Repair', 'Glass & LCD Repair', 'Battery Replacement', 'Charging Port Repair', 'Front Camera Repair', 'Headphone Jack Repair', 'Home Button Repair', 'Loud Speaker Repair', 'Microphone Repair', 'Power Button Repair', 'Rear Camera Repair', 'Volume Button Repair', 'Water Damage Repair'
}
disclaimer = "<p>&nbsp;</p><p><strong>*NOTE: If you decline repairs for diagnostic or water damage treatment or your device is deemed non-repairable, you will be responsible for shipping and handling.</strong></p>"

videoDiv = '<div style="position: relative; padding-bottom: 56.25%; padding-top: 30px; height: 0; overflow: hidden;"><iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: block; margin-left: auto; margin-right: auto;" src="YOUTUBEURL" width="853" height="480" frameborder="0" allowfullscreen="allowfullscreen"></iframe></div><p>&nbsp;</p>'

intro = [
    "<p>&nbsp;</p><p>At iFixYouri, we understand. Your DEVICE is really important to you. When it breaks, it can really mess up your day. If you are in need of SERVICE, let the professional repair technicians at iFixYouri help you out.</p>",
    "<p>&nbsp;</p><p>The DEVICE has great build quality and design, but it isn't invincible. Since your device is of little use when broken, it's a good idea to bring it to iFixYouri for expert SERVICE.</p><p>&nbsp;<p>Each device has its own lifespan - some devices use higher quality components than others and can last years if properly maintained. Drops, water or liquid, even a jolt can damage your device. </p>",
    "<p>&nbsp;</p><p>We recommend not trying SERVICE yourself. Devices have become more and more sophisticated and you may cause more damage. Using the supplied shipping label, send your DEVICE to iFixYouri's mail-in center so our skilled repair technicians can inspect your device, pinpoint all/any issues affecting it, and get them repaired the professional way.</p>"
]

diagnostic = [
    "<p>&nbsp;</p><p>After checkout, you'll receive an email confirmation and shipping label. When your phone arrives at our repair center, we do diagnostic tests to determine if any other issues are at play. Outgoing testing ensures that your DEVICE is fully functional. With the repairs complete, we send you a tracking number and ship your DEVICE back to you!</p>",
    "<p>&nbsp;</p><p>iFixYouri is here to solve your problem with SERVICE for DEVICE. With this service, we'll determine the extent of the damage, get your device repaired, and send it back to you. We'll let you know if there are any other issues affecting your device and give you the option of proceeding with those repairs.</p>",
    "<p>&nbsp;</p><p>With SERVICE for DEVICE, iFixYouri is here to help. With this service, our repair technicians inspect the problem, as well as any other affected components, repair your device, and send it back to you asap. If there are any other issues affecting your device, we'll let you know and proceed with those repairs only after your approval.</p>",
    "<p>&nbsp;</p><p>Every repair service begins with a series of diagnostic tests to determine what the issue is. Our technicians use their repair experience to quickly diagnose the problem. In most cases, repairs are minimal; however, if we see that your DEVICE has additional damage, we'll contact you before proceeding.</p>"
]

shipping = [
    "<p>&nbsp;</p><p>Send your DEVICE to iFixYouri via the UPS shipping method of your choosing. Please ship your device in a sturdy, secure box. If you hear it rattling around in the box, add some more padding. Please do not include cases, cables, or accessories. Standard UPS Ground is covered by us, as well as $100 insurance. Faster shipping and extra insurance coverage can be purchased using the drop-down boxes above.</p>",
    "<p>&nbsp;</p><p>Faster shipping options and extra insurance protection are available for purchase if you'd like. Simply choose from the drop-downs before adding to your shopping cart. When packaging your device, use a sturdy, secure box. You do not need to ship us your cases, cables, or accessories.</p>",
    "<p>&nbsp;</p>Free UPS ground shipping and $100 of insurance are included. You may purchase faster shipping options and additional insurance protection using the drop-down options above. That's up to you. Don't send us your cables, charges, or cases please. We have plenty here already :) Just package your DEVICE in a secure box and affix the provided label.</p>",
    "<p>&nbsp;</p><p>We email you a printable shipping label, and include $100 of insurance protection. If you would like faster shipping or more insurance coverage, you have the option to upgrade above using the drop-downs. </p>"
]

warranty = [
    "<p>&nbsp;</p><p>A 90-day warranty that covers all but accidental damage is included. Contact customer service with any questions at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>.</p>",
    "<p>&nbsp;</p><p>All replacement parts come with a 90-day warranty that covers all but accidental damage.</p>",
    "<p>&nbsp;</p><p>A 90-day warranty that covers all but accidental damage comes with every repair.</p>",
    "<p>&nbsp;</p><p>SERVICE repair includes a 90-day warranty that covers all but accidental damage. If you notice something off about the fit, function, or performance of your replacement part or parts, let us know right away and we will be glad to help.</p>"
]

questions = [
    "<p>&nbsp;</p><p>If you have specific questions about SERVICE or any DEVICE service from iFixYouri, please ask them in the box below. Contact customer service with any questions at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>.</p>",
    "<p>&nbsp;</p><p>Questions about SERVICE? Type them into the box below, and we'll get back to you as soon as possible. Alternatively, you can reach us at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a></p>",
    "<p>&nbsp;</p><p>Do you have any questions about SERVICE from iFixYouri? Just ask them in the box below, and we'll get back to you. Alternatively, you can always reach us via our support phone number <a href=\"tel:888-494-4349\">888-494-4349</a> or email <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a></p>",
    "<p>&nbsp;</p><p>iFixYouri can be reached at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>. Get your DEVICE working like new with the help of experienced technicians who do the job right the first time, and save yourself a lot of money and hassle.</p>"
]

'''
FULL SERVICE LIST

services = {
    'Diagnostic Service': 0.00,'Glass Repair': 249.99,'Glass & LCD Repair': 269.99,'Battery Replacement': 79.99,'Charging Port Repair': 79.99,'Front Camera Repair': 99.99,'Headphone Jack Repair': 49.99,'Home Button Repair': 49.99,'Loud Speaker Repair': 49.99,'Microphone Repair': 49.99,'Power Button Repair': 49.99,'Rear Camera Repair': 49.99,'Volume Button Repair': 49.99,'Water Damage Repair': 0.00,'Ear Speaker Repair': 49.99,'Vibrate Switch Repair': 49.99
}
'''

services = {
    'Diagnostic Service': 0.00,
    'Glass Repair': 349.99,
    'Glass & LCD Repair': 369.99,
    'Battery Replacement': 99.99,
    'Charging Port Repair': 79.99,
    'Front Camera Repair': 99.99,
    'Loud Speaker Repair': 79.99,
    'Microphone Repair': 89.99,
    'Power Button Repair': 99.99,
    'Rear Camera Repair': 129.99,
    'Volume Button Repair': 99.99,
    'Water Damage Repair': 0.00,
    'Ear Speaker Repair': 79.99,
    'Vibrate Switch Repair': 99.99
}

inboundShipping = {
    "Email me a UPS Ground Label. FREE!":0.00,
    "Email me a UPS 2nd Day Air Label. +$10.00":10.00,
    "Email me a UPS Next Day Air Label. +$20.00":20.00
}

outboundShipping = {
    "Ship my device back to me UPS Ground. FREE!":0.00,
    "Ship my device back to me UPS 2nd Day Air. +$13.50":13.50,
    "Ship my device back to me UPS Next Day Air. +$23.50":23.50
}

insurance = {
    "$100 - FREE!":0.00,
    "$250 - +$5.00":5.00,
    "$500 - +$10.00":10.00,
    "$750 - +$15.00":15.00,
    "$1,000 - +$20.00":20.00
}


def printwriterheader():
    print("")
    print("DEVICE SERVICE PAGE CREATOR V 5.0")
    print("---------------------------------")
    print("")


row = ['Handle','Title','Body (HTML)','Vendor','Type','Tags','Published','Option1 Name','Option1 Value','Option2 Name','Option2 Value','Option3 Name','Option3 Value','Variant SKU','Variant Grams','Variant Inventory Tracker','Variant Inventory Policy','Variant Fulfillment Service','Variant Price','Variant Compare At Price','Variant Requires Shipping','Variant Taxable','Variant Barcode','Image Src','Image Position','Image Alt Text','Gift Card','SEO Title','SEO Description','Variant Image','Variant Weight Unit','Variant Tax Code','Cost per item']
# row = ['Handle','Title','Body (HTML)','Vendor','Type','Tags','Published','Option1 Name','Option1 Value','Option2 Name','Option2 Value','Option3 Name','Option3 Value','Variant SKU','Variant Grams','Variant Inventory Tracker','Variant Inventory Policy','Variant Fulfillment Service','Variant Price	Variant Compare At Price','Variant Requires Shipping','Variant Taxable','Variant Barcode','Image Src','Image Position','Image Alt Text','Gift Card','SEO Title','SEO Description','Google Shopping / Google Product Category','Google Shopping / Gender','Google Shopping / Age Group','Google Shopping / MPN','Google Shopping / AdWords Grouping','Google Shopping / AdWords Labels','Google Shopping / Condition','Google Shopping / Custom Product','Google Shopping / Custom Label 0','Google Shopping / Custom Label 1','Google Shopping / Custom Label 2','Google Shopping / Custom Label 3','Google Shopping / Custom Label 4','Variant Image','Variant Weight Unit','Variant Tax Code','Cost per item']
a = []
a.append(row)

# ***************** New STUFF for Shopify

published = 'TRUE'
vendor = 'iFixYouri'
typeOf = ''
option1 = 'Inbound Shipping'
option2 = 'Outbound Shipping'
option3 = 'Insurance'
variantSKU = ''
variantGrams = 0
variantInventoryTracker = ''
variantInventoryPolicy = 'continue'
variantFulFillmentService = 'manual'
variantCompareAtPrice = ''
variantRequiresShipping = 'TRUE'
variantTaxable = 'TRUE'
variantBarcode = ''
imageSrc = ''
imagePosition = ''
imageAltText = ''
giftCard = ''
variantImage = ''
variantWeightUnit = 'lb'
variantTaxCode = ''
costPerItem = ''
collectionName = ''
# ***************** END New STUFF

def createpages(device):
    for service in services:
        serviceName = device + " " + service
        collectionName = device + " Repair"
        cost = services[service]     
        taxRule = 9   
        tags = collectionName
        metaTitle = serviceName

        outputFileName = device + " " + service + ".html"
        outputFileName = outputFileName.replace(" ", "-")
        title = "<h2>" + serviceName + "</h2>"
        shortDescription = "<strong><h4>CALL <a href=\"tel:888-494-4349\">888-494-4349</a> for latest pricing</h4></strong><br/><ul><li>90-day warranty</li><li>Excellent customer service</li><li>Expert technicians</li></ul>"
        urlRewritten = serviceName.replace(" ", "-")
        urlRewritten = urlRewritten.lower()
        metaDescription = serviceName + " performed by repair experts iFixYouri. Warranty included. Call today 888-494-4349."

        availableForOrder = 0
        showPrice = 0

        l = []

        if service == "Water Damage Repair":
            shortDescription = shortDescription.replace('<li>90-day warranty</li>', '')
            l.append(videoDiv.replace("YOUTUBEURL", "https://www.youtube.com/embed/GfawakMoM9E?rel=0"))

        if service == "Diagnostic Service":
            shortDescription = shortDescription.replace('<li>90-day warranty</li>', '')
            l.append(videoDiv.replace("YOUTUBEURL", "https://www.youtube.com/embed/9z61L7QyDVo"))

        if service == "Glass Repair":
            l.append(videoDiv.replace("YOUTUBEURL",
                                  "https://www.youtube.com/embed/1vrnuazxPIo"))

        if service == "Glass & LCD Repair":
            l.append(videoDiv.replace("YOUTUBEURL",
                                  "https://www.youtube.com/embed/tF_zuMX4ixI"))

        l.append(title)
        l.append(random.choice(intro))

        if service == "Diagnostic Service" or service == "Water Damage Repair":
            l.append(disclaimer)
            availableForOrder = 1
            showPrice = 1

        if service == "Water Damage Repair":
            l.append(" Water Damage repair is what you need if you have splashed or submerged your DEVICE in water or any other liquid. iFixYouri has a high success rate restoring devices that have lost power or function after coming in contact with liquid.")

        if service == "Diagnostic Service":
            l.append(" This is the service you need if you aren't quite sure what the problem with your DEVICE is. We'll find out what is going on, and contact you with a repair quote.")

        if service == "Glass Repair":
            l.append(" Those who have both cracked glass and a broken LCD should opt for our DEVICE Glass & LCD Repair. This service is for glass breakage only.")

        if service == "Glass & LCD Repair":
            l.append(" Those who have only cracked glass, NOT a broken LCD, should opt for our DEVICE Glass Repair. This service is for both cracked glass and a broken LCD.")

        if service == "Battery Replacement":
            l.append(" Old or bad batteries can really be frustrating. You might need SERVICE if your battery does not hold charge well or charges very slowly or barely at all.")

        if service == "Charging Port Repair":
            l.append(" Charging port repair may be what you need if your device is charging slowly or not at all. Sometimes the battery needs replacement. Whatever the case, the professional technicians at iFixYouri can help.")

        l.append(random.choice(diagnostic))
        l.append(random.choice(shipping))
        if service == "Diagnostic Service" or service == "Water Damage Repair":
            print("")
        else:
            l.append(random.choice(warranty))
        l.append(random.choice(questions))

        longDescription = ''.join(l)
        longDescription = longDescription.replace("SERVICE", service)
        longDescription = longDescription.replace("DEVICE", device)

        """
        for outbound in outboundShipping:
            for ins in insurance:            
                for inbound in inboundShipping:
                    variantPrice = cost + inboundShipping[inbound] + outboundShipping[outbound] + insurance[ins]
                    #print(format(subtotal, '.2f'))
                    #sum = sum + 1
                    if (inboundShipping[inbound] + outboundShipping[outbound] + insurance[ins]) == 0:
                        row = [urlRewritten, serviceName, longDescription, vendor, typeOf, tags, published, option1, inbound, option2, outbound, option3, ins, variantSKU, variantGrams, variantInventoryTracker, variantInventoryPolicy, variantFulFillmentService, variantPrice, variantCompareAtPrice, variantRequiresShipping, variantTaxable, variantBarcode, imageSrc, imagePosition, imageAltText, giftCard, metaTitle, metaDescription, variantImage, variantWeightUnit, variantTaxCode, costPerItem]
                    else:
                        row = [urlRewritten, '', '', '', '', '', '', '', inbound, '', outbound, '', ins, variantSKU, variantGrams, variantInventoryTracker, variantInventoryPolicy, variantFulFillmentService, variantPrice, variantCompareAtPrice, variantRequiresShipping, variantTaxable, variantBarcode, imageSrc, '', imageAltText, '', '', '', variantImage, variantWeightUnit, variantTaxCode, costPerItem] 
                    a.append(row)        
        """
        variantPrice = cost
        row = [urlRewritten, serviceName, longDescription, vendor, typeOf, tags, published, "Title", "Default Title", "", "", "", "", variantSKU, variantGrams, variantInventoryTracker, variantInventoryPolicy, variantFulFillmentService, variantPrice, variantCompareAtPrice, variantRequiresShipping, variantTaxable, variantBarcode, imageSrc, imagePosition, imageAltText, giftCard, metaTitle, metaDescription, variantImage, variantWeightUnit, variantTaxCode, costPerItem]
        a.append(row)

def displayoutput(device):    
    print('Create a collection with the following fields:')
    print('TITLE: ' + device + ' Repair' )
    print('DESCRIPTION: ' + device + ' Repair completed by experienced iFixYouri technicians. From broken screens to water damage, battery replacement and more.') 
    print('SEO PAGE TITLE: ' + device + ' Repair')
    print('SEO DESCRIPTION: ' + device + ' Repair completed by experienced iFixYouri technicians. From broken screens to water damage, battery replacement and more.') 
    
    print('URL and HANDLE: ' + deviceURL + '-repair')
    print('\n')
    print('Upload the file below into that product collection.')
    print("FILE CREATED: " + outputFileName)
    print('\n')


def runtings():
    printwriterheader()  
    global device
    global deviceURL
    global outputFileName 
    
    device = " "
    device = input("ENTER DEVICE: ")
    
    deviceURL = device.replace(" ", "-")
    outputFileName = deviceURL + '.csv'
    createpages(device)
    displayoutput(device)
    with open(outputFileName, 'w', newline='') as myFile:
        writer = csv.writer(myFile)
        writer.writerows(a) 

