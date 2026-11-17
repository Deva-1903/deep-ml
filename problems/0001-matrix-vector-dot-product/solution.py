
import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.

    # NumPy solution
    A = np.asarray(a)
    v = np.asarray(b)

    if A.ndim != 2 or A.shape[1] != v.shape[0]:
        return -1

    return (A @ v).tolist()

    # normal solution
    # result = []

    # for row in a:
    #     if len(row) != len(b):
    #         return -1

    #     score = 0
    #     for j in range(len(row)):
    #         score += row[j] * b[j]
        
    #     result.append(score)


    # return result