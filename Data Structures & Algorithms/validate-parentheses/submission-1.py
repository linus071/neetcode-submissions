class Solution:
    def isValid(self, s: str) -> bool:
        #Need a HashSet to match closing with opening
        #Have an empty stack to keep track opening 
        #Run a for sign loop on s:
        # If is closing:
            # If stack is true and stack[-1] is == set[close], stack.pop()
            # else return False
        #else:
            #stack.append(sign)
        #return True if stack if not False

        closingSet = {")":"(", "]":"[", "}":"{"}
        stack = []

        for sign in s:
            if sign in closingSet:
                if stack and stack[-1] == closingSet[sign]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(sign)
        
        return True if not stack else False
