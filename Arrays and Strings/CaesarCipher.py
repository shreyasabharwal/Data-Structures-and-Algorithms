'''A Caesar Cipher is a simple and ancient encryption technique. It works by taking the a string of text and "rotating" each letter a fixed number of places down the alphabet. Thus if the "rotation" number is "3", then a A (the 1st letter) would become a D (the 4th), a B would become a E, and a Z would wrap around to become a C.

Define a method rotate_text() that takes in two arguments: a string to encrypt and a number of places to shift each letter. The method should return an "encrypted" version of the string, with each letter shifted the appropriate amount. Note that this method can also be used to "decrypt" text by shifting in the opposite direction (e.g., a negative amount).'''


def rotate_text(string, num):
    res = ""
    for char in string:
        if char.isalnum():
            if char.isupper():
                res += (chr((ord(char)+num-65) % 26+65))
            else:
                res += (chr((ord(char)+num-97) % 26+97))
        else:
            res += char
    return res


if __name__ == "__main__":
    print(rotate_text('This is a programming class', 5))
    print(rotate_text('YMNX NX F UWTLWFRRNSL HQFXX', -5))
