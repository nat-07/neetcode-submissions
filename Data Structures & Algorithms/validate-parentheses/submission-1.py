class Solution:
    def isValid(self, s: str) -> bool:
        startingBrackets = ['(', '[','{']
        endingBrackets = [')',']','}']
        stack = []
        for bracket in s: 
            if bracket in startingBrackets: 
                stack.append(bracket)
            else:
                if not bool(stack):
                    return False
                recentBracket = stack[-1]
                if ((recentBracket == '(' and bracket == ')') or (recentBracket == '[' and bracket == ']') or (recentBracket == '{' and bracket == '}')):
                    stack.pop()
                else: 
                    return False
        if not bool(stack):
            return True
        else:
            return False
     

        