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

    def dot(A, B):
        ''' Considerando A(m.n) e B(n.p), e C(m.p)'''

        #Confere validade da multiplicação
        An, Bn = len(A[0]), len(B)
        if An != Bn:
            print("Não é possível multiplicar as matrizes AxB! \
                \nA quantidade de colunas em A: (", An, ") é diferente da quantidade de linhas em B: (", Bn, ")")
            return []

        lines, columns = len(A), len(B[0]) # Matriz de tamanho: m.p

        C = Matriz(lines, columns, [[0]*lines for i in range(columns)]) # Cria uma matriz nula

        # Faz o somatório
        for i in range(lines):
            for k in range(columns):
                for j in range(An):
                    summation = C.get(i, k) + A.get(i, j) * B.get(j, k)
                    C.set(i, k, summation)
        return C

    def gauss():
        pass

    def solve():
        pass
