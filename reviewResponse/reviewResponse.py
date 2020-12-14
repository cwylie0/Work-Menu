import random

responseChoices = ['Hey, thanks for your FEEDBACK, NAME :) We know a broken device is no fun, but we\'re GLAD you had a positive repair experience at iFixYouri LOCATION.', 'NAME, thanks for choosing iFixYouri LOCATION. We hope you have a great day. Please keep us in mind if you need repair help FUTURE.', 'Thanks for the FEEDBACK, NAME. Have a great day and keep us in mind if you need some smartphone, tablet, or computer repair help FUTURE. Our goal is to make customers happy.', 'So GLAD you chose iFixYouri LOCATION, NAME. Repair is our passion and we\'re glad we could help you.', 'We thank you for your FEEDBACK, NAME. Whenever you need a repair, please remember us at iFixYouri LOCATION. Have a good day :D', 'Thank you for being our customer, NAME. We are so GLAD you had a pleasant repair experience at iFixYouri LOCATION. Call us or stop by anytime if you have any issues.', 'NAME, iFixYouri LOCATION is GLAD you enjoyed your repair experience. We hope you don\'t need us too soon, but keep us in mind if you need smartphone, tablet, or computer help FUTURE.','Thanks for the FEEDBACK, NAME. The staff at iFixYouri LOCATION appreciates the kudos. Have a great day.', 'We at iFixYouri LOCATION appreciate your feedback, NAME. We hope you have a great day!', 'Hi, NAME. We really appreciate your business and your FEEDBACK. We know broken devices can be a pain. iFixYouri LOCATION hopes you have an awesome day and please let us know if you need repair help FUTURE.', 'iFixYouri LOCATION thanks you for your FEEDBACK, NAME. Please keep us in mind for future repair needs.']

upsetChoices = ["I apologize for your inconvenience, NAME. We would like to look up your account so someone can reach out to you to hopefully resolve this situation. Please contact our support team directly at 888-494-4349 or support@ifixyouri.com so they may reference your specific repair ticket.", "NAME, we are sorry to hear you had a bad experience. Please let us know via 888-494-4349 or support@ifixyouri.com which name you checked in with, and we will have management contact you. We apologize for your inconvenience."]

futureChoices = ['in the future', 'with future issues', 'at any time']

gladChoices = ['glad', 'happy', 'pleased']

def printHeader():
	print ("")
	print ("*** 5-STAR REVIEW RESPONDER V 3.3 ***")
	print ("")

def composeResponse(response, name, feedback, location, future, glad):
    finalResponse = response.replace('NAME', name)
    finalResponse = finalResponse.replace('FEEDBACK', feedback)
    finalResponse = finalResponse.replace('LOCATION', location)
    finalResponse = finalResponse.replace('FUTURE', future)
    finalResponse = finalResponse.replace('GLAD', glad)
    return finalResponse   

def generateResponse():
    printHeader()
    while True:
        response = random.choice(responseChoices)
        future = random.choice(futureChoices)
        glad = random.choice(gladChoices)

        name = input("Enter reviewer name (0 to exit): ")
        name = name.capitalize()
        if name == "0":
            break
        
        location = input("Enter location: ")
        location = location.title()
        
        feed = input("Enter re(v)iew or ra(t)ing (1 for 1-star): ")
        if feed == "v":
            feedback = "review"
            final = composeResponse(response, name, feedback, location, future, glad)
        elif feed == "t":
            feedback = "rating"
            final = composeResponse(response, name, feedback, location, future, glad)
        else:
            feedback = ""
            response = random.choice(upsetChoices)      
            final = composeResponse(response, name, feedback, location, future, glad)  

        print ("")
        print (final)
        print ("")
        print ("~~~~~")
        print ("")