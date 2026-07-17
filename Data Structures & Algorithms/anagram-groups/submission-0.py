class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedToArray = defaultdict(list)
        for word in strs: 
            key = "".join(sorted(word))
            sortedToArray[key].append(word)
        return list(sortedToArray.values())

            