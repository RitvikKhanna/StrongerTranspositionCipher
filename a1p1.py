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

    ciphertext = encryptMessage(myKey,myMessage)

    print("\nThe cipher text is :\n"+ciphertext + '|')

    
def encryptMessage(key,message):

    if (len(message)%len(key))!=0:

        
        
        for i in range(len(key)-(len(message)%len(key))):
            message += ' '

    
    ciphertext = ['']*len(key)

    num = 0
    
    for col in range(len(key)):

            pointer = key[num]

            counter = pointer - 1

            num += 1

            while counter<len(message):

                ciphertext[col] += message[counter]

                counter += len(key)

           

    return ''.join(ciphertext)

if __name__ == '__main__':
            main()


                               
