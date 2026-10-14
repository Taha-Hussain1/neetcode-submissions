class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        storage = defaultdict(list)
        for i in range(len(strs)):
            newarr = [0] * 26
            for j in range(len(strs[i])):
                newarr[ord(strs[i][j]) - ord('a')] = newarr[ord(strs[i][j]) - ord('a')] + 1
            storage[tuple(newarr)].append(strs[i])

        for result in storage:
            print(result)
        return storage.values()
                    