import math as ma
from random import random as ra
from optparse import OptionParser
from sys import exit
from copy import deepcopy

###############################################
#     Program to analytically invert an       #
#                 nxn matrix                  #
#                Chris  Lucas                 #
###############################################

def determinant(matrix = [[]], it = 0, verb = False):
    
    if verb:
        print "> Determinant iteration %d" % (it+1)
        print_matrix(matrix, para = it)

    dim = len(matrix)

    if dim==2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

    det = 0

    for top_i in range(dim):
        if verb:
            print ">> Element: %d" % top_i
        
        sub_matrix = []

        # check if element is non-zero
        if matrix[0][top_i] != 0:
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
            det += suf_mult * matrix[0][top_i] * determinant(sub_matrix, it+1, verb)

    return det

def transpose(matrix = [[]]):

    dim = len(matrix)
    trans_matrix = deepcopy(matrix)

    for i in range(dim):
        for j in range(dim):
            trans_matrix[i][j] = matrix[j][i]

    return trans_matrix

def rand_int():
    return int(ma.floor(ra()*10))

def print_matrix(matrix = [[]], para = 0):
    for i in range(len(matrix)):
        line = ""
        for j in range(len(matrix[i])):
            line += str(matrix[i][j]) + " "
        print "%s%s" % ("\t"*para, line)

def main():
    
    pser = OptionParser()
    pser.add_option("-d", "--debug", dest="debug", action="store_true", default = False,
                        help="Run in debug mode, using hardcoded 3x3 matrix")
    pser.add_option("-n", "--numdim", dest="dim", default=3, type="int",
                        help="Dimension of matrix")
    pser.add_option("-v", "--verbose", dest="verb", action="store_true", default = False,
                        help="Verbose output")

    (options, args) = pser.parse_args()

    my_matrix = []
    dim = options.dim

    if dim < 2:
        exit("\n>> Error: Dimension must be >=2.\n   Exiting.\n")

    if options.debug:
        # use hardcoded matrix - need to set the correct dimension
        my_matrix = [[9,2,4], [9,9,9], [7,2,4]]
        dim = 3
        # my_matrix = [[5, 9, 8, 0, 4, 4],
        #                 [0, 7, 4, 7, 1, 4],
        #                 [4, 8, 7, 0, 5, 7],
        #                 [4, 3, 0, 2, 4, 3],
        #                 [9, 1, 1, 2, 6, 2],
        #                 [3, 1, 4, 2, 6, 0]]
        # dim = 6
    else:
        # pseudorandomly generate a matrix
        for i in range(dim):
            my_matrix.append([rand_int() for i in range(dim)])

    print "\nMatrix:"
    print_matrix(my_matrix)

    det = determinant(my_matrix, it = 0, verb = options.verb)

    print "\n> Determinant = %d\n" % det

    if det == 0:
        exit()

    trans_matrix = transpose(my_matrix)

    for i in range(dim):
        for j in range(dim):
            trans_matrix[i][j] = (1./det)*trans_matrix[i][j]

    print "> Inverted matrix:"
    print_matrix(trans_matrix)
    print ""

if __name__ == "__main__":
    main()