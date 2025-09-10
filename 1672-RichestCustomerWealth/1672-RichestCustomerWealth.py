# Last updated: 9/9/2025, 9:04:18 PM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        for account in accounts:
            wealth.append(sum(account))
        
        return max(wealth)

        