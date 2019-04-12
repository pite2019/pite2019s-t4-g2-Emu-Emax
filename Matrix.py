from math import sqrt

class Matrix():
    def __init__(self, *args):
        self.no_of_elements = len(args)
        self.rows = int(sqrt(self.no_of_elements))
        self.elements = [[] for i in range(self.rows)]
        for i in range(self.rows):
            self.elements[i] = [j for j in args[i * self.rows: (i + 1) * self.rows]]
    
    def print_matrix(self):
        self.log("Matrix: ")
        for e in self.elements:
            print(e)

    def __add__(self, addMatrix):
        if self.rows == addMatrix.rows:
            resultMatrix = Matrix(0,0,0,0)
            for i in range(self.rows):
                for j in range(self.rows):
                    resultMatrix.elements[i][j] += self.elements[i][j] + addMatrix.elements[i][j]
            return resultMatrix
        else:
            self.log("Different rows values!")

    def log(self,message):
        print("--Log: " + message)
