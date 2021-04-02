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

disclaimer = "<p><strong>*NOTE: If you decline repairs for diagnostic or water damage treatment or your device is deemed non-repairable, you will be responsible for shipping and handling.</strong></p>"

videoDiv = '<div style="position: relative; padding-bottom: 56.25%; padding-top: 30px; height: 0; overflow: hidden;"><iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: block; margin-left: auto; margin-right: auto;" src="YOUTUBEURL" width="853" height="480" frameborder="0" allowfullscreen="allowfullscreen"></iframe></div>'

intro = [
    "<p>At iFixYouri, we understand. Your DEVICE is really important to you. When it breaks, it can cause problems. If you need Chromebook SERVICE, let the professional repair technicians at iFixYouri help you out.</p>",
    "<p>The DEVICE Chromebook has great build quality and design, but it isn't invincible. Since your device is of little use when broken, it's a good idea to bring it to iFixYouri for expert SERVICE.</p><p>Each device has its lifespan - some devices use higher quality components than others and can last years. However, repeated use or accidents can cause issues that require professional Chromebook repair technicians.</p>",
    "<p>We recommend not trying Chromebook SERVICE yourself. Devices have become sophisticated and you may cause more damage. Using the shipping label which we email to you after checkout, send your DEVICE to iFixYouri's mail-in center so our skilled repair technicians can inspect your device, pinpoint all/any issues affecting it, and get them repaired the professional way.</p>",
    "<p>Please don't try Chromebook SERVICE yourself. Computers have become more complex, with smaller components. You'll most likely cause more damage. Using the shipping label emailed after checkout, send your DEVICE to iFixYouri so our repair technicians can check your device, pinpoint any issues, and get them repaired the professional way.</p>"
]

diagnostic = [
    "<p>After checkout, you'll receive an email confirmation and shipping label. When your Chromebook arrives at our repair center, we do diagnostic tests to determine if any other issues affect your computer. Outgoing testing ensures that your DEVICE is fully functional. With the repairs complete, we send you a tracking number and ship your DEVICE back to you. So easy.</p>",
    "p>iFixYouri is here to solve your problem with SERVICE for DEVICE Chromebooks. With this service, we'll determine the extent of the damage, get your device repaired, and send it back to you. We'll let you know if any other issues affect your device and give you the option of proceeding with those repairs.</p>",
    "<p>With SERVICE for DEVICE Chromebooks, iFixYouri is here to help. Our repair technicians inspect the problem, as well as any other components, repair your device, and send it back to you quickly. If there are any other issues with your device, we'll let you know and proceed with those repairs only after your approval.</p>",
    "<p>Every repair service begins with a series of diagnostic tests to determine what the issue is. Our technicians use their repair experience to quickly diagnose the problem. In many cases, repairs are minimal; however, if we see that your DEVICE Chromebook has additional damage, we'll contact you before proceeding.</p>",
    "<p>Our repair technicians will begin with a diagnostic. Typically, repairs are straightforward. If we see that your DEVICE Chromebook has additional damage, we'll inform you and get your approval before proceeding.</p>"
]

shipping = [
    "<h3>Shipping Your DEVICE</h3><p>Use the calculator below to estimate shipping. Please ship your device in a sturdy, secure box. If you hear it rattling around in the box, add some more padding. Please do not include cases, cables, or accessories. Standard shipping is covered by us, as well as $100 insurance. Faster shipping and extra insurance coverage can be purchased during checkout.</p>",
    "<h3>Shipping Your Chromebook</h3><p>The shipping cost calculator below can be used to price your shipping cost. Faster shipping options and extra insurance protection are available for purchase if you'd like. When packaging your device, use a sturdy, secure box. You do not need to ship us your cases, cables, or accessories.</p>",
    "<h3>Shipping Your DEVICE</h3><p>You may purchase faster shipping options and additional insurance protection during checkout. That's up to you. Don't send us your cables, charges, or cases, please. We have plenty here already :) Just package your DEVICE Chromebook in a secure box and affix the provided label.</p>",
    "<h3>Shipping Your Chromebook</h3><p>We email you a printable shipping label, and include $100 of insurance protection. If you would like faster shipping or more insurance coverage, you have the option to upgrade during checkout. </p>"
]

warranty = [
    "<h3>Warranty: DEVICE</h3><p>A 90-day warranty that covers all but accidental damage is included. Contact customer service with any questions at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>.</p>",
    "<h3>Warranty Details</h3><p>All replacement parts come with a 90-day warranty that covers all but accidental damage.</p>",
    "<h3>DEVICE Warranty</h3><p>A 90-day warranty that covers all but accidental damage comes with every repair.</p>",
    "<h3>90-Day Warranty</h3><p>SERVICE for the DEVICE includes a 90-day warranty that covers all but accidental damage. If you notice something off about the fit, function, or performance of your replacement part or parts, let us know right away and we will be glad to help.</p>", 
    "<h3>iFixYouri Warranty</h3><p>DEVICE SERVICE includes a 90-day warranty that covers everything except accidental damage. If you notice something off about your Chromebook, or your replacement part or parts, please let us know. We'll be glad to help.</p>"
]

questions = [
    "<h3>Questions?</h3><p>If you have specific questions about SERVICE or any DEVICE service from iFixYouri, please ask them in the box below. Contact customer service with any questions at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>.</p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>",
    "<h3>Customer Service</h3><p>Questions about SERVICE? Type them into the box below, and we'll get back to you as soon as possible. Alternatively, you can reach us at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a></p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>",
    "<h3>Questions? Just Ask.</h3><p>Do you have any questions about SERVICE from iFixYouri? Just ask them in the box below, and we'll get back to you. Alternatively, you can always reach us via our support phone number <a href=\"tel:888-494-4349\">888-494-4349</a> or email <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a></p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>",
    "<h3>We're Here to Help!</h3><p>iFixYouri can be reached at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>. Questions may be asked using the chatbot or question form below.</p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>",
    "<h3>Contact/Support</h3><p>Call iFixYouri @ <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>. You can also ask questions using the chatbot or question form below.</p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>"
]

services = {
    'Screen Repair': 299.99,
    'Keyboard Repair': 299.99,    
    'Battery Replacement': 199.99,    
    'Hinge Repair': 199.99,
    'Bottom Cover Repair': 199.99,
    'Top Cover Repair': 199.99, 
    'Diagnostic Service': 0.00,
    'Water Damage Repair': 0.00
}

def printwriterheader():
    print("")
    print("CHROMEBOOK SERVICE PAGE CREATOR V 1.0")
    print("-------------------------------------")
    print("")


row = ['Handle','Title','Body (HTML)','Vendor','Type','Tags','Published','Option1 Name','Option1 Value','Option2 Name','Option2 Value','Option3 Name','Option3 Value','Variant SKU','Variant Grams','Variant Inventory Tracker','Variant Inventory Policy','Variant Fulfillment Service','Variant Price','Variant Compare At Price','Variant Requires Shipping','Variant Taxable','Variant Barcode','Image Src','Image Position','Image Alt Text','Gift Card','SEO Title','SEO Description','Variant Image','Variant Weight Unit','Variant Tax Code','Cost per item']

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
imageAltText = ""
giftCard = ''
variantImage = ''
variantWeightUnit = 'lb'
variantTaxCode = ''
costPerItem = ''
collectionName = ''
# ***************** END New STUFF

def createpages(device):
    for service in services:
        serviceName = device + " Chromebook " + service
        collectionName = device + " Chromebook Repair"
        cost = services[service]     
        taxRule = 9   
        tags = collectionName
        metaTitle = serviceName

        #outputFileName = device + " " + service + ".html"
        #outputFileName = outputFileName.replace(" ", "-")
        title = "<h2>" + serviceName + "</h2>"
        #shortDescription = "<strong><h4>CALL <a href=\"tel:888-494-4349\">888-494-4349</a> for latest pricing</h4></strong><br/><ul><li>90-day warranty</li><li>Excellent customer service</li><li>Expert technicians</li></ul>"
        urlRewritten = serviceName.replace(" ", "-")
        urlRewritten = urlRewritten.lower()
        metaDescription = serviceName + " performed by Chromebook repair experts iFixYouri. Warranty included. Call today 888-494-4349."

        #availableForOrder = 0
        #showPrice = 0

        l = []

        l.append(title)
        l.append(random.choice(intro))

        if service == "Screen Repair":
            l.append("<p>Screen or LCD Replacement is what you need if your DEVICE has a cracked display or your Chromebook is displaying horizontal or vertical bars, or nothing at all. Please note that some models require a top cover (lid) replacement while replacing the display. Upon diagnosing your device, a technician will inform you if any other additional repairs are needed. No additional repairs will be started without your approval.</p>")
            l.append(videoDiv.replace("YOUTUBEURL",
                                  "https://www.youtube.com/embed/tF_zuMX4ixI"))
            imageSrc= "https://cdn.shopify.com/s/files/1/0296/6703/3181/files/ChromebookLCDScreenReplacement.jpg?v=1605626283"
            imageAltText = device + " Chromebook LCD Replacement"

        if service == "Keyboard Repair":
            l.append("<p>This is the service you need if your Chromebook's keys are not functioning properly. If you suspect your keys are not working due to water or liquid damage, please choose that service instead. If any evidence of liquid damage is found, your technician will contact you to discuss repair options. iFixYouri does not proceed with repairs discovered after diagnosis without your consent.</p>")
            imageSrc= "https://cdn.shopify.com/s/files/1/0296/6703/3181/files/ChromebookKeyboardReplacement.jpg?v=1605626283"
            imageAltText = device + " Chromebook Keyboard Repair"

        if service == "Hinge Repair":
            l.append("<p>This repair is for hinge replacement only. If your Chromebook has damage to the top or bottom cover in addition to the hinge itself, you will be contacted and an updated repair quote will be provided. We do not proceed with repair in this situation until we have your approval.</p>")
            imageSrc= "https://cdn.shopify.com/s/files/1/0296/6703/3181/files/ChromebookHingeReplacement.jpg?v=1605626283"
            imageAltText = device + " Chromebook Hinge Replacement"

        if service == "Battery Replacement":
            l.append("<p>Old or bad batteries can really be frustrating. You might need SERVICE if your battery does not hold charge well or charges very slowly or barely at all.</p>")
            imageSrc= "https://cdn.shopify.com/s/files/1/0296/6703/3181/files/ChromebookBatteryReplacement.jpg?v=1605626283"
            imageAltText = device + " Chromebook Battery Replacement"

        if service == "Bottom Cover Repair":
            l.append("<p>This repair is for bottom cover replacement only. If your Chromebook has damage to the hinges or top cover in addition to the bottom cover itself, you will be contacted and an updated repair quote will be provided. We won't continue with repairs in this situation until we have your approval.</p>")
            imageSrc= "https://cdn.shopify.com/s/files/1/0296/6703/3181/files/ChromebookBottomCoverReplacement.jpg?v=1605626283"
            imageAltText = device + " Chromebook Bottom Cover Replacement"

        if service == "Top Cover Replair":
            l.append("<p>This repair is for top cover replacement only. If your Chromebook has damage to the hinges or bottom cover in addition to the top cover, you will be contacted with an amended repair quote. Your approval will be required before we proceed with the repairs.</p>")
            imageSrc= "https://cdn.shopify.com/s/files/1/0296/6703/3181/files/ChromebookTopCoverReplacement.jpg?v=1605626283"
            imageAltText = device + " Chromebook Top Cover Replacement"

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

        variantPrice = cost
        row = [urlRewritten, serviceName, longDescription, vendor, typeOf, tags, published, "Title", "Default Title", "", "", "", "", variantSKU, variantGrams, variantInventoryTracker, variantInventoryPolicy, variantFulFillmentService, variantPrice, variantCompareAtPrice, variantRequiresShipping, variantTaxable, variantBarcode, imageSrc, imagePosition, imageAltText, giftCard, metaTitle, metaDescription, variantImage, variantWeightUnit, variantTaxCode, costPerItem]
        a.append(row)

def displayoutput(device):    
    print('Create a collection with the following fields:')
    print('TITLE: ' + device + ' Chromebook Repair' )
    print('DESCRIPTION: ' + device + ' Chromebook Repair is completed by experienced iFixYouri technicians. From keyboard, hinge, LCD, and battery replacement to top or bottom cover repair.') 
    print('SEO PAGE TITLE: ' + device + ' Chromebook Repair')
    print('SEO DESCRIPTION: ' + device + ' Chromebook Repair is completed by experienced iFixYouri technicians. From keyboard, hinge, LCD, and battery replacement to top or bottom cover repair.') 
    #print('URL and HANDLE: ' + deviceURL + '-repair-services')
    #print('\n')
    #print('Upload the file below into that product collection.')
    #print("FILE CREATED: " + outputFileName)
    print('\n')


def chromebookWrite():
    printwriterheader()  
    global device
    global deviceURL
    global outputFileName 
    
    device = " "
    #device = input("ENTER DEVICE: ")
    #deviceURL = device.replace(" ", "-")
    
    devices = ["Acer", "Asus", "Dell", "HP", "Lenovo", "Samsung", "Toshiba"]

    #devices = ["Acer 11 C710","Acer 11 C720","Acer 11 C721-25AS","Acer 11 C730E","Acer 11 C731","Acer 11 C731T","Acer 11 C732","Acer 11 C732T","Acer 11 C733","Acer 11 C738T","Acer 11 C740","Acer 11 C771","Acer 11 C771T","Acer 11 C910","Acer 11 CB3-111","Acer 11 CB3-131","Acer 11 CB311","Acer 11 CB311-8HT","Acer 11 CB5-132T","Acer 11 R721T","Acer 11 R751T","Acer 11 R752T","Acer 13 C810","Acer 13 CB5-311","Acer 13 CB5-312T","Acer 14 CB3-431","Acer 14 CB514-1H","Acer 14 CP5-471","Acer 15 C910","Acer 15 CB3-531","Acer 15 CB3-532","Acer 15 CB5-571","Acer 15 CB515","Asus 10 C100PA", "Asus 10 C101PA", "Asus 11 C200MA","Asus 11 C201PA", "Asus 11 C202SA", "Asus 11 C204E","Asus 11 C213SA", "Asus 11 C213SA-YS02-S", "Asus 11 C223N","Asus 13 C300MA", "Asus 13 C300SA", "Asus 13 C301SA","Asus 14 C423N", "Asus 15 C523N", "Dell 11 3100", "Dell 11 3120", "Dell 11 3180", "Dell 11 3181", "Dell 11 3189", "Dell 11 5190", "Dell 11 CB1C13", "Dell 13 3380", "Dell 13 7310", "HP 11 2010 NR", "HP 11 CB2", "HP 11 G2", "HP 11 G3", "HP 11 G4", "HP 11 G4 EE", "HP 11 G5", "HP 11 G5 (Touch)", "HP 11 G5 EE", "HP 11 G6 EE", "HP 11 G7 EE", "HP 11 G7 EE Touch", "HP 11 G8 EE", "HP 11 V-Series", "HP 11 X360 2-in-1", "HP 11 X360 G1 EE", "HP 11 X360 G2 EE", "HP 11 X360 G3 EE", "HP 13 G1", "HP 14 AK-Series", "HP 14 G3", "HP 14 G4", "HP 14 G5", "HP 14 G6", "HP 14 Q-Series", "HP 14 SMB", "HP 14 X013DX", "Lenovo 11 100e", "Lenovo 11 100e Gen 2", "Lenovo 11 100S", "Lenovo 11 300e", "Lenovo 11 300e Gen 2", "Lenovo 11 500e", "Lenovo 11 500e Gen 2", "Lenovo 11 C330", "Lenovo 11 N20P", "Lenovo 11 N21", "Lenovo 11 N22 (Non-Touch)", "Lenovo 11 N22 (Touch)", "Lenovo 11 N23 (Non-Touch)", "Lenovo 11 N23 (Touch)", "Lenovo 11 N23 Yoga", "Lenovo 11e", "Lenovo 13 Thinkpad", "Lenovo 14 N42", "Lenovo 14 N42 (Touch)", "Lenovo 14e (81MH)", "Lenovo Yoga 11e","Samsung 11 XE303C12", "Samsung 11 XE310XBA", "Samsung 11 XE500C12", "Samsung 11 XE500C13", "Samsung 11 XE501C13", "Samsung 11 XE503C12", "Samsung 11 XE550C22", "Samsung 12 XE500C21", "Samsung 12 XE510C25", "Samsung 12 XE550C22", "Samsung 13 XE503C32", "Toshiba 13 CB30-A3120", "Toshiba 13 CB30-B3121", "Toshiba 13 CB30-B3122", "Toshiba 13 CB35", "Toshiba 13 CB35-B3330", "Toshiba 13 CB35-B3340", "Toshiba 13 CB35-C3300"]

    #outputFileName = deviceURL + '.csv'
    outputFileName = 'diagChromebooks.csv'

    for device in devices:
        createpages(device)
        displayoutput(device)
    
    with open(outputFileName, 'w', newline='') as myFile:
        writer = csv.writer(myFile)
        writer.writerows(a) 

chromebookWrite()

