class DimensionError(Exception):
    def __init__(self, val):
        self.value = val
    
    def __str__(self):
        return(repr(self.value))

class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
    
    def __add__(self, other):
        if (self.m != other.m) or (self.n != other.n):
            raise DimensionError("Addition on matrices with different dimensions is not possible.")
        else:
            pass

if __name__ == "__main__": 
    A = Matrix(2, 2)
    B = Matrix(2, 2)

    A+B