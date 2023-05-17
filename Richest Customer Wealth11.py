class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        rich=0
        for i in accounts:
            rich=max(rich,sum(i))
        return rich
    
# https://leetcode.com/problems/richest-customer-wealth/description/