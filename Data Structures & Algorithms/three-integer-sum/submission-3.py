class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answers = []
        for k in range(0, len(nums) -2, 1):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = len(nums) - 1
            value = 0 - nums[k]
            while i < j: 
                index1 = nums[i]
                index2 = nums[j]
                total = index1 + index2
                numbers = [index1, index2, 0 - value]
                if (total == value and numbers not in answers):
                    answers.append(numbers)
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while j > i and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif (total < value): 
                    i += 1
                else:
                    j -= 1
        return answers
        
                    
                




        