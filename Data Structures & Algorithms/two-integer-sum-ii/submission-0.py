class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Since the solution must only have constant extra space, prefix sum is not considered
        # There will only be one solution
        # If one of the pointers is larger than the target, it is impossible to be part of the answer, unless the other pointer is negative and suceeds at it.
        # case 1: [-2, 0, 19 ,20] target = 19 - should accept  
        # 20 + -2 = 18, less than target 
        # 0 + 20 = 20, more than target

        # case 2: [2,7,11,15] target = 9 - should accept  
        # 2+ 15 = 17, more than target 
        # 2+ 11 = 13, more than target
        # 2+7 = 9 //

        i = 0 
        j = len(numbers) - 1
        while i < j: 
            if numbers[i] + numbers[j] == target:
                return[i+1,j+1]
            elif numbers[i] + numbers[j] < target: 
                i += 1
            else: 
                j -= 1
        