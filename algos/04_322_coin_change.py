class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialize it to a number never reachable
        dp = [sys.maxsize for _ in range(amount + 1)]

        # base case: if we have need amount = 5 and we have a coin = 5,
        # then when indexAmount is 5, coin is 5, then dp[indexAmount - coin] + 1 gives 1 coin.
        # Now consider the case when we need indexAmount = 8 and coin is 3.
        # Then dp[i] = min(dp[i], 1 + dp[i - coin]) => 2 coins
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin > -1:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == sys.maxsize:
            return -1
        return dp[amount]