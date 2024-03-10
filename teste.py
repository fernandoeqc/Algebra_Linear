import algebra

matriz2x3 = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz3x2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

expected_result = [
    [22, 28],
    [49, 64]
]

alg = algebra.LinearAlgebra

result = alg.dot(matriz2x3, matriz3x2)

print(result)