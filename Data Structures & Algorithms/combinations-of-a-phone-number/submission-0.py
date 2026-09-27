class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        map_digits = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno",
        7: "pqrs", 8: "tuv", 9: "wxyz"}
        n = len(digits)
        res = []
        def bkt(level, path):
            if level == n:
                res.append(path)
                return
            current_digit = int(digits[level])
            d = map_digits[current_digit]
            for i in range(len(d)):
                bkt(level + 1, path + d[i])
        bkt(0, "")
        return res
                
