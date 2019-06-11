# Insertion Sort: The way we sort playing cards. Insert the card at the beginning if it is less than the previous cards.


def insertionSort(A):
    for i in range(1, len(A)):
        elem = A[i]
        j = i-1
        while(j >= 0 and elem < A[j]):
            A[j+1] = A[j]
            j = j-1
        A[j+1] = elem
    return A


if __name__ == "__main__":
    A = [64, 25, 12, 22, 11]
    print(insertionSort(A))
