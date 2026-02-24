def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    ans = [[] for _ in range(0, len(a[0]))]

    numRows = len(a)
    numCols = len(a[0])
    for col in range(0, numCols):
        for row in range(0, numRows):
            ans[col].append(a[row][col])
    return ans

print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))