import random
import csv

disclaimer = "<p><strong>*NOTE: If you decline repairs for diagnostic or water damage treatment or your device is deemed non-repairable, you will be responsible for shipping and handling.</strong></p>"

videoDiv = '<div style="position: relative; padding-bottom: 56.25%; padding-top: 30px; height: 0; overflow: hidden;"><iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: block; margin-left: auto; margin-right: auto;" src="YOUTUBEURL" width="853" height="480" frameborder="0" allowfullscreen="allowfullscreen"></iframe></div>'

intro = [
    "<p>At iFixYouri, we understand that your DEVICE is very important to you. When it breaks, it can cause a lot of problems. If your MacBook Pro needs SERVICE, stick with our professional repair technicians.</p>",
    "<p>The DEVICE MacBook Pro has great build quality and design, but it isn't invincible. Since your device is of little use when broken, it's a good idea to bring it to iFixYouri for expert SERVICE.</p><p>Each device has its lifespan - some devices use higher quality components than others and can last years. However, repeated use or accidents can cause issues that require professional MacBook Pro repair technicians.</p>",
    "<p>We strongly recommend that you do not attempt MacBook Pro SERVICE yourself since devices have become sophisticated and you may cause more damage. Send your Apple DEVICE to iFixYouri to have skilled repair technicians inspect it, identify any problems it may have, and get it repaired professionally.</p>",
    "<p>Please don't try MacBook Pro SERVICE yourself. Computers have become more complex, with smaller components. You'll most likely cause more damage. Using the shipping label emailed after checkout, send your DEVICE to iFixYouri so our repair technicians can check your device, pinpoint any issues, and get them repaired the professional way.</p>"
]

diagnostic = [
    "<p>After checkout, you'll receive an email confirmation and shipping label. When your MacBook Pro arrives at our repair center, we do diagnostic tests to determine if any other issues affect your computer. Outgoing testing ensures that your DEVICE is fully functional. With the repairs complete, we send you a tracking number and ship your DEVICE back to you. So easy.</p>",
    "<p>iFixYouri offers SERVICE for MacBook Pros. With this service, we'll assess the extent of the damage, repair it, and send your DEVICE back. We'll let you know if you need further repairs, and give you the option to proceed.</p>",
    "<p>With SERVICE for DEVICE MacBook Pros, iFixYouri is here to help. Our repair technicians inspect the problem, as well as any other components, repair your device, and send it back to you quickly. If there are any other issues with your device, we'll let you know and proceed with those repairs only after your approval.</p>",
    "<p>Every repair service begins with a series of diagnostic tests to determine what the issue is. Our technicians use their repair experience to quickly diagnose the problem. In many cases, repairs are minimal; however, if we see that your DEVICE MacBook Pro has additional damage, we'll contact you before proceeding.</p>",
    "<p>Our repair technicians will begin with a diagnostic. Typically, repairs are straightforward. If we see that your DEVICE MacBook Pro has additional damage, we'll inform you and get your approval before proceeding.</p>"
]

shipping = [
    "<h3>Shipping Your DEVICE</h3><p>Send your DEVICE MacBook Pro to iFixYouri via your chosen shipping method. Please ship your device in a sturdy, secure box. If you hear it rattling around in the box, add some more padding. Please do not include cases, cables, or accessories. Standard shipping is covered by us, as well as $100 insurance. Faster shipping and extra insurance coverage can be purchased during checkout.</p>",
    "<h3>Shipping Your MacBook Pro</h3><p>Faster shipping and extra insurance options are available for purchase if you would like. When packaging your device, use a sturdy, secure box. You do not need to ship in your cases, cables, or accessories.</p>",
    "<h3>Shipping Your DEVICE</h3><p>Free shipping and $100 of insurance are included. You may purchase faster shipping options and additional insurance protection during checkout. That's up to you. Don't send us your cables, charges, or cases, please. We have plenty here already :) Just package your DEVICE MacBook Pro in a secure box and affix the provided label.</p>",
    "<h3>Shipping Your MacBook Pro</h3><p>We email you a printable shipping label, and include $100 of insurance protection. If you would like faster shipping or more insurance coverage, you have the option to upgrade during checkout. </p>"
]

warranty = [
    "<h3>Warranty: DEVICE</h3><p>A 90-day warranty that covers all but accidental damage is included. Contact customer service with any questions at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>.</p>",
    "<h3>Warranty Details</h3><p>All replacement parts come with a 90-day warranty that covers all but accidental damage.</p>",
    "<h3>DEVICE Warranty</h3><p>With every repair comes a 90-day warranty that covers all but accidental damage.</p>",
    "<h3>90-Day Warranty</h3><p>SERVICE for the DEVICE includes a 90-day warranty that covers all but accidental damage. If you notice something off about your replacement part or parts, let us know immediately. We will be happy to help.</p>", 
    "<h3>iFixYouri Warranty</h3><p>DEVICE SERVICE includes a 90-day warranty that covers everything except accidental damage. If you notice something off about your MacBook Pro, or your replacement part or parts, please let us know. We'll be glad to help.</p>"
]

questions = [
    "<h3>Questions?</h3><p>If you have specific questions about SERVICE or any DEVICE service from iFixYouri, please ask them in the box below. Contact customer service with any questions at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>.</p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>",
    "<h3>Customer Service</h3><p>Questions about SERVICE? Type them into the box below, and we'll get back to you as soon as possible. Alternatively, you can reach us at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a></p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>",
    "<h3>Questions? Just Ask.</h3><p>Do you have any questions about SERVICE from iFixYouri? Just ask them in the box below, and we'll get back to you. Alternatively, you can always reach us via our support phone number <a href=\"tel:888-494-4349\">888-494-4349</a> or email <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a></p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>",
    "<h3>We're Here to Help!</h3><p>iFixYouri can be reached at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>. Questions may be asked using the chatbot or question form below.</p><p>Please note that the computer pictured above might not match your exact model. Replacement parts will match your specific device.</p>",
    "<h3>Contact/Support</h3><p>Call iFixYouri @ <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>. You can also ask questions using the chatbot or question form below.</p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>"
]

services = {
    'Screen Repair': 529.99,
    'Keyboard Repair': 139.99,    
    'Battery Replacement': 139.99,    
    'Hinge Repair': 139.99,
    'Bottom Cover Repair': 139.99,
    'Top Cover Repair': 469.99
}

def printwriterheader():
    print("")
    print("MACBOOK SERVICE PAGE CREATOR V 2.0")
    print("----------------------------------")
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
        serviceName = screenSize + "\" MacBook Pro " + device + " " + service
        collectionName = screenSize + "\" MacBook Pro " + device + " Repair"
        cost = services[service]     
        taxRule = 9   
        tags = collectionName
        metaTitle = serviceName

        #outputFileName = device + " " + service + ".html"
        #outputFileName = outputFileName.replace(" ", "-")
        title = "<h2>" + serviceName + "</h2>"
        #shortDescription = "<strong><h4>CALL <a href=\"tel:888-494-4349\">888-494-4349</a> for latest pricing</h4></strong><br/><ul><li>90-day warranty</li><li>Excellent customer service</li><li>Expert technicians</li></ul>"
        urlRewritten = serviceName.replace(" ", "-")
        urlRewritten = urlRewritten.replace("\"", "")
        urlRewritten = urlRewritten.lower()
        metaDescription = serviceName + " performed by MacBook Pro repair experts iFixYouri. Warranty included. Call today 888-494-4349."

        #availableForOrder = 0
        #showPrice = 0

        l = []

        l.append(title)
        l.append(random.choice(intro))

        if service == "Screen Repair":
            l.append("<p>Screen or LCD Replacement is what you need if your DEVICE has a cracked display or your MacBook Pro is displaying horizontal or vertical bars, or nothing at all. Please note that some models require a top cover (lid) replacement while replacing the display. Upon diagnosing your device, a technician will inform you if any other additional repairs are needed. No additional repairs will be started without your approval.</p>")
            l.append(videoDiv.replace("YOUTUBEURL",
                                  "https://www.youtube.com/embed/tF_zuMX4ixI"))
            #imageSrc= "https://cdn.shopify.com/s/files/1/0296/6703/3181/files/MacBook ProLCDScreenReplacement.jpg?v=1605626283"          

        if service == "Keyboard Repair":
            l.append("<p>This is the service you need if your MacBook Pro's keys are not functioning properly. If you suspect your keys are not working due to water or liquid damage, please choose that service instead. If any evidence of liquid damage is found, your technician will contact you to discuss repair options. iFixYouri does not proceed with repairs discovered after diagnosis without your consent.</p>")
            #imageSrc= "https://cdn.shopify.com/s/files/1/0296/6703/3181/files/MacBook ProKeyboardReplacement.jpg?v=1605626283"            

        if service == "Hinge Repair":
            l.append("<p>This repair is for hinge replacement only. If your MacBook Pro has damage to the top or bottom cover in addition to the hinge itself, you will be contacted and an updated repair quote will be provided. We do not proceed with repair in this situation until we have your approval.</p>")
            #imageSrc= "https://cdn.shopify.com/s/files/1/0296/6703/3181/files/MacBook ProHingeReplacement.jpg?v=1605626283"            

        if service == "Battery Replacement":
            l.append("<p>Old or bad batteries can really be frustrating. You might need SERVICE if your battery does not hold charge well or charges very slowly or barely at all.</p>")
            #imageSrc= "https://cdn.shopify.com/s/files/1/0296/6703/3181/files/MacBook ProBatteryReplacement.jpg?v=1605626283"            

        if service == "Bottom Cover Repair":
            l.append("<p>This repair is for bottom cover replacement only. If your MacBook Pro has damage to the hinges or top cover in addition to the bottom cover itself, you will be contacted and an updated repair quote will be provided. We won't continue with repairs in this situation until we have your approval.</p>")
            #imageSrc= "https://cdn.shopify.com/s/files/1/0296/6703/3181/files/MacBook ProBottomCoverReplacement.jpg?v=1605626283"            

        if service == "Top Cover Replair":
            l.append("<p>This repair is for top cover replacement only. If your MacBook Pro has damage to the hinges or bottom cover in addition to the top cover, you will be contacted with an amended repair quote. Your approval will be required before we proceed with the repairs.</p>")
            #imageSrc= "https://cdn.shopify.com/s/files/1/0296/6703/3181/files/MacBook ProTopCoverReplacement.jpg?v=1605626283"            

        imageAltText = "MacBook Pro " + device + " " + service
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
    print('TITLE: ' + screenSize + '" MacBook Pro ' + device + ' Repair' )
    print('DESCRIPTION: ' + screenSize + '" MacBook Pro ' + device + ' Repair is completed by experienced iFixYouri technicians. From keyboard, hinge, LCD, and battery replacement to top or bottom cover repair.') 
    print('SEO PAGE TITLE: ' + screenSize + '" MacBook Pro ' + device + ' Repair')
    print('SEO DESCRIPTION: ' + screenSize + '" MacBook Pro ' + device + ' Repair is completed by experienced iFixYouri technicians. From keyboard, hinge, LCD, and battery replacement to top or bottom cover repair.') 
    #print('URL and HANDLE: ' + deviceURL + '-repair-services')
    #print('\n')
    #print('Upload the file below into that product collection.')
    #print("FILE CREATED: " + outputFileName)
    print('\n')


def MacBookWrite():
    printwriterheader()  
    global device
    global deviceURL
    global outputFileName 
    global screenSize 
    
    device = " "
    #device = input("ENTER DEVICE: ")
    #deviceURL = device.replace(" ", "-")
    
    devices = ["A2140"]    
    screenSize = "16"
    
    #outputFileName = deviceURL + '.csv'
    outputFileName = screenSize + "-MacBook-Pro-" + devices[0] + ".csv"

    for device in devices:
        createpages(device)
        displayoutput(device)
    
    with open(outputFileName, 'w', newline='') as myFile:
        writer = csv.writer(myFile)
        writer.writerows(a) 

MacBookWrite()

