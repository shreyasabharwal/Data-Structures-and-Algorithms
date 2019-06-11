# quick sort: Quick Sort is the standard and is used as the default in almost all software languages.


def quickSortMain(arr):
    return quickSort(arr, 0, len(arr)-1)


def quickSort(arr, left, right):
    if left >= right:
        return arr
    pivot = arr[(left+right)//2]
    index = partition(arr, left, right, pivot)
    quickSort(arr, left, index-1)
    quickSort(arr, index, right)


def partition(arr, left, right, pivot):
    while (left <= right):
        while(arr[left] < pivot):
            left += 1
        while(arr[right] > pivot):
            right -= 1
        if left <= right:
            arr[left],  arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left


if __name__ == "__main__":
    A = [64, 25, 12, 22, 11]
    quickSortMain(A)
    print(A)
