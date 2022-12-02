def push(item):
    global top, stk
    stk.append(item)
    top = len(stk)-1

def pop():
    global top, stk
    if top == None:
        print('Stack Underflow!!')
    else:
        print('Popped item is: ',stk[top])
        stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top-=1

def peek():
    global top, stk
    if len(stk) == 0:
        print('Stack Underflow!!')
    else:
        print("Top item is ", stk[top])

def display():
    global top, stk
    if top == None:
        print('Stack is Empty')
    else:
        temp = top
        while(temp != -1):
            print(stk[temp])
            temp-=1


stk = []        #An Empty Stack
top = None

while True:
    print("\nChoose Stack Operations..")
    print("1.Push \t2.Pop \t3.Peek \t4.Display \t5.Exit")
    ch = int(input("Enter Your Choice (1-5): "))
    if ch == 1:
        item = int(input("Enter Data Item: "))
        push(item)
    elif ch == 2:
        pop()
    elif ch == 3:
        peek()
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("ENTER A VALID CHOICE...")

