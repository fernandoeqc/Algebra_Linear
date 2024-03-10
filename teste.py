import algebra as alg

matriz2x3 = [1, 2, 3, 4, 5, 6]
matriz3x2 = [1, 2, 3, 4, 5, 6]

matriz1x5 = [3, 4, 5, 10, 20]
matriz5x1 = [12, 14, -8, 7, 0]


#DOT TEST
matA = alg.Matrix(2, 3, matriz2x3)
matB = alg.Matrix(3, 2, matriz3x2)
result = alg.LinearAlgebra.dot(matA, matB)
print(result.elements == [22, 28, 49, 64])

matA = alg.Matrix(3, 2, matriz3x2)
matB = alg.Matrix(2, 3, matriz2x3)
result = alg.LinearAlgebra.dot(matA, matB)
print(result.elements == [9, 12, 15, 19, 26, 33, 29, 40, 51])

matA = alg.Matrix(1, 5, matriz1x5)
matB = alg.Matrix(5, 1, matriz5x1)
result = alg.LinearAlgebra.dot(matA, matB)
print(result.elements == [122])
