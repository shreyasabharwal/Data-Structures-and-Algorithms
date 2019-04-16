'''
1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
    bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''


def rotate_matrix(arr):
    # outer layer
    for i in range(len(arr)//2):
        # inner layer
        for j in range(i, len(arr)-i-1):
            tmp = arr[i][j]
            arr[i][j] = arr[len(arr)-j-1][i]
            arr[len(arr)-j-1][i] = arr[len(arr)-i-1][len(arr)-j-1]
            arr[len(arr)-i-1][len(arr)-j-1] = arr[j][len(arr)-i-1]
            arr[j][len(arr)-i-1] = tmp
    return arr


if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_matrix(arr))
