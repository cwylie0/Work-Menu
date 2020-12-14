from pprint import pprint

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

option1 = 'Inbound Shipping'
option2 = 'Outbound Shipping'
option3 = 'Insurance'

row = ['Option1 Name','Option1 Value','Option2 Name','Option2 Value','Option3 Name','Option3 Value','Variant Price']

a = []
a.append(row)

cost = 39.99

for outbound in outboundShipping:
    for ins in insurance: 
        for inbound in inboundShipping:                           
            variantPrice = cost + inboundShipping[inbound] + outboundShipping[outbound] + insurance[ins]
           
            row = [inboundShipping[inbound], outboundShipping[outbound], insurance[ins], variantPrice] 
            print(row)  