# Count pairs in a sorted array whose product is less than k in O(n)


def countPairs(string, k):
    left = 0
    right = len(string)-1
    count = 0

    while(left < right):
        if(string[left]*string[right] < k):
            count += (right-left)
            left += 1
        else:
            right -= 1
    return count


if __name__ == "__main__":
    string = [2, 3, 5, 6, 9, 13, 15]
    k = 16
    print(countPairs(string, k))
