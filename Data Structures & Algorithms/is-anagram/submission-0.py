class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydic = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i not in mydic:
                mydic[i] = 1
            else:
                mydic[i] = mydic[i] + 1
        
        for i in t:
            if i not in mydic:
                return False
            else:
                mydic[i] = mydic[i] - 1

        return all(v == 0 for v in mydic.values())
