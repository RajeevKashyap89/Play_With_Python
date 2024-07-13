alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_count):
    cipher_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_count
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_count):
    plain_text = ''
    for letter in cipher_text:
        position = alphabet.index(letter)
        original_position = position - shift_count
        plain_text += alphabet[original_position]
    print(f"The decoded text is {plain_text}")      
    

    if direction == "encode":
    
        encrypt(plain_text = text , shift_count = shift)
        
    else:

        decrypt(cipher_text = text, shift_count = shift)

    



  