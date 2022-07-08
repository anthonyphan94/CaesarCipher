alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
stop = int((len(alphabet)-1)/2)


endOfGame = False
# -1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    cipher_text = []
    for letter in text:
        for i in range(int(len(alphabet) / 2)):
            if letter == alphabet[i]:
                # print(i, letter)   
                newletter = alphabet[i+shift]
                cipher_text += newletter
    cipher_text = "".join(cipher_text)        
    return cipher_text 



def decrypt(text, shift):
    decrypt_text = []
    for letter in text:
        for i in range(len(alphabet)-1, stop, -1):
            if letter == alphabet[i]:
                newLetter = alphabet[i - shift]
                decrypt_text += newLetter
    decrypt_text="".join(decrypt_text)
    return decrypt_text
                

while not endOfGame:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    if direction == 'encrypt':
        print(encrypt(text,shift))
        print("start again?, 'y' or 'n' ")
        start = input()
        if start == 'y':
            endOfGame = False
        if start == 'n':
            endOfGame = True
        
    elif direction == 'decrypt':
        print(decrypt(text, shift))
        print("start again?, 'y' or 'n' ")
        start = input()
        if start == 'y':
            endOfGame = False
        if start == 'n':
            endOfGame = True

