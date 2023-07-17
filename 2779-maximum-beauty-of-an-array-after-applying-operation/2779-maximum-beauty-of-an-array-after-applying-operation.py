class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        """We will sort the given array
        then we will initiate 'i' and use it to track an subarray that we will create.
        'j' will be used to iterate over the given array
        At given index where given condition isn't satified, we will eliminate the   element from sub array.
        eventually we will return the difference between i & j arrays(j - i +1)."""
        nums.sort()
        i = 0
        
        for j in range(len(nums)):
            
            if nums[j] - nums[i] > k*2:
                i += 1
        
        return j - i + 1
        