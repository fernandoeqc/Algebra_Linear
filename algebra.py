class Vector:
    def __init__(self, dim: int, elements: list):
        self.dim = dim
        self.elements = elements

    def get(self, i: int) -> int:
        return self.elements[i - 1]

    def set(self, i, value):
        if i < 1 or i > self.dim:
            raise Exception('Esse vetor não possui o indice ' + i)
        self.elements[i - 1] = value

    def __add__(self, other):
        # verifica se é a mesma dimensão
        if self.dim != other.dim:
            raise Exception('Os objetos não são do mesmo tamanho ' +
                            str(self.dim) + ' != ' + str(other.dim))

        new_vector = Vector(self.dim, [0] * self.dim)
        for index in range(1, self.dim + 1):
            sum_vector = self.get(index) + other.get(index)
            new_vector.set(index, sum_vector)

        return new_vector

    def __str__(self):
        return str(self.elements)


class Matrix:
    def __init__(self, linha, coluna, matrizelementos):
        self.rows = linha
        self.cols = coluna
        self.matrix = []
        for i in range(linha):
            linha_da_matriz = []
            for j in range(coluna):
                elemento = matrizelementos[i * coluna + j]
                linha_da_matriz.append(elemento)

            self.matrix.append(linha_da_matriz)

    def get(self, i, j):
        return self.matrix[i - 1][j - 1]

    def set(self, i, j, value):
        if i < 1 or i > self.rows:
            raise Exception('Essa matriz não possui a linha ' + i)
        if j < 1 or j > self.cols:
            raise Exception('Essa matriz não possui a coluna ' + j)

        self.elements[(i-1) * self.rows + (j-1)] = value


class LinearAlgebra:
    def transpose():
        pass

    def sum():
        pass

    def times():
        pass

    def dot():
        pass

    def gauss():
        pass

    def solve():
        pass
