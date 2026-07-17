class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        for i in range (len(nums)): 
            if (i == 0):
                prefixProduct = [nums[0]]
                suffixProduct = [nums[(len(nums)-1)]]
            else:
                prefixProduct.append(prefixProduct[i-1]*nums[i])
                suffixProduct.append(suffixProduct[i-1]*nums[(len(nums)-1)-i])
        answer = []
        for i in range (len(nums)):
            if (i == 0):
                answer.append(suffixProduct[(len(nums) - 2)])
            elif (i == (len(nums) - 1)):
                answer.append(prefixProduct[i-1])
            else: 
                answer.append(suffixProduct[len(nums)-2-i]*prefixProduct[i-1])
        return answer