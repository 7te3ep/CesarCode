import random
import os

# Config
MoovingInList = 0
EncryptingKey = int()
InitialWords = str()
wordCuted = []
Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
IndexLetter = 0
IndexWord = 0

# choix de l'action 
print ("\n                            CESAR CRYPTOLOGY TOOL")
descision = input("\n Veut tu encrypter (1) ou decrypter quelque chose (2) ? 1/2  ")

# ENCRYPTAGE

if descision == str(1) :

    # Starting Program
    print ("\n                            CESAR ENCRYPTING TOOL")
    InitialWords = input("\n Que doit on encrypter ? (only lower case character) ")
    EncryptingKey = int(input("\n Quelle est la clé d'encryptage ? "))

    # Encrypting

    EncryptingWord = list(InitialWords)

    for Encrypting in range(len(EncryptingWord)) :

        for Modifying in range (len(Alphabet)) :
            if EncryptingWord[IndexWord] == Alphabet[IndexLetter] :
                MoovingInList = int(IndexLetter) + int(EncryptingKey)
                EncryptingWord[IndexWord] = Alphabet[MoovingInList]
                MoovingInList = 0
                break
            else : 
                IndexLetter += 1
        IndexLetter = 0
        IndexWord +=1
        

    output = ''.join(EncryptingWord)
    print("\nResultat : ",output)

else :

    # Config
    MoovingInList = 0
    EncryptingKey = int()
    InitialWords = str()
    wordCuted = []
    Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    IndexLetter = 0
    IndexWord = 0
    # Starting Program
    print ("\n                            CESAR DECRYPTING TOOL")
    InitialWords = input("\n Que doit on decrypter ? (only lower case character) ")
    EncryptingKey = int(input("\n Quelle est la clé d'encryptage ? "))

    # Encrypting

    EncryptingWord = list(InitialWords)

    for Encrypting in range(len(EncryptingWord)) :

        for Modifying in range (len(Alphabet)) :
            if EncryptingWord[IndexWord] == Alphabet[IndexLetter] :
                MoovingInList = int(IndexLetter) - int(EncryptingKey)
                EncryptingWord[IndexWord] = Alphabet[MoovingInList]
                MoovingInList = 0
                break
            else : 
                IndexLetter += 1
        IndexLetter = 0
        IndexWord +=1


    output = ''.join(EncryptingWord)
    print("\nResultat : ",output)