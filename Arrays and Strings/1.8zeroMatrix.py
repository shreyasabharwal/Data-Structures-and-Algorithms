'''
1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
    column are set to 0.
'''


def zero_matrix(arr):
    list_pos = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                list_pos.append((i, j))

    for i, j in list_pos:
        nullifyRow(arr, i)
        nullifyCol(arr, j)

    return arr


def nullifyRow(arr, row):
    for col in range(len(arr[row])):
        arr[row][col] = 0


def nullifyCol(arr, col):
    for row in range(len(arr)):
        arr[row][col] = 0


if __name__ == "__main__":
    arr = [[1, 0, 3], [4, 5, 6], [0, 7, 8]]
    print(zero_matrix(arr))
