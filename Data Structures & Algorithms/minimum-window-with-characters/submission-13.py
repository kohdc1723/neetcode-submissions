class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        sMap = {}
        
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1

        have = 0
        need = len(tMap)
        res = [-1, -1]
        resLen = len(s) + 1
        l = 0

        for r in range(len(s)):
            c = s[r]
            sMap[c] = sMap.get(c, 0) + 1

            if c in tMap and sMap[c] == tMap[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        if resLen == len(s) + 1:
            return ""
        
        return s[l : r + 1]

