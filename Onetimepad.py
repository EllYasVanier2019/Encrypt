import csv
from random import randint


class OTP:
    def __init__(self , sinput):
        f = open("otp-5.txt", "w+")  # creates a new file with the given file name
        for i in range(5000):  # prints the contents of the text file
            f.write(str(randint(0, 255)))  # creates a random number
            f.write(" ")

        f.close()  # closes the instance of the file
        self.sinput = sinput
        self.message = []
        self.e_message = []
        self.pad = []
        with open('otp-5.txt') as otp:
            readotp = csv.reader(otp, delimiter=" ")
            for row in readotp:
                for i in range(len(row)):
                    self.pad.append(row[i])

    def encrypt(self):
        """

           :param smessage:
           :return:
           """
        for letter in self.sinput:
            letter = ord(letter)
            self.message.append(letter)

        with open('otp-5.txt') as otp:
            readotp = csv.reader(otp, delimiter=" ")
            for row in readotp:
                for i in range(len(row)):
                    self.pad.append(row[i])

        for value in range(0, len(self.sinput)):
            self.e_message.append(self.message[value] ^ int(self.pad[value]))
        self.e_message = ''.join(chr(n) for n in self.e_message)
        self.message = ""
        self.sinput = ""

        return self.e_message

    def decrypt(self):
        dmessage = ''
        for i in range (len(self.e_message)):
            charval = chr(ord(self.e_message[i]) ^ int(self.pad[i]))
            dmessage += charval

        return dmessage



x = input("Enter your message: ")

message = OTP(x)

print(message.sinput)
print(message.encrypt())
print(message.decrypt())



