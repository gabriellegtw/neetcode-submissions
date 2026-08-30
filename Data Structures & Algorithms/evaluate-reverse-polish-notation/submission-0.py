class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item == "+" or item == "*" or item == "-" or item == "/":
                first = int(stack.pop())
                second = int(stack.pop())
                newNum = 0
                if item == "+":
                    newNum = second + first
                elif item == "*":
                    newNum = second * first
                elif item == "-":
                    newNum = second - first
                else:
                    newNum = second / first
                
                stack.append(newNum)
            else:
                stack.append(item)

        return int(stack.pop())
        