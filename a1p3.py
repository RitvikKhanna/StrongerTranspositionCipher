"""

Before reading this file or using it please read the readme_Ritvik.pdf included in the zip file. The logic and other things have slightly been changed according to the assignment.
Everything about the resources used to make this file are in the above said file. Do not proceed without reading that.

"""


# I have included the encryptMessage and the decryptMessage functions I wrote as a1p1.py and a1p2.py in this for faster run time.

# Included modules
import random,sys,math

## *************************** START OF THE PROGRAM ****************************** #

def main():
    
    random.seed(32)

    for i in range(20):                                                     # 20 Test Cases
        
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'* random.randint(4,40)        # Random length message

        message = list(message)                                             

        random.shuffle(message)                                             # Shuffled message

        message = ''.join(message)

        print("Test #%s: '%s...'" %(i+1,message[:50]))


        for keylen in range(1,len(message)):                                # key lengths from 1 until length of the message
            
            for i in range(10):                                             # 10 keys for each keylength
                
                key = list(range(1,keylen+1))                               # For key lengths between 1 and keylen + 1 as for range(1,keylen) there will be empty lists since range(1,1) = []
                
                random.shuffle(key)                                         
             
                encrypted = encryptMessage(key,message)                     # Encryption 
                
                decrypted = decryptMessage(key,encrypted)                   # Decryption
                
                if message != decrypted:                                    # Check condition if the encrypted text is the same as decrypted or not

                    print("Mismatch with key %s and message|%s|"%(key,message))
                    
                    print("The decrypted text is:|%s|"%(decrypted))

                    sys.exit()                                              # Exit system

    print("Transposition cipher test passed.")                              # If all tests are passed



# ******** ENCRYPTION FUNCTION ******** # 
   
def encryptMessage(key,message):

    if (len(message)%len(key))!=0:                                          # Add spaces in the end of the text to avoid shading

        for i in range(len(key)-(len(message)%len(key))):                  

            message += ' '
    
    ciphertext = ['']*len(key)

    num = 0

#**** For the function below I made some changes. Instead of saving it in a sequential order it saves the encrypted text in the order of the column numbers passed as parameter ****#    

    for col in range(len(key)):         

            pointer = key[num]

            counter = pointer - 1

            num += 1

            while counter<len(message):

                ciphertext[col] += message[counter]

                counter += len(key)

    return ''.join(ciphertext)


# ******** DECRYPTION FUNCTION ******** #

def decryptMessage(key,message):
    
    
# **** The main idea behind this function is to change the encrypted text from the order of the key to sequential order and then use the function given in the source code **** #


#  Example : They key was [2,3,4,1,5] which is in message1 then the function will convert the encrypted text in the order [1,2,3,4,5] which is saved as message2
#  and then message2 is converted to plaintext. 

    
    colnum = math.ceil(len(message)/len(key))

    rownum = len(key)

    plaintext = [''] * colnum

    message1 = [''] * rownum

    message2 = [''] * rownum


    
         
    message1 = [message[i:i+colnum] for i in range(0,len(message), colnum)]     # message1 is conversion of the text in the list form
    
  
    
    i = 0

# **** Below is the conversion to the order [1,2,3,4,5,.......,....]

    for row in range(rownum):

        col = key[i]-1

        message2[col] = message1[row]

        i += 1
    
    message2 = ''.join(message2)
    

    plaintext = [''] * colnum

    col = 0

    row = 0

# **** The following is taken from the source code only **** #

    for symbol in message2:
        plaintext[col] += symbol
        col += 1 
        if (col == colnum):
            col = 0
            row += 1
    plaintext = ''.join(plaintext)    # Convert the list to a string
    plaintext = plaintext.strip()     # Strip all the spaces in the end of the plaintext if any
    return plaintext
         

if __name__=='__main__':
    main()
