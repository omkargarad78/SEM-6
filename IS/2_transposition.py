def encrypt_transposition(text, key):
    order_dict = {key[i]: i + 1 for i in range(len(key))}
    num_rows = (len(text) + len(key) - 1) // len(key)
    table = [[' ' for i in range(len(key))] for i in range(num_rows)]
    index = 0

    for row in range(num_rows):
        for col in range(len(key)):
            if index < len(text):
                table[row][col] = text[index]
                index += 1

    encrypted_text = ""
    for col, col_index in order_dict.items():
        for row in range(num_rows):
            encrypted_text += table[row][col_index - 1] if row < len(table) else '*'
    return encrypted_text

def decrypt_transposition(encrypted_text, key):
    order_dict = {key[i]: i + 1 for i in range(len(key))}
    num_rows = len(encrypted_text) // len(key)
    table = [[' ' for _ in range(len(key))] for _ in range(num_rows)]
    
    index = 0
    for col, col_index in order_dict.items():
        for row in range(num_rows):
            table[row][col_index - 1] = encrypted_text[index] if index < len(encrypted_text) else ' '
            index += 1
    decrypted_text = "".join("".join(row) for row in table).rstrip()
    return decrypted_text.replace('*', ' ')

text = input("Enter the text to encrypt: ")
key = input("Enter the key: ")
encrypted_text = encrypt_transposition(text, key)
print("\nEncrypted Text:", encrypted_text)
decrypted_text = decrypt_transposition(encrypted_text, key)
print("Decrypted Text:", decrypted_text)