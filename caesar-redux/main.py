def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ord(char) - ord("A" if is_upper else "a")
            char_code = (char_code + shift) % 26
            encrypted_char = chr(char_code + ord("A" if is_upper else "a"))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)


def caesar_cipher(shift, text):
    if "the" in text.strip().split():
        print(caesar_encrypt(text, shift))
    else:
        print(caesar_decrypt(text, shift))


n = int(input())

for i in range(n):
    shift = int(input())
    text = input()
    caesar_cipher(shift, text)
