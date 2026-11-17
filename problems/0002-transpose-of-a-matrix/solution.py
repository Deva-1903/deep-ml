import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here

    # NumPy code
    # A = np.asarray(a)

    # B = np.transpose(A)

    # return B.tolist()


    # a = [[1, 2, 3], [4, 5, 6]]

    rows = len(a) # 2
    cols = len(a[0])

    b = []
   
    # Step 1: Create empty transposed matrix
    for i in range(cols):
        new_row = []

        for j in range(rows):
            new_row.append(0)

        b.append(new_row)

    # Copy the values
    for i in range(rows):
        for j in range(cols):
            b[j][i] = a[i][j]

    
    return b

        




