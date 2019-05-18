'''8.3 Magic Index: A magic index in an array A [0 ... n -1] is defined to be an index such that A[ i] =
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.

FOLLOW UP
What if the values are not distinct?
Hints: # 170, #204, #240, #286, #340'''

''' This could be done using linear search, but use the information provided: "sorted array of distinct integers"'''


def magicIndex(arr, start, end):
    if end < start:
        return -1
    mid = (start+end)//2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return magicIndex(arr, start=start, end=mid-1)
    else:
        return magicIndex(arr, start=mid+1, end=end)
    return None


def getMagicIndex(arr):
    return magicIndex(arr, start=0, end=len(arr)-1)


def magicIndexNd(arr, start, end):
    if end < start:
        return -1
    mid = (start+end)//2
    if arr[mid] == mid:
        return mid

    # search left index
    leftEnd = min(mid-1, arr[mid])
    left = magicIndexNd(arr, start, leftEnd)
    if left > 0:
        return left
    # search right index
    rightStart = max(mid+1, arr[mid])
    right = magicIndexNd(arr, rightStart, end)
    if right > 0:
        return right


def getMagicIndexNd(arr):
    return magicIndexNd(arr, start=0, end=len(arr)-1)


if __name__ == "__main__":
    testArr = [-2, -1, 0, 1, 4, 7, 8, 11, 90, 600, 601]
    print('Magic number if numbers are distinct:', getMagicIndex(testArr))

    testArr_1 = [-2, 1, 1, 1, 3, 4, 8, 11, 90, 600, 601]
    print('Magic number if numbers are not distinct: ',
          getMagicIndexNd(testArr_1))
