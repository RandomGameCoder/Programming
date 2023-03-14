class Matrix:
    def __init__(self,matrix):
        self.matrix=matrix
    def transpose(self):
        rows=len(self.matrix)
        cols=len(self.matrix[0])
        trans_mat=[]
        for n in range(cols):
            trans_mat.append([])
        for i in range(rows):
            for j in range(cols):
                trans_mat[j].append(self.matrix[i][j])
        return trans_mat
    def add(self,matrix):
        if len(self.matrix)!=len(matrix) or len(self.matrix[0])!=len(matrix[0]):
            pass
        summ=[]
        for i in range(len(self.matrix)):
            summ.append([])
            for j in range(len(self.matrix[0])):
                summ[i].append(self.matrix[i][j]+matrix[i][j])
        return summ
class Determinant:
    def __init__(self):
        pass
