import time
from random import Random


matrix_size = 200

# matrix_a = [[3, 1, -4],
#            [2, -3, 1],
#            [5, -2, 0]]

# matrix_b = [[1, -2, -1],
#            [0, 5, 4],
#            [-1, -2, 3]]

matrix_a = [[0] * matrix_size for r in range(matrix_size)]
matrix_b = [[0] * matrix_size for r in range(matrix_size)]
matrix_result = [[0] * matrix_size for r in range(matrix_size)]
random = Random()


def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row][col] = random.randint(-10, 10)


start = time.time()

for t in range(10):
    generate_random_matrix(matrix_a)
    generate_random_matrix(matrix_b)
    matrix_result = [[0] * matrix_size for r in range(matrix_size)]

    for row in range(matrix_size):
        for col in range(matrix_size):
            for i in range(matrix_size):
                matrix_result[row][col] += matrix_a[row][i] * matrix_b[i][col]

    # for row in range(matrix_size):
    #    print(matrix_a[row], "\t", matrix_b[row], "\t", matrix_result[row])

end = time.time()

print("Done, time taken: ", end - start)