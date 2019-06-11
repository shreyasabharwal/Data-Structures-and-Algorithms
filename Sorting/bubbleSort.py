# Bubble Sort: Repeatedly swapping the adjacent elements if they are in wrong order. In one iteration the largest element bubbles down to the bottom


def bubbleSort(A):
    for i in range(len(A)):
        for j in range(0, len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A


if __name__ == "__main__":
    A = [64, 25, 12, 22, 11]
    print(bubbleSort(A))


# Time complexity: O(n^2) in worst case(when array is sorted in reverse order). In Best case - O(n) (when array is sorted )
