import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    
    A = np.asarray(a)

    old_rows = len(a)
    old_cols = len(a[0])

    new_rows = new_shape[0]
    new_cols = new_shape[1]

    if (old_rows * old_cols)  != (new_cols * new_rows):
        return []

    
    flat = []

    for row in a:
        for j in row:
            flat.append(j)

    reshaped_matrix = []
    index = 0

    for i in range(new_rows):
        new_row = []

        for j in range(new_cols):
            new_row.append(flat[index])
            index = index + 1

        reshaped_matrix.append(new_row)

    
    return reshaped_matrix
