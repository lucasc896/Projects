import math as ma
from random import random as ra
from sys import argv

#################################################
#     Program to analytically invert an         #
#                   nxn matrix                  #
#                  Chris  Lucas                 #
#################################################

def determinant(matrix = [[]], it = 0):
    
    dim = len(matrix)

    if dim==2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

    det = 0

    for top_i in range(dim):
        
        sub_matrix = []

        # check if element is zero
        if matrix[0][top_i] == 0:
            return 0

        # loop over original matrix, ignoring first row
        # row
        for i in range(1,dim):
            this_row = []
            # column
            for j in range(dim):
                # skip the column being tested
                if j==top_i:
                    continue
                if len(this_row)<dim:
                    this_row.append(matrix[i][j])
            sub_matrix.append(this_row)

        # get pos/neg factor
        if(top_i%2 == 0):
            suf_mult = 1
        else:
            suf_mult = -1

        # sum the determinants
        det += suf_mult * matrix[0][top_i] * determinant(sub_matrix, it+1)

    return det

def rand_int():
    return int(ma.ceil(ra()*10))

def print_matrix(matrix = [[]], para = 0):
    for i in range(len(matrix)):
        line = ""
        for j in range(len(matrix[i])):
            line += str(matrix[i][j]) + " "
        print "%s%s" % ("\t"*para, line)

def main():
    
    if len(argv) < 2:
        print "> No dimension specified. Default, n=3."
        dim = 3
    else:
        dim = int(argv[1])

    my_matrix = []
    for i in range(dim):
        my_matrix.append([rand_int() for i in range(dim)])

    print ""
    print_matrix(my_matrix)

    print "\nDeterminant = %d" % determinant(my_matrix, it = 0)

if __name__ == "__main__":
    main()