class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for customer in accounts:
            customer_wealth = sum(customer)
            if customer_wealth > max_wealth:
                max_wealth = customer_wealth
        return max_wealth