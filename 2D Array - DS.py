
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

def hourglassSum(arr):

    array_length = len(arr) - 2
    middle_length = len(arr[0][1:-1])
    sums = []
    for i in range(array_length):
        for j in range(middle_length):

            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i + 1][j+1]
            bottom = arr[i + 2][j] + arr[i + 2][j+1] + arr[i + 2][j+2]

            hourglass_sum = top + middle + bottom
            sums.append(hourglass_sum)

    print(max(sums))

hourglassSum(arr)