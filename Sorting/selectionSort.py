# Selection Sort:  Select minimum from array and put it at the beginning


def selectionSort(A):
    for i in range(len(A)):
        # find min
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        # swap
        A[i], A[min_idx] = A[min_idx], A[i]
    return A


if __name__ == "__main__":
    A = [64, 25, 12, 22, 11]
    print(selectionSort(A))

# ## Time complexity: O(n^2). It never makes more than O(n) swaps and can be useful when memory write is a costly operation.
