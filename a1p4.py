
"""

Before reading this file or using it please read the readme_Ritvik.pdf included in the zip file. The logic and other things have slightly been changed according to the assignment.
Everything about the resources used to make this file are in the above said file. Do not proceed without reading that.

"""

# All important comments are already in a1p3 and the logic used in the readme file.

import time, os, sys, math

def main():
    inputFilename = 'mystery.txt'
    outputFilename = 'mystery.dec.txt'
    
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('Decrypting...' )

    
    startTime = time.time()
    
    
    translated = decryptMessage([2,4,6,8,10,1,3,5,7,9], content)
    totalTime = round(time.time() - startTime, 2)
    print('Decyption time: %s seconds' % (totalTime))

    
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done decrypting %s (%s characters).' % (inputFilename, len(content)))
    print('Decrypted file is %s.' % (outputFilename))


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



# If transpositionCipherFile.py is run (instead of imported as a module)
# call the main() function.
if __name__ == '__main__':
    main()
