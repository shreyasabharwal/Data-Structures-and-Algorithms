'''10.3 Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array. You may assume that the array was
originally sorted in increasing order.
EXAMPLE
Input: find 5 in [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
Output: 8 (the index of 5 in the array)
'''


def searchArray(arr, num):
    return searchRotatedArray(arr, 0, len(arr)-1, num)


def searchRotatedArray(arr, left, right, num):
    mid = (left+right)//2
    if num == arr[mid]:
        return mid
    if right < left:
        return -1

    if arr[left] < arr[mid]:  # left is sorted in increasing order
        if num > arr[left] and num < arr[mid]:
            # search left side
            return searchRotatedArray(arr, left, mid-1, num)
        else:
            # search right side
            return searchRotatedArray(arr, mid+1, right, num)

    elif arr[mid] < arr[right]:  # right is sorted in increasing order
        if num > arr[mid] and num < arr[right]:
            # search right side
            return searchRotatedArray(arr, mid+1, right, num)
        else:
            # search left side
            return searchRotatedArray(arr, left, mid-1, num)

    # if left and middle are identical, eg: [2, 2, 2, 3, 4, 2]
    elif arr[mid] == arr[left]:
        if arr[mid] != arr[right]:  # search right if right!=left
            return searchRotatedArray(arr, mid+1, right, num)
        else:
            # search both sides
            index = searchRotatedArray(arr, left, mid-1, num)
            if index == -1:
                return searchRotatedArray(arr, mid+1, right, num)
            else:
                return index

    return -1


if __name__ == "__main__":
    #arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    arr = [2, 2, 2, 3, 4, 2]
    num = 4
    print(searchArray(arr, num))
