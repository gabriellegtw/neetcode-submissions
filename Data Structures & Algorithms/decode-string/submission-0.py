class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""

        for i in range(len(s)):

            if not s[i] == "]":
                stack.append(s[i])
            else:
                # Collect the letters in the brackets
                word = ""
                while stack[-1] != "[":
                    # Not word += stack.pop()
                    word = stack.pop() + word
                # Pop out the "["
                stack.pop()

                # Multiply the current word
                digit = ""
                # Initially forgot to write the while stack
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                digit = int(digit)
                # join back to the stack
                stack.append(digit * word)

        return "".join(stack) 




                    
        