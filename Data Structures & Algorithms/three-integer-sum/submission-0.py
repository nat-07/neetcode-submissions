class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        answers = []
        sets = []
        for k in range(0, len(sortedNums) -2, 1):
            i = k + 1
            j = len(sortedNums) - 1
            value = 0 - sortedNums[k]
            while i < j: 
                index1 = sortedNums[i]
                index2 = sortedNums[j]
                total = index1 + index2
                numbers = set([index1, index2, 0 - value])
                if (total == value and numbers not in sets):
                    answers.append([index1, index2, 0 - value])
                    sets.append(numbers)
                if (total < value): 
                    i += 1
                elif (total > value):
                    j -= 1
                else: 
                    i +=1
                    j -=1
        return answers
        