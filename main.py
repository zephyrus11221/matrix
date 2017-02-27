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

matrix1 = []
matrix2 = []
matrix3 = []
matrix4 = []

for i in range(101):
    add_edge(matrix1, i*5, 500-i*5, 0, 500-i*5, 0, 0)
for i in range(101):
    add_edge(matrix2, 500-i*5, i*5, 0, 0, 500-i*5, 0)
for i in range(101):
    add_edge(matrix3, 500-i*5, 500-i*5, 0, 500, i*5, 0,)
for i in range(101):
    add_edge(matrix4, i*5, 500-i*5, 0, 500-i*5, 500, 0)

color = [0, 200, 150]    
draw_lines( matrix1, screen, color) 
color = [100, 0, 200]    
draw_lines( matrix2, screen, color)
color = [0, 0, 150]    
draw_lines( matrix3, screen, color) 

color = [50, 200, 0]    
draw_lines( matrix4, screen, color) 


display(screen)
