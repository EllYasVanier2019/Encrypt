import Operators as op
import struct
import os


class TripleDES:
    # Initialize all lookup tables used for encryption and decryption
    ColumnNumberTables =      [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
                                0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
                                4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
                                15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

                               [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
                                3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
                                0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
                                13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

                               [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
                                13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
                                13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
                                1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

                               [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
                                13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
                                10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
                                3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

                               [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
                                14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
                                4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
                                11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

                               [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
                                10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
                                9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
                                4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

                               [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
                                13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
                                1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
                                6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

                               [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
                                1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
                                7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
                                2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

    # a lookup table for initial permutation
    InitialPerm = [58, 50, 42, 34, 26, 18, 10, 2,
                   60, 52, 44, 36, 28, 20, 12, 4,
                   62, 54, 46, 38, 30, 22, 14, 6,
                   64, 56, 48, 40, 32, 24, 16, 8,
                   57, 49, 41, 33, 25, 17, 9, 1,
                   59, 51, 43, 35, 27, 19, 11, 3,
                   61, 53, 45, 37, 29, 21, 13, 5,
                   63, 55, 47, 39, 31, 23, 15, 7]

    # a lookup table for expansion bit
    Expansionbit = [32, 1, 2, 3, 4, 5,
                    4, 5, 6, 7, 8, 9,
                    8, 9, 10, 11, 12, 13,
                    12, 13, 14, 15, 16, 17,
                    16, 17, 18, 19, 20, 21,
                    20, 21, 22, 23, 24, 25,
                    24, 25, 26, 27, 28, 29,
                    28, 29, 30, 31, 32, 1]

    # a lookup table for second permutation
    SecondPerm = [16, 7, 20, 21,
                  29, 12, 28, 17,
                  1, 15, 23, 26,
                  5, 18, 31, 10,
                  2, 8, 24, 14,
                  32, 27, 3, 9,
                  19, 13, 30, 6,
                  22, 11, 4, 25]

    # a lookup table for the final permutation
    Finalperm = [40, 8, 48, 16, 56, 24, 64, 32,
                 39, 7, 47, 15, 55, 23, 63, 31,
                 38, 6, 46, 14, 54, 22, 62, 30,
                 37, 5, 45, 13, 53, 21, 61, 29,
                 36, 4, 44, 12, 52, 20, 60, 28,
                 35, 3, 43, 11, 51, 19, 59, 27,
                 34, 2, 42, 10, 50, 18, 58, 26,
                 33, 1, 41, 9, 49, 17, 57, 25]

    # Look up table for Permuted Choice 1
    PC_1 = [57, 49, 41, 33, 25, 17, 9, 1,
            58, 50, 42, 34, 26, 18, 10, 2,
            59, 51, 43, 35, 27, 19, 11, 3,
            60, 52, 44, 36, 63, 55, 47, 39,
            31, 23, 15, 7, 62, 54, 46, 38,
            30, 22, 14, 6, 61, 53, 45, 37,
            29, 21, 13, 5, 28, 20, 12, 4]

    # Look up table for Permuted Choice 2
    PC_2 = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]

    # List for the changing iterations for rotating
    iteration = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    def __init__(self, plainkey):
        self.key = self.keyCreator(plainkey)

    def Perm(self, listinput, inputmessage):

        """
        :param listinput: is the table you want to permute the input message according to
        :param inputmessage: is the message that you want to permute
        :return: returns the permuted message
        """

        # initalizes a variable called finalmessage
        finalmessage = ""
        listlength = len(listinput)

        for index in range(listlength):
            finalmessage += inputmessage[listinput[index] - 1]

        return finalmessage

    def Sbox(self, inputmessage):

        """
        :param inputmessage: the message that you want to permute
        :return: returns the permuted message
        """

        # the tables that are used to get the output message for every iteration

        finalmessage = ""

        for boxnum in range(8):  # Substitution Box

            # takes 6 bits at a time from the message
            sixbits = inputmessage[boxnum * 6: (boxnum + 1) * 6]

            # the row is the first but and the last bit of the sixbits
            row = sixbits[0] + sixbits[5]

            # the column is the middle 4
            columns = sixbits[1] + sixbits[2] + sixbits[3] + sixbits[4]

            # converts the row and column to an integer
            row = op.bintoint(row)
            columns = op.bintoint(columns)

            # finds a value using the current s-box to
            columnrowindex = (row * 16) + columns

            # makes temp equal the the corresponding number on the table
            temp = op.inttobin(TripleDES.ColumnNumberTables[boxnum][columnrowindex])[4:]

            # adds the temp message to finalmesssage
            finalmessage += temp
        return finalmessage

    def DESencrypt(self, input, Keys, round):
        """

        :param input: plain text message
        :param Keys: which keys you are using
        :param round: which round you need to use.
        :return:
        """
        final = ''

        input = op.stringtobin(input)

        # pads the message with zeros after it to make it a multiple of 64
        while len(input) % 64 != 0:
            input += "0"

        # finds out how many blocks of 64 there are
        blocks = len(input) // 64

        # runs for every block
        for index in range(blocks):

            # gets the 64 bit chunk from the message
            message = input[index * 64: (index + 1) * 64]

            # does the initial permutation
            message = self.Perm(TripleDES.InitialPerm, message)

            # splits the message into left and right
            MessageLeft = message[0:32]
            MessageRight = message[32:64]

            # runs for each key
            for subkey in range(16):
                righttemp = ''

                # lefttemp becomes message right we do this because messageLeft has to equal
                # message right, but we use MessageRight in another step so lefttemp is necessary
                lefttemp = MessageRight

                # expands righttemp
                righttemp = self.Perm(TripleDES.Expansionbit, MessageRight)

                righttemp = op.bitxor(Keys[round][subkey], righttemp)  # xors the subkey and right temp

                while len(righttemp) < 48:
                    righttemp = "0" + righttemp  # pads the right temp until it reaches the desired length

                righttemp = self.Sbox(righttemp)  # runs sbox function on righttemp

                righttemp = self.Perm(TripleDES.SecondPerm, righttemp)  # runs perm function on right temp

                MessageRight = op.bitxor(MessageLeft, righttemp)  # xors messageleft with message right

                while len(MessageRight) < 32:
                    MessageRight = "0" + MessageRight  # pads the message until it reaches 32 bits

                MessageLeft = lefttemp

            temp = ''

            message = (MessageRight + MessageLeft)  # combines the two halves of the message

            for g in range(64):
                temp += message[TripleDES.Finalperm[g] - 1]  # final permutation

            final += temp

        return op.bintostring(final)  # returns string of encrypted message.

    def DESdecrypt(self, input, Keys, round):
        """

        :param input: encrypted message
        :param Keys: which keys to use
        :param round: which round you need to use
        :return:
        """

        final = ''

        input = op.stringtobin(input)

        # pads the message with zeros after it to make it a multiple of 64
        while len(input) % 64 != 0:
            input += "0"

        # finds out how many blocks of 64 there are
        blocks = len(input) // 64

        # runs for every block
        for index in range(blocks):

            # gets the 64 bit chunk from the message
            message = input[index * 64: (index + 1) * 64]

            # does the initial permutation
            message = self.Perm(TripleDES.InitialPerm, message)

            # splits the message into left and right
            MessageLeft = message[0:32]
            MessageRight = message[32:64]

            # runs for each key
            for subkey in range(16):
                righttemp = ''

                # lefttemp becomes message right we do this because messageLeft has to equal
                # message right, but we use MessageRight in another step so lefttemp is necessary
                lefttemp = MessageRight

                # expands righttemp
                righttemp = self.Perm(TripleDES.Expansionbit, MessageRight)

                righttemp = op.bitxor(Keys[round][15 - subkey],
                                      righttemp)  # XOR the keys in inverse order with right temp

                while len(
                        righttemp) < 48:  # while xor-ing the subkey and righttemp, the length of the final message may be lower than 48 due to no padding from the function
                    righttemp = "0" + righttemp

                righttemp = self.Sbox(righttemp)  # runs the sbox function on right temp

                righttemp = self.Perm(TripleDES.SecondPerm, righttemp)  # run perm fucntion on right temp

                MessageRight = op.bitxor(MessageLeft, righttemp)  # xor the message left and right temp

                while len(MessageRight) < 32:
                    MessageRight = "0" + MessageRight  # the xor may need to be padded, as the function itself does not include it.

                MessageLeft = lefttemp  # message left is given the value of lefttemp

            temp = ''

            message = (MessageRight + MessageLeft)  # combines the two messages

            for g in range(64):
                temp += message[TripleDES.Finalperm[g] - 1]  # does the final permutaion

            final += temp

        return op.bintostring(final)  # function returns the string of the final decrypted message

    def E3DES(self, message, messagetype, outputtype="hex"):
        """

        :param message: inital message or file to be encrypted
        :param messagetype: type of the message 'file' or 'string'.
        :param outputtype: Output type is one of the following:  'string' 'hex(default)' 'bytes'
        :return:
        """
        stringmessage = ""
        if messagetype == "string":  # formats message to a string
            stringmessage = message

        elif messagetype == "file":
            bytesmessage = op.getbytearray(message)
            for i in range(len(bytesmessage)):     # formats message as a file
                stringmessage += op.bintostring(bytesmessage[i])

        else:
            print("Message type invalid. Deafulted to string")
            stringmessage = message  # defaults message to a string

        encryptedmessage = self.DESencrypt(self.DESdecrypt(self.DESencrypt(stringmessage, self.key, 0), self.key, 1), self.key, 2)

        if outputtype == "string":  # formats output to hex
            pass

        elif outputtype == "hex":
            encryptedmessage = op.bintohex(op.stringtobin(encryptedmessage))  # formats output to hex
            return encryptedmessage

        elif outputtype == "bytes":
            temp = []
            for i in range(len(encryptedmessage)):
                temp.append(op.stringtobin(encryptedmessage[i]))  # formats message to binary

            encryptedmessage = temp

        return encryptedmessage


    def D3DES(self, message, messagetype, outputtype = "hex"):
        """

        :param message: encrypted message
        :param messagetype: it can be 'string' , 'hex', 'bytes', or 'file'
        :param outputtype: it can be 'string', 'bytes'
        :return:
        """
        if messagetype == "string":
            encryptedmessage = message  # formats message to string

        elif messagetype == "hex":
            encryptedmessage = op.bintostring(op.hextobin(message))

        elif messagetype == "bytes":
            encryptedmessage = ""       # formats message to binary
            for i in range(len(message)):
                encryptedmessage += op.bintostring(message[i])

        elif messagetype == "file":
            bytesmessage = op.getbytearray(message)
            encryptedmessage = ""           # formats message to file
            for i in range(len(bytesmessage)):
                encryptedmessage += op.bintostring(bytesmessage[i])

        else:
            print("Message Type Invalid. Defaulted to string")
            encryptedmessage = message

        decryptedmessage = self.DESdecrypt(self.DESencrypt(self.DESdecrypt(encryptedmessage, self.key, 2), self.key, 1), self.key, 0)

        if outputtype == "string":
            pass

        elif outputtype == "bytes":
            temp = []
            for i in range(len(decryptedmessage)):
                temp.append(op.stringtobin(decryptedmessage[i]))

            decryptedmessage = temp

        else:
            print("Output Type Invalid. Defaulted to string")

        return decryptedmessage

    @staticmethod
    def keyCreator(plainkey):
        """

        :param plainkey: requires a plain-text key of max 24 characters
        :return:
        """
        plainkey = op.stringtobin(plainkey)  # changes the key to bits

        while len(plainkey) < 192:  # Pads the bits with zeros
            plainkey += "0"

        Keys = [[], [], []]  # Initalizes the final list of the three keys

        for n in range(3):  # seperates the 192 bits into three chunks

            key = plainkey[n * 64: (n + 1) * 64]

            temp = ""
            newkey = ""
            lkey = ""
            rkey = ""
            Key = []

            for i in range(56):  # Permutes the block with Permuted choice 1
                temp += (key[TripleDES.PC_1[i] - 1])

            for value in range(28):  # splits the block into two halves
                lkey += (temp[value])

            for value in range(28, 56):
                rkey += (temp[value])

            for i in range(16):
                lkey = op.leftrotate(lkey, TripleDES.iteration[i])  # rotates left block by the given iteration
                rkey = op.leftrotate(rkey, TripleDES.iteration[i])  # rotates right block by the given iteration

                newkey = lkey + rkey  # puts the blocks back together

                temp = ""
                for i in range(48):  # permutes the block again with Permuted choice 2
                    temp += (newkey[TripleDES.PC_2[i] - 1])

                Key.append(temp)  # appends these values to a list

            Keys[n] = Key  # appends the list to a final list.

        return Keys  # returns the final list of the three keys and their subkeys.


file = "encrypted.dat"
plainkey = "DrPepper"

test = TripleDES(plainkey)
image_bytes = test.D3DES(file, "file", "bytes")
test.write_to_desktop(image_bytes, ".dat", ".jpeg")



