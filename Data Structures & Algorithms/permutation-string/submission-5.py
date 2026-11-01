class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = {}
        for ch in s1:
            count1[ch] = count1.get(ch, 0) + 1
        
        for i in range(len(s2) - len(s1) + 1):
            count2 = {}
            for j in range(i, i + len(s1)):
                count2[s2[j]] = count2.get(s2[j], 0) + 1

            if count1 == count2:
                return True

        return False