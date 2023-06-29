def matrix(mat1, mat2):
    rows= len(mat1)
    cols  = len(mat1[0])
    res = [[0 for s in range(cols)] for v in range(rows)]

    for i in range (rows):
        for j in range(cols):
            res[i][j] = mat1[i][j] + mat2[i][j]

    print(res)

mat1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]

mat2 = [[9,8,7],
        [6,5,4],
        [3,2,1]]

res = matrix(mat1, mat2)