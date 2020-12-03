# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:32:54 2020

@author: kalan
"""

# =============================================================================
# 1672. Richest Customer Wealth
# 
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
# 
#  
# 
# Example 1:
# 
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.
# Example 2:
# 
# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation: 
# 1st customer has wealth = 6
# 2nd customer has wealth = 10 
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.
# Example 3:
# 
# Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17
# =============================================================================


class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        
        outs = []
        for person in accounts:
            out = 0
            for account in person:
                out += account
            
            outs.append(out)
        
        return max(outs)


a=Solution()
a.maximumWealth(accounts = [[1,2,3],[3,2,1]]) 
a.maximumWealth(accounts = [[1,5],[7,3],[3,5]])
a.maximumWealth(accounts = [[2,8,7],[7,1,3],[1,9,5]])       