class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def compress(mat):
            compress_dict = defaultdict(list)
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if mat[i][j] != 0:
                        compress_dict[i].append((j, mat[i][j]))
            return compress_dict
        
        m = len(mat1)
        n = len(mat2[0])

        A = compress(mat1)
        B = compress(mat2)
        res = [[0 for _ in range(n)] for _ in range(m)]

        for mat1_row in range(m):
            for col1, val1 in A[mat1_row]:
                for col2, val2 in B[col1]:
                    res[mat1_row][col2] += val1 * val2

        return res

# Have a hash table with the key being a row and the value being (column, val) for non-zero vals for both matrices
# If 2 matrices are A x B and B x C, then the product would be A x C
# Iterate through the rows of the first matrix to get the non-zero columns/vals, multiply them with the corresponding row index (this case being mat1's column) of the other matrix
