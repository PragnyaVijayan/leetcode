# Last updated: 9/18/2025, 11:23:15 PM
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        for account in accounts:
            wealth.append(sum(account))
        
        return max(wealth)

        