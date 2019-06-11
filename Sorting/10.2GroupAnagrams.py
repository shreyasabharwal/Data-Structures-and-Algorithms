'''10.2 Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
each other.
'''


'''Approach: We can do this by using a hash table which maps from the sorted version of a word to a list of its anagrams.
So, for example, acre will map to the list {acre, race, care}. Once we've grouped all the words into
these lists by anagram, we can then put them back into the array.'''


def groupAnagrams(l_strings):
    anagrams = {}
    for string in l_strings:
        sortedWord = ''.join(sorted(string.lower()))
        if sortedWord not in anagrams:
            anagrams[sortedWord] = []
        anagrams[sortedWord].append(string)

    # converting dict values to list
    list_str = []
    for v in anagrams.values():
        list_str.extend(v)
    return list_str


if __name__ == "__main__":
    l_strings = ['alerted', 'acre', 'altered',
                 'later', 'race', 'alter', 'care', 'alert']
    print(groupAnagrams(l_strings))
