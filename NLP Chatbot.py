import speech_recognition as sr#library
#function for voice to text
def speech():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            t=r.recognize_google(audio)
            return t
        except:
             return None
# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
def audio(mytext):
    # Language in which you want to convert
    language = 'en'
    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)
    return myobj
#function for criteria match
def criteria(member):
    if int(member)<=3:
        mytext="Need to check for the villa but 1,2,3 BHK are available sir\madam"
        myobj=audio(mytext)
        myobj.save("4.mp3")
        os.system("4.mp3")
    elif ((int(member)>=3) | (int(member)<=10)):
        mytext=" Need to check for the villa but 1,2,3 BHK are available sir\madam"
        myobj=audio(mytext)
        myobj.save("5.mp3")
        os.system("5.mp3")
    else:
        mytext=" Villa is available and 1,2,3 BHK is not available sir\madam"
        myobj=audio(mytext)
        myobj.save("6.mp3")
        os.system("6.mp3")
#main function
#code for name function
mytext="Welcome to Guvi Hotel sir or madam"
myobj=audio(mytext)
myobj.save("welcome.mp3")
os.system("welcome.mp3")
name=speech()
#code for phone number
mytext=" sir or madam can you please say the 10 digit Phone Number"
myobj=audio(mytext)
myobj.save("phonenumber.mp3")
os.system("phonenumber.mp3")
phone_number=speech()
#code for address
mytext= "Please provide the Address(City name)"
myobj=audio(mytext)
myobj.save("address.mp3")
os.system("address.mp3")
address=speech()
#code for id_proof
mytext="Do you have any id proof for verification"
myobj=audio(mytext)
myobj.save("proof.mp3")
os.system("proof.mp3")
id_proof=speech()
#code for room_type
mytext="What kind of rooms are you looking sir/madam We have 1BHK or 2BHK or 3BHK or Villa are available"
myobj=audio(mytext)
myobj.save("room.mp3")
os.system("room.mp3")
room_type=speech()
#code for arrival date
mytext="Can you confirm the arrival date sir/madam"
myobj=audio(mytext)
myobj.save("arrivaldate.mp3")
os.system("arrivaldate.mp3")
date=speech()
#code for group of member
mytext=" Member coming sir/madam"
myobj=audio(mytext)
myobj.save("member.mp3")
os.system("member.mp3")
Member=speech()
#code for depature date
mytext=" can you confirm your Depature Date sir/madam "
myobj=audio(mytext)
myobj.save("depaturedate.mp3")
os.system("depaturedate.mp3")
depature_date=speech()
#final segment for confirmation ogf booking
mytext="To confirm the booking please press 1 or want to wait for the room press 2 or any queries please press any"
myobj=audio(mytext)
myobj.save("booking.mp3")
os.system("booking.mp3")
a=input("To confirm the booking please press 1 or want to wait for the room press 2 or any queries please press any:")
if a=="1":
    mytext="Thanks for Booking Happy vacation\n Thank you please visit again"
    myobj=audio(mytext)
    myobj.save("1.mp3")
    os.system("1.mp3")
elif a=="2":
    mytext="We are extremly sorry for this and we hope the waiting will be sort out quickly \nThank you please visit again"
    myobj=audio(mytext)
    myobj.save("2.mp3")
    os.system("2.mp3")
else:
    mytext="Please contact xyz@xyz.com for queries or please contact xxxxxxxxxx for any queries \n Thank you please visit again"
    myobj=audio(mytext)
    myobj.save("3.mp3")
    os.system("3.mp3")
