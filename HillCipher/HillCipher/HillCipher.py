# Hill Cipher
# Nataliya Chibizova, Ethan Morgan, Samuel Reynolds, Chandler Scott
# 10/27/2021
# <ENTER DESCRIPTION HERE>

# Converts a string to an integer based off of the index in the whitelist characters set.
# Returns a set of integers
def integerConversion(plaintext):
    whitelistCharacters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.\/;!@#$%^&*()-_=+| '

    numberedText = []

    for i,pLetter in enumerate(plaintext):
        for j, wLetter in enumerate(whitelistCharacters):
            if pLetter == wLetter:
              numberedText.append(j)

    return numberedText


# Driver -- the program assumes good input.  p, q, and e must all be prime
# numbers.
if __name__ == '__main__':
    # Step 1.  Get user input for plaintext, key, matrix size
   
    # Plaintext
    plaintext = input("Enter plaintext to be encrypted: ")
    numberedPlaintext = integerConversion(plaintext)
    
    # Debug for-loop -- can be removed
    for number in numberedPlaintext:
        print(number)
    
    # Key
    keyinput = input("Enter key to be encrypt with: ")
    numberedKey = integerConversion(keyinput)
    
    # Debug for-loop -- can be removed
    for number in numberedKey:
        print(number)
    
    # Matrix Size
    matrixSize = int(input("Enter matrixSize for an n x n matrix: "))
    
    # Check matrix size/key size compatibility
    while numberedKey < (matrixSize * matrixSize):
        print("Invalid Key/Matrix size.")
        
        keyinput = input("Enter key to be encrypt with: ")
        numberedKey = integerConversion(keyinput)
        
        matrixSize = input("Enter matrixSize for an n x n matrix: ")
        break

    # Step 2. Create encryption matrix with key input
    # Step 3. Encrypt plaintext with key matrix
    # Step 4. Invert key matrix
    # Step 5. Find inverse multiplicative of the determinant
    # Step 6. Multiply inverse matrix by step 5 and mod
    # Step 7. Invert key matrix
    
