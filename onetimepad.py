import csv
import random
import socket
import threading

socketHolder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class MyOTP:
    def __init__(self, key=None, keytype=None):
        self.pad = []

        if key is None:
            if keytype == "file":  # formats the key type to file type
                newfilename = "pad.txt"  # sets file name

                f = open(newfilename, "w+")  # creates a new file with the given file name
                for i in range(120000000):  # prints the contents of the text file
                    f.write(str(random.randint(0, 255)))  # creates a random number
                    f.write(" ")

                f.close()  # closes the instance of the file

                with open(newfilename) as otp:  # sets the file name to a easy to use name
                    readotp = csv.reader(otp, delimiter=" ")  # reads the contents of the text and accounts for quotes or spaces
                    for row in readotp:  # this loop will run for every number in the text file
                        for i in range(len(row)):  # this loop will run for the number that the first loop is currently in
                            self.pad.append(int(row[i]))  # this appends the value of the loop, to a new list called pad

            elif keytype == "string":
                for i in range(16):  # case for string type
                    self.pad.append(random.randint(0, 255))

            elif keytype is None:
                print("Key type defaulted to string")  # case for default
                for i in range(16):
                    self.pad.append(random.randint(0, 255))

            else:
                print("Key Type Invalid. Defaulted to generating a string key")  # case for default
                for i in range(16):
                    self.pad.append(random.randint(0, 255))

        else:
            if keytype is None:  # type defaulted to string
                print("Key Type defaulted to string.")
                for letter in key:
                    self.pad.append(ord(letter))

            elif keytype == "string":  # case for type string
                for letter in key:
                    self.pad.append(ord(letter))

            elif keytype == "file":
                with open(key) as otp:  # sets the file name to a easy to use name
                    readotp = csv.reader(otp, delimiter=" ")  # reads the contents of the text and accounts for quotes or spaces
                    for row in readotp:  # this loop will run for every number in the text file
                        for i in range(len(row)):  # this loop will run for the number that the first loop is currently in
                            self.pad.append(int(row[i]))  # this appends the value of the loop, to a new list called pad

            else:
                print("Key Type is invalid. Defaulted to string.")  # case for default
                for letter in key:
                    self.pad.append(ord(letter))

    def encrypt(self, plaintext):
        """

        :param plaintext: requires a plaintext from the user
        :return:
        """
        encryptedmessage = ''

        if len(self.pad) < len(plaintext):  # this pads the pad with zeros, in order to be able to XOR with the plaintext
            while len(self.pad) < len(plaintext):
                self.pad.append(0)

        for icounter in range(len(plaintext)):  # XORS all the values in the plaintext with the pad
            encryptedmessage += chr(ord(plaintext[icounter]) ^ self.pad[icounter])

        return encryptedmessage  # returns the character of the XOR-ed value.

    def decrypt(self, ciphertext):
        """

        :param ciphertext: This parameter requires ciphered text encrypted by the encrypt function
        :return:
        """
        return self.encrypt(ciphertext)

    def communicate(self, sender=False, IP='0.0.0.0'):
        """
        This is the method to call when the user wants to communicate between 2 computers
        :param sender: If this computer sends first, set this value to True
        :param IP: If sender is True, then the IP of the receiving computer must be inserted here
        """
        global socketHolder
        if sender:
            socketHolder.connect((IP, 54321))
            print("connected")
        else:
            socketHolder.bind(('0.0.0.0', 54321))
            socketHolder.listen()
            connection, address = socketHolder.accept()
            socketHolder = connection

        a = threading.Thread(target=self.sends)
        b = threading.Thread(target=self.recv)
        a.start()
        b.start()

    def sends(self):
        global socketHolder  # call variable as global
        while True:
            msg = input("")  # placeholder for a way fof getting input
            msg = self.encrypt(msg)
            socketHolder.send(msg.encode(encoding='utf-8', errors='ignore'))  # sends input(add your encryption here)

    def recv(self):
        global socketHolder  # call variable as global
        while True:
            data = socketHolder.recv(4096).decode(encoding='utf-8', errors='strict')  # recieves data from connection
            print(self.decrypt(data))


test = MyOTP("abc", "string")

