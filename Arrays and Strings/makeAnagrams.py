# Hackerrank - Make Anagrams

'''Given two strings,a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

For example, if cde and dcf are given, we can delete e from 1st string and f from 2nd string so that both remaining strings are and cd and dc which are anagrams.'''


def makeAnagram(a, b):
    count = 0
    for i in range(97, 123):
        ia = a.count(chr(i))
        ib = b.count(chr(i))
        count += abs(ia-ib)
    return count


if __name__ == '__main__':
    a = 'naqwmanesd'  # naman - 5
    b = 'xbmaznnma'  # manna - 4
    print(makeAnagram(a, b))
