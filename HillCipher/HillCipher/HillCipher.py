def GetUserInput():
    plaintext = input("Enter plaintext to be encrypted: ")

    keyinput = int(input("Enter key to be encrypt with: "))

    matrixSize = int(input("Enter matrixSize for an n x n matrix: "))
    while keyinput < (matrixSize * matrixSize):
        print("Invalid Key/Matrix size.")
        keyinput = input("Enter key to be encrypt with: ")
        matrixSize = input("Enter matrixSize for an n x n matrix: ")
        break

GetUserInput()
