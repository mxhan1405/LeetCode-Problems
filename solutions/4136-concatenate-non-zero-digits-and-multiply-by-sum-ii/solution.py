class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        n = len(s)

        pow10 = [1] * (n + 1)
        curr = 1
        for i in range(1, n + 1):
            curr = (curr * 10) % MOD
            pow10[i] = curr

        idx = [0] * (n + 1)
        x = [0] * (n + 1)
        total = [0] * (n + 1)

        c_idx, c_x, c_total = 0, 0, 0
        for i, ch in enumerate(s):
            d = ord(ch) - 48
            if d:
                c_idx += 1
                c_x = (c_x * 10 + d) % MOD
            c_total += d
            
            idx[i + 1] = c_idx
            x[i + 1] = c_x
            total[i + 1] = c_total

        return [
            ((x[r + 1] - x[l] * pow10[idx[r + 1] - idx[l]]) * (total[r + 1] - total[l])) % MOD
            for l, r in queries
        ]

