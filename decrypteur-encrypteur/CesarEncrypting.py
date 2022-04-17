import random
import os

# Config
EncryptingKey = int()
InitialWords = str()
wordCuted = []
Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
IndexLetter = 0
IndexWord = 0
# Starting Program
print ("\n                            CESAR ENCRYPTING TOOL")
InitialWords = input("\n Que doit on encrypter ? (only lower case character) ")
EncryptingKey = input("\n Quelle est la clé d'encryptage ? ")

# Encrypting

EncryptingWord = list(InitialWords)

for Encrypting in range(len(EncryptingWord)) :

    for Modifying in range (len(Alphabet)) :
        IndexLetter = 0
        IndexWord = 0
        if EncryptingWord[IndexWord] == Alphabet[IndexLetter] :
            MoovingInList = int(IndexLetter) + int(EncryptingKey)
            EncryptingWord[IndexWord] = Alphabet[MoovingInList]
            IndexLetter += 1
        else : 
            print("Je passe a la lettre d'apres")
            IndexLetter += 1
    
    IndexWord += 1

output = ''.join(EncryptingWord)
print(output)
        
    
        

