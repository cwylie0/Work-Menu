import glob
from PIL import Image

foregrounds = ["HomeButtonRepair.png", "HeadphoneJackRepair.png", "FrontCameraRepair.png", "BatteryReplacement.png", "DiagnosticService.png", "ChargingPortRepair.png", "LoudspeakerRepair.png", "MicrophoneRepair.png", "PowerButtonRepair.png", "EarSpeakerRepair.png", "VolumeButtonRepair.png", "WaterDamage.png", "VibrateButtonRepair.png"]

def prettyPictures():
    print ("")
    print ("*** IMAGE GENERATOR V 1.1 ***")    
    print ("")
    device = input("Enter background filename: ")

    for fg in foregrounds:
        foreground = Image.open(fg)
        background = Image.open(device)
        filename = device.replace(".png", "-") + fg
        print (filename)
        Image.alpha_composite(background, foreground).save(filename)

"""
Headphone Jack by Luke Anthony Firth from the Noun Project
micro usb by lastspark from the Noun Project
drops by Murthy2819 from the Noun Project
prettyPictures()
"""

