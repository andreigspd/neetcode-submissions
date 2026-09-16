class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans
    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        ans = []
        while i < n:
            nr = ""
            while s[i] != "#":
                nr += s[i]
                i += 1
            nr = int(nr)
            i += 1
            curr = ""
            while nr:
                curr += s[i]
                i += 1
                nr -= 1
            ans.append(curr)
        return ans