class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        #This is where order matters again, where if a sign comes, then the first two recent expressions are dealt with 
        #Assume the input will always be a valid arithmetic
        stack = []
        for t in tokens:
            if (t == "/"):
                temp1 = stack.pop()
                temp2 = stack.pop()
                newValue = math.trunc(float(temp2) / temp1)
                stack.append(newValue)
            elif (t == "+"):
                temp1 = stack.pop()
                temp2 = stack.pop()
                newValue = temp2 + temp1
                stack.append(newValue)
            elif (t == "*"):
                temp1 = stack.pop()
                temp2 = stack.pop()
                newValue = temp2 * temp1
                stack.append(newValue)
            elif (t == "-"):
                temp1 = stack.pop()
                temp2 = stack.pop()
                newValue = temp2 - temp1
                stack.append(newValue)
            else: 
                stack.append(int(t))
        return stack[-1]

        