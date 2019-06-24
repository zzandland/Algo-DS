class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False    
                out = stack.pop()
                if c == ')' and out != '(':
                    return False
                elif c == ']' and out != '[':
                    return False
                elif c == '}' and out != '{':
                    return False
        return len(stack) == 0