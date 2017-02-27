import math


def print_matrix( matrix ):
    for p in matrix:
        for i in p:
            print i,
        print 

def ident( matrix ):
    for i in range(4):
        matrix[i][i] = 1
    pass

def scalar_mult( matrix, s ):
    for p in range(len(matrix)):
        for i in range(4):
            matrix[p][i] *= s
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    hold = [0,0,0,0]
    for p in range(len(m2)):
        hold1 = m2[p]
        hold2 = []
        for i in range(4):
            for x in range(4):
                hold2.append(m1[x][i])
            m2[p][i]=point_mult(hold2, hold1[i])
    pass

def point_mult(l, p):
    otpt = 0
    for i in range(4):
        otpt += l[i]*p
    return otpt


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
