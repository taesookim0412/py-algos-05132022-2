# https://leetcode.com/discuss/interview-question/1273766

class Solution:
    def longestCommonSubstring(self, word1, word2):
        res = 0
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i, char1 in enumerate(word1):
            for j, char2 in enumerate(word2):
                if char2 == char1:
                    dp[i+1][j+1] = 1 + dp[i][j]
                    res = max(res, dp[i+1][j+1])
        # print(dp)
        return res

s = Solution()
print(s.longestCommonSubstring("3bcdaf", "abcdf"))