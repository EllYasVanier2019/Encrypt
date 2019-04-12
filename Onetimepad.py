import csv
from random import randint


class OTP:
    def __init__(self , sinput):
        """
        This is the One-Time pad initialize function. It reads and writes a text file with a malleable amount of
        integers. This pad that it creates and reads is known as the One-Time pad and is the essence of this encryption
        method.
        """
        f = open("otp-5.txt", "w+")  # creates a new file with the given file name
        for i in range(120000000):  # prints the contents of the text file
            f.write(str(randint(0, 255)))  # creates a random number
            f.write(" ")

        f.close()  # closes the instance of the file
        self.sinput = sinput  # creates an input variable to use within the methods
        self.message = []  # creates a message variable to use in the methods
        self.e_message = []  # creates the encrypted message variable to use within the methods
        self.pad = []

        with open('otp-5.txt') as otp:  # sets the file name to a easy to use name
            readotp = csv.reader(otp, delimiter=" ")  # reads the contents of the text and accounts for quotes or spaces
            for row in readotp:  # this loop will run for every number in the text file
                for i in range(len(row)):  # this loop will run for the number that the first loop is currently in
                    self.pad.append(row[i])  # this appends the value of the loop, to a new list called pad

    def encrypt(self):  # ENCRYPTION FUNCTION
        """
         This is the One-Time Pad encrypt function. What it does is it allows the user to encrypt a desired message
         by taking the ASCII values of that specific message and performing the XOR operator between the ASCII value
         and the value of a text file, also known as the One-Time pad itself. This function returns the characters of
         the result in a string format.
        """
        for letter in self.sinput:  # initializes a loop for the number of characters in the user input
            letter = ord(letter)  # rewrites each character to its ASCII value
            self.message.append(letter)  # appends each ASCII value to a new list called message

        for value in range(0, len(self.sinput)):  # runs the loop for the amount of numbers in the list input
            self.e_message.append(self.message[value] ^ int(self.pad[value]))  # XORS the message with the pad value
        self.e_message = ''.join(chr(n) for n in self.e_message)  # allows the new list to be written as a string
        self.message = ""  # removes traces of message list
        self.sinput = ""  # removes traces of input list

        return self.e_message  # returns the encrypted string

    def decrypt(self):  # DECRYPTION FUNCTION
        """
        This is the One-Time Pad decrypt function. It reverses the effects of the encrypt function by changing the
        values of the message back to its ASCII values, then running the XOR operation between it, and the text file
        also known as the One-Time pad. It then changes those characters back to their original character values. This
        function returns the characters in a user friendly string.
        """

        dmessage = ''  # initalizes a new variable
        for i in range (len(self.e_message)):  # runs a new loop for the number of characters in the encrypted message
            charval = chr(ord(self.e_message[i]) ^ int(self.pad[i]))  # XORS the encrypted message with the pad
            dmessage += charval  # above this line, the value was reset to characters, and variable equals that value

        return dmessage  # returns the contents of the string



x = input("Enter your message: ")

message = OTP(x)

print(message.sinput)
print(message.encrypt())
print(message.decrypt())



