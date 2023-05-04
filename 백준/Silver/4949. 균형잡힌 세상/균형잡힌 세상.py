while True:
    stack = []
    string = input()
    if string == '.':
        break
    for i in string:
        if i == "(":
            stack.append(i)
        elif i =="[":
            stack.append(i)
        elif i == ")":
            if len(stack)!=0 and stack[-1]=="(":
                stack.pop()
                continue
            else:
                stack.append(i)
        elif i == "]":
            if len(stack)!=0 and stack[-1]=="[":
                stack.pop()
                continue
            else:
                stack.append(i)
    if len(stack)==0:
        print("yes")
    else: print("no")