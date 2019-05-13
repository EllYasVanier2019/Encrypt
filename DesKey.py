import Operators as op

def makeKeys(sinput):
    # ----------------------------LOOK UP TABLES-------------------------------- #
    PC_1 = [57, 49, 41, 33, 25, 17, 9, 1,  # Look up table for Permuted Choice 1
            58, 50, 42, 34, 26, 18, 10, 2,
            59, 51, 43, 35, 27, 19, 11, 3,
            60, 52, 44, 36, 63, 55, 47, 39,
            31, 23, 15, 7, 62, 54, 46, 38,
            30, 22, 14, 6, 61, 53, 45, 37,
            29, 21, 13, 5, 28, 20, 12, 4]

    PC_2 = [14, 17, 11, 24, 1, 5,  # Look up table for Permuted Choice 2
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]

    iteration = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]  # List for the changing iterations for rotating
    # ------------------------------------------------------------------------------- #
    message = op.stringtobin(sinput)

    while len(message) < 64:
        message = "0" + message

    keys = []
    temp = ""
    temp2 = ""
    lhalf = ""
    rhalf = ""

    for perm in range(56):
        temp += message[PC_1[perm]-1]

    lhalf = temp[0:28]
    rhalf = temp[28:56]

    for round in range(len(iteration)):
        lhalf = op.leftrotate(lhalf, iteration[round])
        rhalf = op.leftrotate(rhalf, iteration[round])

        temp = lhalf + rhalf

        for perm2 in range(48):
            temp2 += temp[PC_2[perm2]-1]

        keys.append(temp)
    return keys

print(makeKeys("12345678"))


