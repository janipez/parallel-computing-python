import multiprocessing
from multiprocessing import Barrier
from multiprocessing.context import Process
import time
from random import Random


process_count = 8
matrix_size = 200
random = Random()


def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row * matrix_size + col] = random.randint(-10, 10)


def work_out_row(id, matrix_a, matrix_b, matrix_result, work_start, work_complete):
    while(True):
        work_start.wait()

        for row in range(id, matrix_size, process_count):
            for col in range(matrix_size):
                for i in range(matrix_size):
                    matrix_result[row * matrix_size + col] += matrix_a[row * matrix_size + col] * matrix_b[row * matrix_size + col]

        work_complete.wait()


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    work_start = Barrier(process_count + 1)
    work_complete = Barrier(process_count + 1)

    matrix_a = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    matrix_b = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    matrix_result = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)

    start = time.time()

    for p in range(process_count):
        Process(target=work_out_row, args=(p, matrix_a, matrix_b, matrix_result, work_start, work_complete)).start()

    for t in range(10):
        generate_random_matrix(matrix_a)
        generate_random_matrix(matrix_b)

        for i in range(matrix_size * matrix_size):
            matrix_result[i] = 0

        work_start.wait()
        work_complete.wait()

        # for row in range(matrix_size):
        #    print(matrix_a[row], "\t", matrix_b[row], "\t", matrix_result[row])

    end = time.time()

    print("Done, time taken: ", end - start)
