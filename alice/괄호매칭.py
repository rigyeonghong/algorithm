def isParenthesisValid(st):
    if len(st) % 2 != 0: #시간 줄이기 위해서 거르기
        return False
    dict = {'(':')', '{':'}', '[':']', '<':'>'}
    stack = []
    
    for i in st:
        if i in dict.keys(): 
            stack.append(i)
        else: # 클로징일 때 if 스택빈경우 else 있는 경우
            if stack == []:
                return False
            a = stack.pop()
            if i != dict[a]:
                return False
    return stack == [] # (((( 일경우를
        
    

def main():
    examples = ["({()})", "[]<>{}", ")(" "<]", "<(>)"]
    for example in examples:
        print(example, isParenthesisValid(example))

    
if __name__ == "__main__":
    main()