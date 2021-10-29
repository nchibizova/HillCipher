# Hill Cipher
# Nataliya Chibizova, Ethan Morgan, Samuel Reynolds, Chandler Scott
# 10/27/2021
# Using Hill Cipher encrypt then decrypt the message
# Message: “Success is the ability to go from one failure to another with no loss of enthusiasm”
from egcd import egcd
import numpy as np
from sympy import Matrix
import random


whitelistCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.\/;?!@#$%&\'*()-_=+ '
modulus = 83

# integerConversion -- Establishes the character set and converts a string into an array of integers
def integerConversion(plaintext):
    

    numberedText = []

    for i,pLetter in enumerate(plaintext):
        for j, wLetter in enumerate(whitelistCharacters):
            if pLetter == wLetter:
              numberedText.append(j)

    return numberedText

# stringConversion -- Establishes the character set and converts arrays of integers into a string
def stringConversion(textBlocks):
    output = ""
    for array in textBlocks:
        for x in range(0, len(array)):
            output = output + whitelistCharacters[int(array[x])]

    return output


# CreateKeyMatrix -- Takes the key input string and converts it into a key matrix
def CreateKeyMatrix(keyInput, matrixSize):
    keyMatrix = np.zeros(matrixSize*matrixSize)
    index = 0
    for char in keyInput:
        keyMatrix[index] = keyInput[index]
        index = index + 1
    keyMatrix = keyMatrix.reshape(matrixSize, matrixSize)
    return keyMatrix


# PadPlaintext -- Pads the plaintext at the end with an arbitrary value 
# to be evenly divided by the matrix size
def PadPlaintext(plaintext, matrixSize):
    remainder = len(plaintext) % matrixSize
    if remainder > 0:
        remainder = matrixSize - remainder
        for i in range(remainder):
            plaintext += '/'
            remainder = remainder - 1
    return plaintext

# PadKey -- Pads the key at the end with an arbitrary value 
def padKey(key, matrixSize):
    mSize = matrixSize * matrixSize
    if len(key) > mSize:
        key = key[0: (mSize)]
    else:
        remainder = len(key) % mSize
        if remainder > 0:
            remainder = mSize - remainder
            for i in range(remainder):
                var = whitelistCharacters[random.randint(0, modulus - 1)]
                key += var
                remainder = remainder - 1
    return key

# SplitTextToBlocks -- Separates the plaintext into n-size blocks for encryption
def SplitTextToBlocks(numberedText, matrixSize):
    textMatrix = []
    offset = 0
    for i in range(0, int(len(numberedText) / matrixSize)):
        array = []
        for x in range(0, matrixSize):
            array.append(numberedText[offset])
            offset = offset + 1
        textMatrix.append(array)
            
    textMatrix = np.asarray(textMatrix)
    return textMatrix

# ENCRYPT -- encypts by multiplying the block matrix with the key matrix and 
# modulo by the number of characters in the set
def Encrypt(blockText, keyMatrix, matrixSize):
    cipherMatrix = []
    for matrix in blockText:
        cipherValue = (matrix@keyMatrix) % modulus
        cipherMatrix.append(cipherValue)
    return cipherMatrix

# DECRYPT -- decypts by multiplying the block matrix with the inverse key matrix and 
# modulo by the number of characters in the set
def Decrypt(blockText, keyMatrix, matrixSize):
    plaintextMatrix = []
    for matrix in blockText:
        plainTextValue = np.matmul(matrix, keyMatrix)
        plainTextValue = np.remainder(plainTextValue, 83).flatten()
        plaintextMatrix.append(plainTextValue)
    return plaintextMatrix

# findInverseKey -- finds the inverse of the key matrix for decryption
def FindInverseKey(keyMatrix, det):
    det_inv = egcd(det, modulus)[1] % modulus;
    matrix_modulus_inv = det_inv * np.round(det * np.linalg.inv(keyMatrix)) % modulus

    return matrix_modulus_inv

# ErasePadding -- Removes the padding from the string 
def ErasePadding(decryptedText):
    done = False
    while(done == False):
        if(decryptedText[len(decryptedText)-1] == '/'):
            decryptedText = decryptedText.rstrip(decryptedText[-1])
        else:
            done = True
    return decryptedText




# Driver -- the program assumes good input.  p, q, and e must all be prime
# numbers.
if __name__ == '__main__':
 
    goAgain = "Y"
    
while goAgain == "Y":
        # Step 1.  Get user input for plaintext, key, matrix size
   
        # Plaintext
        plaintext = input("Enter plaintext to be encrypted: ")
        # Matrix Size
        while True:
            matrixSize = input("\nEnter size for an n x n matrix: ")
            try:
                matrixSize = int(matrixSize)
                break
            except ValueError:
                print("Invalid input! Please try again." )
        
    
        # Key
        keyinput = input("\nEnter key to encrypt with: ")
        keyinput = padKey(keyinput, matrixSize)
        numberedKey = integerConversion(keyinput)
        
        # Plaintext Padding
        paddedPlaintext = PadPlaintext(plaintext, matrixSize)
        numberedPlaintext = integerConversion(paddedPlaintext)
    
        keyMatrix = CreateKeyMatrix(numberedKey, matrixSize)
        det = int(np.round(np.linalg.det(keyMatrix)))
    
        while det == 0:
            print("Invalid Key/Matrix input. Determinant of the key matrix is equal to 0.")
            
            # Key
            keyinput = input("\nEnter key to encrypt with: ")
            keyinput = padKey(keyinput, matrixSize)
            numberedKey = integerConversion(keyinput)
            
            # Step 2. Create encryption matrix with key input
            keyMatrix = CreateKeyMatrix(numberedKey, matrixSize)
            # calculate determinant of the key matrix
            det = int(np.round(np.linalg.det(keyMatrix)))
            break
    
        # Step 3. Create n size blocks of the plaintext
        blockText = SplitTextToBlocks(numberedPlaintext, matrixSize)
        # Step 4. Encrypt plaintext with key matrix
        cipherText = Encrypt(blockText, keyMatrix, matrixSize)
        # Step 5. Print key & ciphertext
        print("\nKey:")
        print(keyinput)
        print("\nCiphertext:")
        print(stringConversion(cipherText))
        # Step 6. Invert key matrix
        inverseKey = FindInverseKey(keyMatrix, det)
        # Step 7. Decrpyt ciphertext with inverse key matrix
        decipheredText = Decrypt(cipherText, inverseKey, matrixSize)
        # Step 8. Print deciphered plaintext
        print("\nPlaintext:")
        print(ErasePadding(stringConversion(decipheredText)))
        # Step 8. Ask user another input
        goAgain = input("\nWould you like to encrypt/decrypt another message?(Y/N): ")
        print("\n*********************************************\n")

    
