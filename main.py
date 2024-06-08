from app.algebra import Matrix, Vector, LinearAlgebra
from app.page_rank import PageRank


A = Matrix(4, 4, [
    0, 0, 1, 1,
    1, 0, 0, 0,
    1, 0, 0, 1,
    1, 1, 1, 0,
])

# A = Matrix(2, 2, [
#     1, 3,
#     2, -5
# ])

# b = Matrix(2, 1, [5, 2])

print(PageRank.run(A))
# print(LinearAlgebra.dot(A, b))

