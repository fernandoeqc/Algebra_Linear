class Vector:
    def __init__(self, dim: int, elements: list):
        self.dim = dim
        self.elements = elements

    def get(self, index: int) -> int:
        return self.elements[index]

    def set(self, index: int, value):
        self.elements[index] = value

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
    pass


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
