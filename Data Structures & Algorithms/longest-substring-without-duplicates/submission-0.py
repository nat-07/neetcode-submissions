class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #If we start from the beginning and iterate through the string.. it will become invalid once we find a duplicate 
        #Once there is a duplicate, we shrink the string from the beginning until there no longer is a duplicate, then continue. We can do this since the substrings until the duplicated letter won't be valid anyways. 

        left = 0 # beginning
        right = 1 # end
        letters = set()
        largestSubstring = 1

        #If it is empty or one letter, return their length
        if len(s) <= 1: 
            return len(s)
        else: 
            letters.add(s[left])

        while right < len(s):
            if (s[right] in letters):
                while (s[left] != s[right]):
                    letters.remove(s[left])
                    left += 1
                left += 1 
            else: 
                letters.add(s[right])
            largestSubstring = max(largestSubstring, right - left +1)
            right += 1
        return largestSubstring
