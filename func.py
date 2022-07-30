# Course work by Ekaka Emmanuel 19/ITD/2926/PD
import random
def sendDistortedMessage(filename):
    # string to store the message during reading
    msg=""
    # reading data out of the file.
    with open(filename) as f:
        for line in f:
            msg+=line
        length = len(msg)
    # creating partion size
    normal = length//5
    remainder = length%5 
    if remainder>0:
        all=normal+1
    k = 5
    m = 0
    # Holding the data after spliting
    final =[]
    for i in range(normal):
        n=''
        n +=msg[m:k]
        n +=str(i)
        # final+=n
        final.append(n)
        print(n)
        # print(n) for testing
        # Executed when the last characters are less than 5 in number
        if i==(normal-1) and remainder:
            rem_n = i+1
            n=''
            n +=msg[k:length]
            extra = 5-len(n)
            n +=' '*extra
            n +=str(rem_n)
            # final+=n
            final.append(n)
            print(n)
            # print(n) for testing

        # increment
        k+=5
        m+=5
    random.shuffle(final)
    normalize =''
    for i in final:
        normalize+=i
    
    return normalize

# Function to re-arrage the data
def reArrageMessage(cipher):
    temp =[]
    read = ''
    stretch = len(cipher)
    partition = stretch//6
    m,k=0,6
    for i in range(partition):
        n=''
        n +=cipher[m:k]
        temp.append(n)
        m+=6
        k+=6
    indices = [ind for ind in range(stretch)]
    for va in range(partition):
        for inner in temp:
            no = int(inner[-1])
            
            if no==indices[va]:
                read +=inner[0:5]
                temp.remove(inner)
                break
    return read