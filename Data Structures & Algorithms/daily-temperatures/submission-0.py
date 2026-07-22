class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        #Worse Case: where the warmer temperature is always at the end
        #E.g [10,9,8,7,6,5,4,3,2,1,11]
        #Brute Force: loop through each temperature until you find a warmer temperature, this would be O(n^2) in a worse case

        #Another Way: Are we able to go through this one way? or Two way? 
        #We only need to know when a temperature happens to be larger, the moment we find, we can append to the array. 
        #We need a way to store in all values waiting for a larger value

        stack = []
        answer = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            #If stack is empty, add
            if not bool(stack):
                #add index
                stack.append(i)
            else:
                #j is assignd the top
                j = stack[-1]
                #while the value is larger and the stack is not empty
                while t > temperatures[j] and bool(stack):
                    answer[j] = i - j
                    stack.pop()
                    if bool(stack):
                        j = stack[-1]

            stack.append(i)
        return answer
      