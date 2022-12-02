def EnQ(item):
    global f, r, qu
    qu.append(item)
    if len(qu) == 1:
        f = r = 0
    else:
        r = len(qu) - 1

def DeQ():
    global f, r, qu
    if len(qu) == 0:
        print("Queue Underflow !!")
    else:
        print("Deleted item is: ",qu[0])
        qu.pop(0)
    if len(qu) == 0:
        f = r = None

def peek():
    global f, qu
    if len(qu) == 0:
        print('Queue is Empty..')
    else:
        print("Front item is: ",qu[0])

def display():
    global f, r, qu
    if len(qu) == 0:
        print('Queue is Empty..')
    else:
       for i in qu:
            print(i)            

# Main Program

qu = []
f = r = None

while True:
    print("\nChoose Queue Operations..")
    print("1.Enqueue \t2.Dequeue \t3.Peek \t4.Display \t5.Exit")
    ch = int(input("Enter Your Choice (1-5): "))
    if ch == 1:
        item = int(input("Enter Data Item: "))
        EnQ(item)
    elif ch == 2:
        DeQ()
    elif ch == 3:
        peek()
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("ENTER A VALID CHOICE...")
