class Vector:
    def __init__(self, dim: int, elements: list):
        self.dim = dim
        self.elements = elements

    def get(self, index: int) -> int:
        return self.elements[index - 1]

    def set(self, index, value):
        if index < 1 or index > self.dim:
            raise Exception('Esse vetor não possui o indice ' + index)
        self.elements[index - 1] = value

    def __add__(self, other):
        # verifica se é a mesma dimensão
        if self.dim != other.dim:
            raise Exception('Os objetos não são do mesmo tamanho ' +
                            str(self.dim) + ' != ' + str(other.dim))

        new_vector = Vector(self.dim, [0] * self.dim)
        for index in range(self.dim):
            sum_vector = self.get(index) + other.get(index)
            new_vector.set(index, sum_vector)

        return new_vector

    def __str__(self):
        return str(self.elements)


class Matriz:
    def __init__(self, linha, coluna, matrizelementos):
        self.rows = linha
        self.cols = coluna
        self.elements = matrizelementos

    def get(self, i, j):
        return self.elements[(i-1) * self.rows + (j-1)]

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
