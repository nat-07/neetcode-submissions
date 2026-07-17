class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        i = 0 
        j = len(s) - 1
        while i < j: 
            while s[i] not in valid: 
                i +=1
                if i == len(s):
                    return True
            while s[j] not in valid: 
                j -=1

            if s[i].lower()!= s[j].lower():
                return False
            i += 1
            j -= 1
        return True
