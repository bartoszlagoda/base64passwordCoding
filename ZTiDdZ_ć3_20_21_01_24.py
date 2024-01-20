import base64
import random
import string


def codePassToBase64(encodePassword):
    # Method that encodes the given string into base64
    encodePassToByte = encodePassword.encode('ascii')
    encodePassTob64 = base64.b64encode(encodePassToByte)
    decodePass = encodePassTob64.decode('ascii')
    return decodePass

def generate_new_password():
    # Variables that create all possible characters in a password
    big_letters = string.ascii_uppercase
    small_letters = string.ascii_lowercase
    digits = string.digits
    special_signs = string.punctuation

    # Creating the first password containing all the above variables
    all_signs = big_letters + small_letters + digits + special_signs

    # generating a password with a length of not less than 8 characters and not more than 12
    password = random.choice(big_letters) + random.choice(small_letters) + random.choice(digits) + random.choice(special_signs)
    password += ''.join(random.choice(all_signs) for i in range(random.randint(4,12)))

    # Mix the password
    password = ''.join(random.sample(password, len(password)))

    return password

# Uruchomienie metod i testowanie
if __name__ == '__main__':
    first_pass_b64 = codePassToBase64('alamakota')
    print(first_pass_b64)
    second_pass_b64 = codePassToBase64('e2r4t5y6u7i8o9p0a0s9d8f7g6h5j4k3l2-a1s2!34%g6h&j*!a')
    print(second_pass_b64)

    firstPass = generate_new_password()
    secondPass = generate_new_password()
    thirdPass = generate_new_password()

    print(firstPass)
    print(secondPass)
    print(thirdPass)
