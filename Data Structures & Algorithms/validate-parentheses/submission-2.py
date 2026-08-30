class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        for i in s:
            if i == ')' or i == '}' or i == ']':
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp == '(' and i == ')':
                    continue
                elif temp == '{' and i == '}':
                    continue
                elif temp == '[' and i == ']':
                    continue
                else:
                    return False
            else:
                stack.append(i)

        if len(stack) == 0:
            return True
        else:
            return False


        