'''10.1 Sorted Merge:
    You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.
'''

'''Approach: If we insert an element into the front of A, then we'll have to shift the existing elements backwards to make room for it. It's better to insert elements into the back of the array, where
there's empty space.'''


def sortedMerge(A, B):
    mergedIndex = len(A)-1
    indexB = len(B)-1
    indexA = len(A)-len(B)-1

    while(indexB >= 0):
        if indexA > 0 and A[indexA] >= B[indexB]:
            A[mergedIndex] = A[indexA]
            indexA -= 1
        else:
            A[mergedIndex] = B[indexB]
            indexB -= 1
        mergedIndex -= 1

    return A


if __name__ == "__main__":
    lengthA = 5  # original length of A
    lengthB = 10  # Original length of B
    buffer = abs(lengthA-lengthB)
    A = [0]*(lengthA+lengthB)  # length = 15, buffer = 10
    B = [0]*(lengthB)  # length = 10
    for i in range(lengthA):
        A[i] = 3*i
    for i in range(lengthB):
        B[i] = 2*i
    print(sortedMerge(A, B))

    # [0, 3, 6, 9, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
