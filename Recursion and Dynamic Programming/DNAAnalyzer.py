'''
DNA Analyser:

Write python code to generate a report on the statistical occurrences of various amino acids in a given string. This consists of 3 parts-

Part 1:
It should read the DNA strands from a given list of strings in which every element represents a single strand. The method should refine and update the list to contain valid strands "only". A strand is valid when:
1. its length is greater than 10,
2. its length is less than 100,
3. it contains only 'A', 'T', 'G', 'C' characters,
4. it's not an empty string,
5. all characters are in uppercase.
When the number of clean strands is less than 3, the method should stop its execution and return an empty string.

Part 2:
Using the refined list, now you should find overlapping elements and build one long strand which would be returned as a string. Two strands overlap when last 3 characters of the first one match exactly 3 first characters of the second strand.  The following rules should be used for building the resulting string.
1. All input strands must overlap.
2. When two strands overlap they should be merged, eg. 'AAACCCAATTT' and 'TTTACACAGCT' should be merged to 'AAACCCAATTTACACAGCT' - the overlapping part should not be repeated.
3. One strand must overlap with another one only by the end of it - this is the starting strand.
4. One strand must overlap with another one by the beginning of it - this is the ending strand.
5. All other strands must overlap on both ends.
Please note, the starting and ending strands can be anywhere in the received list.

Part 3:
The last part of this task is to actually generate the report. Now the constructed string should be split into 3-character long substrings. Each substring is a codon specifying an amino acid. Based on the given populated dictionary('codon mapping'), count the amino acids occurrences in the given sequence. The method should finally return a string consisting of alphabetically sorted amino acids and their count(colon-separated, one per line as depicted below).

For sequence 'AAATTTGGGAAA' and 'codon_mapping' dictionary with following values:
AAA Lysine
GGG Glycine
TTT Phenylalanine

the expected outcome is
Glycine: 1
Lysine:2
Phenylalanine: 1
'''


def dna_analyser_part3(valid_str):
    # source: https://pythonforbiologists.com/dictionaries
    codon_mapping = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}
    substr_list = []
    for i in range(0, len(valid_str), 3):
        substr_list.append(valid_str[i:i+3])

    dict_amino = {}
    for string in substr_list:
        if string in codon_mapping:
            if codon_mapping[string] not in dict_amino:
                dict_amino[codon_mapping[string]] = 1
            else:
                dict_amino[codon_mapping[string]] += 1

    tup_amino = sorted(dict_amino.items())

    for tup in tup_amino:
        print(tup[0], ':', tup[1])


def dna_analyser_part1(list_str):
    chars = ['A', 'T', 'G', 'C']
    valid_list = []
    for string in list_str:
        valid = True
        if len(string) > 10 and len(string) < 100 and string.isupper() and string:
            for char in string:
                if char not in chars:
                    valid = False
                    break
            if valid == True:
                valid_list.append(string)
    return valid_list


def dnaRecurse(valid_str, step=0):
    overlap = False
    # base case: if length of valid_str reduces to one or step is greater than the length of valid_str
    if len(valid_str) == 1 or step >= len(valid_str):
        return valid_str

    str1 = valid_str[step]
    endStr = str1[-3:]

    for i in range(len(valid_str)):
        if valid_str[i] != str1 and endStr == valid_str[i][:3]:
            valid_str[step] = str1[:-3] + valid_str[i]
            del valid_str[i]
            overlap = True
            break
    # if there was no overlap, increment step to 1.
    if not overlap:
        step += 1
        dnaRecurse(valid_str, step)
    # if there was an overlap, i.e. strings were combined, move step to 0.
    else:
        dnaRecurse(valid_str, step=0)

    return valid_str


def dna_analyser_part2(valid_str):
    # ['TTTACACAGCT', 'AAACCCAATTT', 'AAATTGGGAAA']
    if dnaRecurse(valid_str):
        return dnaRecurse(valid_str)[0]


if __name__ == "__main__":
    list_str = ['TTTACACAGCT', 'AAACCCAATTT', 'AAA', '',
                'aaatttgggaaa', 'AAATTTGGGAAAMMM', 'AAATTGGGAAA', 'GCTATCATTATG']
    # part 1
    valid_str = dna_analyser_part1(list_str)
    # print(valid_str)
    # part 2
    valid_str2 = dna_analyser_part2(valid_str)
    print(valid_str2)
    dna_analyser_part3(valid_str2)
