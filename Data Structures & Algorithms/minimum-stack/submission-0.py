class MinStack:

    # a stack can only push and pop numbers from the top
    # the minimum number at any point of the stack will change depending on the instance of that stack (whether that be pushing and popping everything)
    # we can keep track of the minimum number by adding another stack
    def __init__(self):
        self.stack = []
        self.minimumStack = []
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if not bool(self.minimumStack):
            self.minimumStack.append(value)
        elif value <= self.minimumStack[-1]: 
            #Incase it is <= duplicates are added to the stack
            self.minimumStack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        if (self.stack[-1] == self.minimumStack[-1]):
            self.minimumStack.pop()
        self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if not bool(self.stack):
            return null
        else: 
            return self.stack[-1]
        
        
    def getMin(self):
        """
        :rtype: int
        """

        if not bool(self.minimumStack):
            return null
        else: 
            return self.minimumStack[-1]
        

