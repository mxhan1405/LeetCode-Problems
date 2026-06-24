class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        num_vals = r - l + 1
        dim = 2 * num_vals
        
        def multiply(A, B):
            C = [[0] * dim for _ in range(dim)]
            for i in range(dim):
                for k in range(dim):
                    if not A[i][k]:
                        continue
                    for j in range(dim):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def power(matrix, p):
            res = [[0] * dim for _ in range(dim)]
            for i in range(dim):
                res[i][i] = 1
            base = matrix
            while p > 0:
                if p % 2:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res

        M = [[0] * dim for _ in range(dim)]
        for i in range(num_vals):
            for j in range(i + 1, num_vals):
                M[i][num_vals + j] = 1
            for j in range(i):
                M[num_vals + i][j] = 1

        M_pow = power(M, n - 1)
        initial_vector = [1] * dim
        
        ans = 0
        for i in range(dim):
            row_sum = 0
            for j in range(dim):
                row_sum = (row_sum + M_pow[i][j] * initial_vector[j]) % MOD
            ans = (ans + row_sum) % MOD
            
        return ans

