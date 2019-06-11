# merge sort


def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr)//2
        L = arr[:m]
        R = arr[m:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while(i < len(L) and j < len(R)):
            if L[i] < R[j]:
                arr[k] = L[i]
                i = i+1
            elif L[i] > R[j]:
                arr[k] = R[j]
                j = j+1
            else:
                arr[k] = L[i]
                i = i+1
                j = j+1
            k = k+1

        while (i < len(L)):
            arr[k] = L[i]
            i = i+1
            k = k+1

        while (j < len(R)):
            arr[k] = R[j]
            j = j+1
            k = k+1

    return arr


if __name__ == "__main__":
    A = [64, 25, 12, 22, 11]
    print(mergeSort(A))


# Time Complexity: O(nlogn). It is pretty efficient. The downside is that it requires extra space. Space complexity: o(n)
