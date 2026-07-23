class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hashMap = defaultdict(int)
        #Count how many instances of s1 in a hashmap 
        for letter in s1: 
            hashMap[letter] += 1
        #Go through s2 until the first letter is found, if the next letter is not part of s1, skip to the next and restart
        tempMap = hashMap.copy()
        i = 0
        for j in range (len(s2)):
            if s2[j] in tempMap:
                if tempMap[s2[j]] != 0:
                    tempMap[s2[j]] -= 1
                    print(s2[j])
                else: 
                    #there are too many of that type
                    while s2[i] != s2[j] and i < j:
                        tempMap[s2[i]] += 1
                        i+=1
                    i+=1                  
            else:
                tempMap = hashMap.copy()
                i = j
                i+=1
            if (sum(tempMap.values()) == 0):
                return True
        return False