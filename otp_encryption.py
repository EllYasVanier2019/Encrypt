import csv
from random import randint

def padCreator():
    f = open("otp-5.txt","w+")  #creates a new file with the given file name
    for i in range(500):        #prints the contents of the text file
        f.write(str(randint(0,300)))
        f.write(" ")

    f.close() #closes the instance of the file

pad = []
message = []
e_message = []

def otpEncryption(smessage):
    for letter in smessage:
        letter = ord(letter)
        message.append(letter)
    

    with open('otp-5.txt') as otp:
        readotp = csv.reader(otp, delimiter = " ")
        for row in readotp:
            for i in range (len(row)):
                pad.append(row[i])
    
    for value in range(0 , len(smessage)):
        e_message.append(message[value] + int(pad[value])*2)

    print (e_message)

    
user_message = input("Please enter a message to be encrypted: ")

padCreator()
otpEncryption(user_message)
                  
