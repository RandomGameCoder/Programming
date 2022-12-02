class A:
    def __init__(self,x,y,z,a,b,c):
        print(x,y,z,a,b,c)

class B(A):
    def __init(self,*args):
        super().__init__()
            
a = B(1,2,3,4,4,5)