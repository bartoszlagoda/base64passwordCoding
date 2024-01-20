import base64
import random
import string


def kodujHasloNaBase64(encodePassword):
    # metoda kodująca podanego stringa do base64
    enkodujHasloDoBajtow = encodePassword.encode('ascii')
    enkodujHaslo = base64.b64encode(enkodujHasloDoBajtow)
    dekodujHasloDoAscii = enkodujHaslo.decode('ascii')
    return dekodujHasloDoAscii

def generuj_haslo():
    # Zmienne tworzące wszystkie możliwe znaki w haśle
    wielkie_litery = string.ascii_uppercase
    male_litery = string.ascii_lowercase
    cyfry = string.digits
    znaki_specjalne = string.punctuation

    # Stworzenie pierwszego hasła zawierającego wszystkie powyższe zmienne
    wszystkie_znaki = wielkie_litery + male_litery + cyfry + znaki_specjalne

    # generowanie hasła o długości nie mniejszej niż 8 znaków i nie większej niż 12
    haslo = random.choice(wielkie_litery) + random.choice(male_litery) + random.choice(cyfry) + random.choice(znaki_specjalne)
    haslo += ''.join(random.choice(wszystkie_znaki) for i in range(random.randint(4,12)))

    # Mieszamy hasło
    haslo = ''.join(random.sample(haslo, len(haslo)))

    return haslo

# Uruchomienie metod i testowanie
if __name__ == '__main__':
    pierwsze_haslo_b64 = kodujHasloNaBase64('alamakota')
    print(pierwsze_haslo_b64)
    drugie_haslo_b64 = kodujHasloNaBase64('e2r4t5y6u7i8o9p0a0s9d8f7g6h5j4k3l2-a1s2!34%g6h&j*!a')
    print(drugie_haslo_b64)

    pierwszeHaslo = generuj_haslo()
    drugieHaslo = generuj_haslo()
    trzecieHaslo = generuj_haslo()

    print(pierwszeHaslo)
    print(drugieHaslo)
    print(trzecieHaslo)
