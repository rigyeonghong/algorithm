def is_correct(s):    
    partner = {"}":"{","]":"[",")":"("}
    
    if s[0] in partner.keys():
        return False
    else:
        stack = []
        for element in s:
            if element in partner.keys() and stack:
                if partner[element] != stack.pop():
                    return False
            else:
                stack.append(element)
                    
    return True if not stack else False

def solution(s):    
    count = 0
    
    for i in range(len(s)):
        if is_correct(s[i:] + s[:i]):
            count += 1
            
    return count