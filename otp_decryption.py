import csv
pad =[]
e_message = []
message = []
inumber = 0
number = 0

def otpDecryption(e_message):
    with open('otp-5.txt') as otp:
        readotp = csv.reader(otp, delimiter = " ")
        for row in readotp:
            for i in range (len(row)):
                pad.append(row[i])




    for value in range(0 , len(e_message) ):
        
        inumber = (int(e_message[value]) - int(pad[value])*2)

        inumber = chr(inumber)

        print(inumber , end = "")
        

        
    


amount = int(input("Enter the amount of numbers there are in your encrypted message: "))
print("Enter all your numbers followed by the enter key")
for x in range (0, amount):
    number = input("")
    e_message.append(int(number))
    x = x + 1

otpDecryption(e_message)
