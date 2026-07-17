class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        largest = 0
        for num in nums: 
            if num - 1 not in nums: 
                y = num + 1
                while y in nums:
                    y += 1
                largest = max(largest, y - num)
        return largest