class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a hashmap to store the frequencies 
        hashmap = {}
        for n in nums: 
            if n in hashmap: 
                hashmap[n] += 1
            else: 
                hashmap[n] = 1
        # Now we have the frequencies, how do we get the top without sorting?
        array = [[] for _ in range(len(nums) + 1)]
        for n in hashmap: 
            array[hashmap[n]].append(n)
        answer = []

        for i in range(len(array) - 1, -1, -1):
            for n in array[i]:
                answer.append(n)
                if len(answer) == k:
                    return answer