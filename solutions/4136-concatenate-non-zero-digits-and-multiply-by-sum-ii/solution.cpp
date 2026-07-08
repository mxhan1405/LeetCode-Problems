#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        long long MOD = 1000000007;
        int n = s.length();

        // 1. Fast contiguous pre-allocation
        vector<long long> pow10(n + 1, 1);
        vector<int> idx(n + 1, 0);
        vector<long long> x(n + 1, 0);
        vector<int> total(n + 1, 0);

        for (int i = 0; i < n; ++i) {
            pow10[i + 1] = (pow10[i] * 10) % MOD;
        }

        // 2. Stream-optimized parsing without functions
        int c_idx = 0;
        long long c_x = 0;
        int c_total = 0;

        for (int i = 0; i < n; ++i) {
            int d = s[i] - '0';
            if (d > 0) {
                c_idx++;
                c_x = (c_x * 10 + d) % MOD;
            }
            c_total += d;

            idx[i + 1] = c_idx;
            x[i + 1] = c_x;
            total[i + 1] = c_total;
        }

        // 3. Directly map results into output array
        int q_size = queries.size();
        vector<int> ans(q_size);

        for (int i = 0; i < q_size; ++i) {
            int l = queries[i][0];
            int r = queries[i][1];

            long long digit_sum = total[r + 1] - total[l];
            int shift = idx[r + 1] - idx[l];
            
            long long concatenated_x = (x[r + 1] - x[l] * pow10[shift]) % MOD;
            if (concatenated_x < 0) concatenated_x += MOD; // Safe modulo correction

            ans[i] = (concatenated_x * digit_sum) % MOD;
        }

        return ans;
    }
};

