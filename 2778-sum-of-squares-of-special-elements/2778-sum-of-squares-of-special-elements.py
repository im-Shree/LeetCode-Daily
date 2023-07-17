class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
        n = len(nums)
        special_sum = sum(map(lambda i: nums[i-1]**2 if n % i == 0 else 0, range(1, n+1)))
        
        return special_sum
       
        