import math


def print_matrix( matrix ):
    for p in matrix:
        for i in p:
            print i
        print '\n'

def ident( matrix ):
    pass

def scalar_mult( matrix, s ):
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    hold = []
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
