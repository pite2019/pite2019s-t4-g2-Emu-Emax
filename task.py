from Matrix import *

def run():
    matrix_1 = Matrix(4,5,6,7)
    matrix_2 = Matrix(2,2,2,1)

    matrix_1.print_matrix()
    matrix_2.print_matrix()

    matrix_3 = matrix_2 + matrix_1 
    matrix_3.print_matrix()

if __name__ == "__main__":
    run()