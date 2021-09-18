
def checkbalancedbrackets(a):
    stack=[]
    for i in a:
        if i in ['[','{','(']:
            stack.append(i)
        else:
            if not stack:
                print("NO")
                return
            top_element=stack.pop()
            if top_element=="[":
                if i!="]":
                    print("NO")
                    return
            if top_element=="{":
                if i!="}":
                    print("NO")
                    return
            if top_element=="(":
                if i!=")":
                    print("NO")
                    return
    if stack:
        print("NO")
        return 
    print("YES")
    return 

def test():
    inputs=int(input())
    while inputs>0:
        arr = list(input())
        checkbalancedbrackets(arr)
        inputs-=1

def main():
    test()

if __name__ == '__main__':
    main()