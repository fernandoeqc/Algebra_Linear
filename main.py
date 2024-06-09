from app.algebra import Matrix
from app.page_rank import PageRank


matrix_5 = Matrix(4, 4, [
    0, 0, 1, 0, # 1
    1, 0, 0, 0, # 2
    1, 1, 0, 0, # 3
    0, 1, 0, 0, # 4
])

print(matrix_5)
print('Result')
print(PageRank.run(matrix_5))

matrix_6 = Matrix(4, 4, [
    0, 1, 1, 0, # 1
    0, 0, 1, 0, # 2
    1, 0, 0, 1, # 3
    1, 0, 0, 0, # 4
])
print(matrix_6)
print('Result')
print(PageRank.run(matrix_6))

matrix_7 = Matrix(5, 5, [
    0, 1, 1, 1, 0, # 1
    1, 0, 0, 0, 1, # 2
    0, 0, 0, 0, 1, # 3
    0, 1, 0, 0, 0, # 4
    0, 1, 1, 0, 0, # 5
])
print(matrix_7)
print('Result')
print(PageRank.run(matrix_7))

matrix_8 = Matrix(10, 10, [
    0, 1, 1, 0, 1, 1, 0, 0, 0, 1, # 1
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, # 2
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1, # 3
    0, 1, 1, 0, 0, 1, 1, 0, 0, 1, # 4
    0, 0, 0, 1, 0, 0, 0, 0, 0, 0, # 5
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, # 6
    0, 0, 0, 0, 0, 0, 0, 0, 1, 0, # 7
    0, 0, 0, 0, 0, 1, 0, 0, 0, 0, # 8
    0, 1, 1, 0, 0, 1, 0, 1, 0, 1, # 9
    0, 0, 0, 0, 0, 1, 0, 0, 0, 0, # 10
])
print(matrix_8)
print('Result')
print(PageRank.run(matrix_8))


