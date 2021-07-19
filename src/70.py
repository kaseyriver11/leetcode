"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        if n < 4:
            return n
        count0 = 2
        count1 = 3
        n2 = 3
        while n2 != n:
            new_sum = count0 + count1
            count0 = count1
            count1 = new_sum
            n2 += 1
        return new_sum
        
        

Solution.climbStairs(1)
Solution.climbStairs(5)
Solution.climbStairs(3)
