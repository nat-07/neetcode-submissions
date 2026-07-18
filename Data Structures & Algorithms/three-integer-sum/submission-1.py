class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        answers = []
        for k in range(0, len(sortedNums) -2, 1):
            if k > 0 and sortedNums[k] == sortedNums[k-1]:
                continue
            i = k + 1
            j = len(sortedNums) - 1
            value = 0 - sortedNums[k]
            while i < j: 
                index1 = sortedNums[i]
                index2 = sortedNums[j]
                total = index1 + index2
                numbers = [index1, index2, 0 - value]
                if (total == value and numbers not in answers):
                    answers.append(numbers)
                    while i < j and sortedNums[i] == sortedNums[i+1]:
                        i += 1
                    while j > i and sortedNums[j] == sortedNums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif (total < value): 
                    i += 1
                else:
                    j -= 1
                    
        return answers
        
                    
                




        