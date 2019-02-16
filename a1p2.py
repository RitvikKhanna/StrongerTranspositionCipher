"""

Before reading this file or using it please read the readme_Ritvik.pdf included in the zip file. The logic and other things have slightly been changed according to the assignment.
Everything about the resources used to make this file are in the above said file. Do not proceed without reading that.

"""

# All important comments are already in a1p3 and the logic used in the readme file.

import math

def main():

    myMessage = input("Enter message : ")

    print("\nEnter keys with spaces (Example: 1 2 3 4 5): ")

    myKey = [int(num) for num in input().split()]

    
    plaintext = decryptMessage(myKey,myMessage)

  
    print("\nPlaintext is :\n"+plaintext + '|')



def decryptMessage(key,message):

    colnum = math.ceil(len(message)/len(key))

    rownum = len(key)

    plaintext = [''] * colnum
    message1 = [''] * rownum
    message2 = [''] * rownum

    
    message1 = [message[i:i+colnum] for i in range(0,len(message), colnum)]
    
  
    
    i = 0
    for row in range(rownum):

        col = key[i]-1

        message2[col] = message1[row]

        i += 1
    
    message2 = ''.join(message2)
    

    plaintext = [''] * colnum

    col = 0
    row = 0

    for symbol in message2:
        plaintext[col] += symbol
        col += 1 
        if (col == colnum):
            col = 0
            row += 1
    plaintext = ''.join(plaintext)
    plaintext = plaintext.strip()
    return plaintext

  

if __name__ == '__main__':
    main()

