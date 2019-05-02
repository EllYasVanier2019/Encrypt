import operators as op
def keyCreator(ogkey):
    PC_1 = [57, 49, 41, 33, 25, 17, 9, 1,   #Look up table for Permuted Choice 1
	        58, 50, 42, 34, 26, 18, 10, 2,
	        59, 51, 43, 35, 27, 19, 11, 3,
	        60, 52, 44, 36, 63, 55, 47, 39,
	        31, 23, 15, 7, 62, 54, 46, 38,
	        30, 22, 14, 6, 61, 53, 45, 37,
	        29, 21, 13, 5, 28, 20, 12, 4]

    PC_2 = [14, 17, 11, 24, 1, 5,           #Look up table for Permuted Choice 2
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]

    iteration = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]  #List for the changing iterations for rotating


    ogkey = op.stringtobin(ogkey)   #changes the key to bits

    while len(ogkey) < 193:   #Pads the bits with zeros
        ogkey += "0"

    Keys = [[], [], []]  #Initalizes the final list of the three keys

    for n in range(3):   #seperates the 192 bits into three chunks

        key = ogkey[n * 64: (n + 1) * 64]

        temp = ""
        newkey = ""
        lkey = ""
        rkey = ""
        Key = []



        for i in range (56):  #Permutes the block with Permuted choice 1
            temp += (key[PC_1[i]-1])

        for value in range (28):   #splits the block into two halves
            lkey += (temp[value])

        for value in range (28,56):
            rkey += (temp[value])

        for i in range (16):
            lkey = op.leftrotate(lkey, iteration[i]) #rotates left block by the given iteration
            rkey = op.leftrotate(rkey, iteration[i]) #rotates right block by the given iteration

            newkey = lkey + rkey #puts the blocks back together

            temp = ""
            for i in range (48): #permutes the block again with Permuted choice 2
                temp += (newkey[PC_2[i]-1])

            Key.append(temp) #appends these values to a list

        Keys[n] = Key #appends the list to a final list.


    return Keys #returns the final list of the three keys and their subkeys.





key = "asdfafasdf"
print(keyCreator(key))
