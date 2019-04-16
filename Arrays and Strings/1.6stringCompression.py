
'''
1.6 String Compression: Implement a method to perform basic string compression using the counts
    of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
    "compressed" string would not become smaller than the original string, your method should return
    the original string. You can assume the string has only uppercase and lowercase letters(a - z).
'''
import sys


def string_compression(string):
    compressed = []
    count = 1
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            compressed.append(string[i]+str(count))
            count = 1
    # appending last character
    compressed.append(string[-1] + str(count))
    compressed = ''.join(compressed)

    # if counts of all characters are one, len(compressed)=2*len(string)
    if len(compressed) == 2*len(string):
        return string
    return compressed


if __name__ == "__main__":
    string = sys.argv[1]
    print(string_compression(string))
