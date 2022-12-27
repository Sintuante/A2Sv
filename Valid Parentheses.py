class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup ={")":"(","}":"{","]":"["}
        for par in s:
            if par in lookup.values():
                stack.append(par)
            elif stack and lookup[par] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == [] 
