from display import *
from draw import *


#tests
print 'Testing matrix creation'
color = [ 0, 255, 0 ]
matrix = new_matrix()
print_matrix(matrix)

print '---------------------------\nTesting identity'

ident(matrix)
print_matrix(matrix)

print '---------------------------\nTesting scalar mult'

matrix1 = new_matrix()
ident(matrix1)
scalar_mult(matrix1, 2)
print_matrix(matrix1)

print '---------------------------\nTesting matrix mult'

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


#draw
screen = new_screen()

matrix1 = []
matrix2 = []
matrix3 = []
matrix4 = []
matrix5 = []
matrix6 = []

for i in range(101):
    add_edge(matrix1, i*5, 500-i*5, 0, 500-i*5, 0, 0)
for i in range(101):
    add_edge(matrix2, 0, i*5, 0, 500-i*5, 500-i*5, 0)
for i in range(101):
    add_edge(matrix3, 500-i*5, 500-i*5, 0, 500, i*5, 0,)
for i in range(101):
    add_edge(matrix4, i*5, 500-i*5, 0, 500-i*5, 500, 0)


for i in range(251):
    color = [250-i, 250-i, 250-i]
    add_edge(matrix6, 0, 0, 0, 500, 500-i, 0)
    add_edge(matrix6, 500, 0, 0, 0+i, 500, 0)
    add_edge(matrix6, 500, 500, 0, 0, 0+i, 0)
    add_edge(matrix6, 0, 500, 0, 500-i, 0, 0)
    draw_lines( matrix6, screen, color)
    matrix6 = []
    
for i in range(251):
    color = [i, i/10, i/10]
    add_edge(matrix5, 0, 0, 0, 500, 250-i, 0)
    add_edge(matrix5, 500, 0, 0, 250+i, 500, 0)
    add_edge(matrix5, 500, 500, 0, 0, 250+i, 0)
    add_edge(matrix5, 0, 500, 0, 250-i, 0, 0)
    draw_lines( matrix5, screen, color) 
    matrix5 = []
    
color = [150, 100, 150]    
draw_lines( matrix1, screen, color) 
color = [150, 100, 100]    
draw_lines( matrix4, screen, color) 

color = [50, 0, 200]    
draw_lines( matrix2, screen, color)
color = [0, 0, 150]    
draw_lines( matrix3, screen, color) 


display(screen)
