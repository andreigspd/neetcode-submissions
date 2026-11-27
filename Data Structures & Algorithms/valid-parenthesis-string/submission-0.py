class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_open = []
        stack_star = []
        for i in range(len(s)):
            if s[i] is "(":
                stack_open.append(i)
            elif s[i] is ")":
                if stack_open:
                    stack_open.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
            else:
                stack_star.append(i)
        while stack_open and stack_star:
            if stack_open[-1] > stack_star[-1]:
                return False
            stack_open.pop()
            stack_star.pop()
        return stack_open == []