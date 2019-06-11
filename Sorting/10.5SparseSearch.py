'''10.5 Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
    method to find the location of a given string.
    EXAMPLE
    Input: ball, ['at', '', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
    Output: 4
'''

'''Approach: With empty strings interspersed, we can implement a simple modification of binary search. All we need to
do is fix the comparison against mid, in case mid is an empty string. We simply move mid to the closest
non-empty string.
Careful consideration should be given to the situation when someone searches for the empty string. Should
we find the location (which is an O( n) operation)? Or should we handle this as an error?
'''


def search(l_string, string):
    # if string is empty, return -1. Ask interviewer if this is to be considered as an eror.
    if not string:
        return -1
    return sparseSearch(l_string, string, 0, len(l_string)-1)


def sparseSearch(l_string, string, first, last):
    mid = (first+last)//2
    if string == l_string[mid]:
        return mid
    if last < first:
        return -1

    if not l_string[mid]:
        left = mid-1
        right = mid+1
        while(True):
            if right <= last and l_string[right]:
                mid = right
                break
            elif left >= first and l_string[left]:
                mid = left
                break
            else:
                return -1
            right += 1
            left -= 1

    if string == l_string[mid]:
        return mid
    elif string < l_string[mid]:  # search left
        return sparseSearch(l_string, string, first, mid-1)
    else:
        return sparseSearch(l_string, string, mid+1, last)


if __name__ == "__main__":
    l_string = ['at', '', '', '', '', 'ball',
                '', '', 'car', '', '', 'dad', '', '']
    string = 'dad'
    print(search(l_string, string))
