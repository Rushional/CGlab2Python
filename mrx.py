from math import sin, cos

# матрицы проекций
iso = [[0.707, 0.408, 0., 0.], [0., 0.816, 0., 0.], [0.707, -0.408, 0., 0.], [0., 0., 0., 1.]]
dim = [[0.926, 0.134, 0., 0.], [0., 0.935, 0., 0.], [0.378, -0.327, 0., 0.], [0., 0., 0., 1.]]
# матрица непроецированных осей осей
axis = [[0, 0, 0, 1], [10000, 0, 0, 1], [0, -10000, 0, 1], [0, 0, -10000, 1]]


# Перемножение двух матриц
def mrx_mult(A, B):
    col_num1 = len(A[0])
    col_num2 = len(B[0])
    row_num1 = len(A)
    row_num2 = col_num1
    a = [[0] * col_num2 for i in range(row_num1)]

    if len(B) != len(A[0]):
        print("Матрицы не могут быть перемножены")
    else:
        # print("ВСЕМОГУЩИЙ")
        for i in range(row_num1):
            for j in range(col_num2):
                for k in range(col_num1):
                    a[i][j] = a[i][j] + A[i][k] * B[k][j]
    return (a)


# умножение матрицы на список матриц
def mult_mrx_mult(A, BList):
    a = A
    for i in BList:
        a = mrx_mult(a, i)
    return (a)


# умножение матрицы на число
def n_mult(A, N):
    cols = len(A[0])
    rows = len(A)
    a = A
    for i in range(rows):
        for j in len(cols):
            a[i][j] = a[i][j] * N
    return (a)


# сумма двух матриц
def sum(A, B):
    a = A
    for i in range(len(A)):
        for j in range(len(A[0])):
            a[i][j] = a[i][j] + B[i][j]
    return (a)


# к каждому элемменту матрцы суммируется число N(СОМНИТЕЛЬНАЯ ВАЖНОСТЬ)
def n_sum(A, N):
    a = A
    for i in range(len(A)):
        for j in range(len(A[0])):
            a[i][j] = a[i][j] + N
    return (a)


# получение матрицы поворота относительно оси по углу в пи (ПРОВЕРИТЬ У)
def rotate_x(phi):
    return ([[1, 0, 0, 0],
             [0, cos(phi), -sin(phi), 0],
             [0, sin(phi), cos(phi), 0],
             [0, 0, 0, 1]])


def rotate_y(phi):
    return ([[cos(-phi), 0, -sin(-phi), 0],
             [0, 1, 0, 0],
             [sin(-phi), 0, -cos(phi), 0],
             [0, 0, 0, 1]])
