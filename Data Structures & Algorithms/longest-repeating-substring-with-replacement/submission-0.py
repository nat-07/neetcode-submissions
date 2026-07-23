class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #"XYYXYYYX"
        #"XYYXBBXXY"

        #The largest frequency of a letter replaces the others
        #If the frequency of the "other letters" exceeds the k replacement, 
        #string is no longer Valid, move until  "other letters" 
        if len(s) == 1: 
            return 1
        
        letterFreqs = defaultdict(int)
        longestSubString = 1
        left = 0 
        right = 1
        letterFreqs[s[left]] = 1
        highestLetterFreq = s[left]

        while right < len(s):
            letterFreqs[s[right]] += 1
            highestLetterFreq = max(letterFreqs, key=letterFreqs.get)
            while (sum(letterFreqs.values()) - letterFreqs[highestLetterFreq] > k):
                letterFreqs[s[left]] -= 1
                left += 1
                highestLetterFreq = max(letterFreqs, key=letterFreqs.get)
            longestSubString = max(longestSubString, right - left + 1)
            right += 1
        return longestSubString
