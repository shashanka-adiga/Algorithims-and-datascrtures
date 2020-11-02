def isBalanced(string):
    open_list = ['[','{','(']
    closed_list = [']','}',')']
    stack = []
    pos = 0
    for i in string:
        if i in open_list:
            stack.append(i)
        elif i in closed_list:
            position = closed_list.index(i)
            if len(stack)>0 and stack[len(stack)-1] == open_list[position]:
                stack.pop()
            else:
                print("unbalanced")
                exit(0)
    if len(stack) == 0:
        print("balanced")

string = "{()}[()]"
isBalanced(string)

