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
    "<p>&nbsp;</p><p>iFixYouri understands how important your DEVICE is to you, and how unfortunate it is to find it broken. If you need SERVICE from a team of reliable and professional technicians, look no further than iFixYouri.</p>",
    "<p>&nbsp;</p><p>Even though the DEVICE has great quality, it is not indestructible. Since broken devices are of little use, you should bring your DEVICE to iFixYouri for expert SERVICE.</p><p>&nbsp;<p>The longevity of your device depends on the quality of its parts. When properly maintained, some devices last longer than others, while others can be damaged if dropped or submerged in liquid.</p>",
    "<p>&nbsp;</p><p>It is recommended that you don’t try SERVICE for yourself. It's more complicated now to fix devices, so you may end up causing more damage. With the shipping label provided, mail your DEVICE to iFixYouri's mail-in center for our skilled repair technicians to look over the device and diagnose any problems with it, so that it can be repaired professionally.</p>",
    "<p>&nbsp;</p><p>We recommend not trying SERVICE yourself. Devices have become more and more sophisticated and you may cause more damage. Using the supplied shipping label, send your DEVICE to iFixYouri's mail-in center so our skilled repair technicians can inspect your device, pinpoint all/any issues affecting it, and get them repaired the professional way.</p>"
]

diagnostic = [
    "<p>&nbsp;</p><p>After checkout, you'll receive an email confirmation and shipping label. When your phone arrives at our repair center, we do diagnostic tests to determine if any other issues are at play. Outgoing testing ensures that your DEVICE is fully functional. With the repairs complete, we send you a tracking number and ship your DEVICE back to you!</p>",
    "<p>&nbsp;</p><p>iFixYouri is here to solve your problem with SERVICE for DEVICE. With this service, we'll determine the extent of the damage, get your device repaired, and send it back to you. We'll let you know if there are any other issues affecting your device and give you the option of proceeding with those repairs.</p>",
    "<p>&nbsp;</p><p>With SERVICE for DEVICE, iFixYouri is here to help. With this service, our repair technicians inspect the problem, as well as any other affected components, repair your device, and send it back to you asap. If there are any other issues affecting your device, we'll let you know and proceed with those repairs only after your approval.</p>",
    "<p>&nbsp;</p><p>A shipping label and email confirmation will be sent to you after checkout. We run diagnostic tests on your phone when it arrives at our repair center to determine if there are any other problems. The DEVICE is thoroughly tested before we ship it back to you. Once the repairs are complete, we provide you with a tracking number to track the shipment back to you!</p>",
    "<p>&nbsp;</p><p>iFixYouri is here to resolve the problem for your DEVICE with SERVICE. In this service, we will assess the extent of the damage, repair your device, and return it to you. You will be informed if there are other problems with your device and you can choose whether to proceed with those repairs.</p>",
    "<p>&nbsp;</p><p>iFixYouri is here to help you with SERVICE for your DEVICE. This service includes a full inspection of your device and any other damaged components, repairs by our expert technicians, and secure shipping to you as soon as it is ready. We will let you know about any additional issues affecting your device and repair them only after you approve.</p>",
    "<p>&nbsp;</p><p>Every repair service begins with a series of diagnostic tests to determine what the issue is. Our technicians use their repair experience to quickly diagnose the problem. In most cases, repairs are minimal; however, if we see that your DEVICE has additional damage, we'll contact you before proceeding.</p>",
    "<p>&nbsp;</p><p>We begin every repair service with a series of diagnostic tests to determine what the problem is. Our technicians use their extensive repair experience to swiftly diagnose the problem. It is important to note that most repairs are minor, however, if we notice more damage to your DEVICE, we will contact you prior to carrying out further repairs.</p>"
]

shipping = [
    "<h3>Shipping Your DEVICE</h3><p>Use the calculator below to estimate shipping. Please ship your device in a sturdy, secure box. If you hear it rattling around in the box, add some more padding. Please do not include cases, cables, or accessories. Standard shipping is covered by us, as well as $100 insurance. Faster shipping and extra insurance coverage can be purchased during checkout.</p>",
    "<h3>Shipping Your DEVICE</h3><p>To estimate shipping, use the calculator below. We advise you to ship your device in a sturdy and secure box. If it sounds like it is rattling, add some additional padding. You should not include any cases, cables, or accessories. Standard shipping and $100 insurance are included; faster shipping and extra insurance can be purchased at checkout.</p>",
    "<h3>Shipping Your DEVICE</h3><p>To estimate your shipping costs, please use the shipping cost calculator below. Additional insurance protection and fast shipping options are available for purchase. When packaging your device, make sure you use a strong, secure box. Your cases, cables, and other accessories should not be shipped to us.</p>",
    "<h3>Shipping Your DEVICE</h3><p>Additional shipping protection and faster shipping options are available during checkout. That’s all up to you. You don't need to send us its charging cables, cases, or other accessories. We have plenty here already! The DEVICE should be packaged in a secure box and the label should be affixed.</p>",
    "<h3>Shipping Your DEVICE</h3><p>We email a printable shipping label for your use, plus we include $100 in insurance coverage. If you would like faster shipping or more insurance coverage, you may upgrade your order during checkout.</p>",
    "<h3>How do I ship my DEVICE?</h3><p>The shipping cost calculator below can be used to price your shipping cost. Faster shipping options and extra insurance protection are available for purchase if you'd like. When packaging your device, use a sturdy, secure box. You do not need to ship us your cases, cables, or accessories.</p>",
    "<h3>Shipping Your DEVICE</h3><p>You may purchase faster shipping options and additional insurance protection during checkout. That's up to you. Don't send us your cables, charges, or cases, please. We have plenty here already :) Just package your DEVICE Chromebook in a secure box and affix the provided label.</p>",
    "<h3>How to Ship Your DEVICE</h3><p>We email you a printable shipping label, and include $100 of insurance protection. If you would like faster shipping or more insurance coverage, you have the option to upgrade during checkout. </p>"
]

warranty = [
    "<h3>Warranty: DEVICE</h3><p>A DURATION warranty that covers all but accidental damage is included. Contact customer service with any questions at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>.</p>",
    "<h3>Warranty: DEVICE</h3><p>A DURATION warranty is included that covers all but accidental damage. You may contact customer service for further information at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>.</p>",
    "<h3>Warranty Details</h3><p>All replacement parts come with a DURATION warranty that covers all but accidental damage.</p>",
    "<h3>DEVICE Warranty</h3><p>A DURATION that covers all but accidental damage comes with every repair.</p>",
    "<h3>Warranty Details</h3><p>All replacement parts come with a DURATION warranty covering all damage except accidental damage.</p>",
    "<h3>DEVICE Warranty</h3><p>Every repair comes with a DURATION covering all but accidental damage.</p>",
    "<h3>DURATION Warranty</h3><p>A DURATION warranty covers all but accidental damage for the DEVICE. We will be glad to help if you notice something off about your replacement part, function, or performance. We just ask that you reach out to us as soon as possible.</p>", 
    "<h3>DURATION Warranty</h3><p>SERVICE for the DEVICE includes a DURATION warranty that covers all but accidental damage. If you notice something off about the fit, function, or performance of your replacement part or parts, let us know right away and we will be glad to help.</p>", 
    "<h3>iFixYouri Warranty</h3><p>DEVICE SERVICE includes a DURATION warranty that covers everything except accidental damage. If you notice something off about your Chromebook, or your replacement part or parts, please let us know. We'll be glad to help.</p>",
    "<h3>iFixYouri Warranty</h3><p>A DURATION warranty is built into DEVICE SERVICE, and it covers everything except accidental damage. We will be happy to assist you if you notice any problems with your device or replacement parts.</p>"
]

questions = [
    "<h3>Questions?</h3><p>If you have specific questions about SERVICE or any DEVICE service from iFixYouri, please ask them in the box below. Contact customer service with any questions at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>.</p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>",
    "<h3>Customer Service</h3><p>Questions about SERVICE? Type them into the box below, and we'll get back to you as soon as possible. Alternatively, you can reach us at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a></p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>",
    "<h3>Questions?</h3><p>In the box below, please post your questions about SERVICE or any DEVICE services from iFixYouri. Contact customer service at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>.</p><p>NOTE: This computer may not necessarily match the exact model you own. Your replacement part or parts will match your device.</p>",
    "<h3>Customer Service</h3><p>If you have a question about SERVICE, please enter it below, and we'll get back to you shortly. Otherwise, you can reach us at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a></p><p>NOTE: The computer shown above may not match your exact model. Your replacement part will match your specific device.</p>",
    "<h3>Questions? Just Ask.</h3><p>Have any questions about SERVICE from iFixYouri? Just ask them in the box below, and we'll get back to you asap. On the other hand, you can always reach us via our support phone number <a href=\"tel:888-494-4349\">888-494-4349</a> or email <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a></p><p>NOTE: You will be receiving your replacement part or parts based on your exact model. The computer pictured above may not correspond to your exact model.</p>",
    "<h3>Questions? Just Ask.</h3><p>Is there anything you need to know about SERVICE from iFixYouri? Feel free to ask us in the box below, and we'll get back to you. Alternatively, you can always reach us via our support phone number <a href=\"tel:888-494-4349\">888-494-4349</a> or email <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a></p><p>NOTE: Your replacement part or parts will be tailored to your specific device. The computer pictured above may not match your exact model.</p>",
    "<h3>Contact/Support</h3><p>Call iFixYouri @ <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>. If you have any questions, you can write them down in the chatbot below.</p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>",
    "<h3>Questions? Just Ask.</h3><p>Do you have any questions about SERVICE from iFixYouri? Just ask them in the box below, and we'll get back to you. Alternatively, you can always reach us via our support phone number <a href=\"tel:888-494-4349\">888-494-4349</a> or email <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a></p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>",
    "<h3>We're Here to Help!</h3><p>iFixYouri can be reached at <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>. Questions may be asked using the chatbot or question form below.</p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>",
    "<h3>Contact/Support</h3><p>Call iFixYouri @ <a href=\"tel:888-494-4349\">888-494-4349</a> or <a href=\"mailto:support@ifixyouri.com\">support@ifixyouri.com</a>. You can also ask questions using the chatbot or question form below.</p><p>NOTE: Computer pictured above may not necessarily match your exact model. Your replacement part or parts will match your specific device.</p>"
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
    print("DEVICE SERVICE PAGE CREATOR V 5.5")
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
        if "iPad" in device:
            longDescription = longDescription.replace("DURATION", "one-year")
        if "iPhone" in device:
            longDescription = longDescription.replace("DURATION", "one-year")
        else:
            longDescription = longDescription.replace("DURATION", "90-day")

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

