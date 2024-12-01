import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Please enter a positive integer.")
            return value
        except ValueError as e:
            print(e)

def encrypt(text, public_key):
    e, n = public_key['e'], public_key['n']
    encrypted_text = []
    for char in text:
        encrypted_char = pow(ord(char), e, n)
        encrypted_text.append(encrypted_char)
    return encrypted_text

def decrypt(encrypted_text, private_key):
    d, n = private_key['d'], private_key['n']
    decrypted_text = ''.join([chr(pow(char, d, n)) for char in encrypted_text])
    return decrypted_text

p = get_input("Enter the 1st Prime No. : ")
q = get_input("Enter the 2nd Prime No. : ")

if not (is_prime(p) and is_prime(q)):
    print("One or both of the entered numbers are not prime.")
else:
    n = p * q
    print("n =", n)
    phi_n = (p - 1) * (q - 1)
    print("Phi(n) =", phi_n)

    e = get_input("Enter the value of e : ")

    if math.gcd(e, phi_n) != 1:
        print("Error: gcd(e, Phi(n)) is not 1. Please choose another value for e.")
    else:
        d = pow(e, -1, phi_n)
        print("d =", d)

        public_key = {'e': e, 'n': n}
        print("\nPublic key is :", public_key)

        private_key = {'d': d, 'n': n}
        print("Private key is :", private_key)

        plaintext = input("\nEnter the plaintext: ")
        print("------------------------------------------")

        encrypted_text = encrypt(plaintext, public_key)
        print("Performing Encryption with: C=M^e mod n")
        print("Encrypted text:", encrypted_text)

        decrypted_text = decrypt(encrypted_text, private_key)
        print("\nPerforming Decryption with: C=M^e mod n")
        print("Decrypted text:", decrypted_text)
        print("------------------------------------------")
