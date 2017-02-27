from display import *
from draw import *

'''
tests
color = [ 0, 255, 0 ]
matrix = new_matrix()
print_matrix(matrix)

print '---------------------------'

ident(matrix)
print_matrix(matrix)

print '---------------------------'

matrix1 = new_matrix()
ident(matrix1)
scalar_mult(matrix1, 2)
print_matrix(matrix1)

print '---------------------------'

matrix_mult(matrix, matrix1)
print_matrix(matrix1)
for i in range(4):
    for p in range(4):
        matrix[i][p]=2
for i in range(4):
    for p in range(4):
        matrix1[i][p]=2

print_matrix(matrix)
matrix_mult(matrix, matrix1)
print_matrix(matrix1)
'''

#draw
screen = new_screen()
color = [0, 255, 0]

matrix = new_matrix(4,0)
for i in range(101):
    p = [i*5, 500-i*5, 0, 1]
    p2 = [500-i*5, i*5, 0, 1]
    matrix.append(p)
    matrix.append(p2)
print_matrix(matrix)

draw_lines( matrix, screen, color )
display(screen)
