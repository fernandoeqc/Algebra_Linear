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

        self.matrix[i-1][j-1] = value

    @property
    def elements(self):
        elements = []
        for row in self.matrix:
            for item in row:
                elements.append(item)
        return elements


class LinearAlgebra:
    @staticmethod
    def transpose(a):
        """
        Retorna a matriz ou vetor transposto.

        :param a: A matriz ou vetor a ser transposto.
        :return: Uma matriz ou vetor transposto.
        """
        if isinstance(a, Matrix):
            # Se 'a' for uma matriz
            transposed_elements = []
            for j in range(1, a.cols + 1):
                column = [a.get(i, j) for i in range(1, a.rows + 1)]
                transposed_elements.extend(column)
            return Matrix(a.cols, a.rows, transposed_elements)

        if isinstance(a, Vector):
            # Se 'a' for um vetor
            return Vector(a.dim, [a.get(i) for i in range(1, a.dim + 1)])
        
        raise ValueError("O parâmetro 'a' deve ser uma matriz ou um vetor.")

    @staticmethod
    def sum(a, b):
        """
        Soma duas matrizes ou dois vetores.

        :param a: A matriz ou vetor a ser somado.
        :param b: A matriz ou vetor a ser somado.
        :return: Uma matriz ou vetor resultante da soma.
        """
        if isinstance(a, Matrix) and isinstance(b, Matrix):
            # Se ambos 'a' e 'b' forem matrizes
            if a.rows != b.rows or a.cols != b.cols:
                raise ValueError("As matrizes devem ter a mesma dimensão para a soma.")
            sum_elements = [a.get(i, j) + b.get(i, j) for i in range(1, a.rows + 1) for j in range(1, a.cols + 1)]
            return Matrix(a.rows, a.cols, sum_elements)
        if isinstance(a, Vector) and isinstance(b, Vector):
            # Se ambos 'a' e 'b' forem vetores
            if a.dim != b.dim:
                raise ValueError("Os vetores devem ter a mesma dimensão para a soma.")
            sum_elements = [a.get(i) + b.get(i) for i in range(1, a.dim + 1)]
            return Vector(a.dim, sum_elements)

        raise ValueError("Os parâmetros 'a' e 'b' devem ser ambos matrizes ou ambos vetores.")

    def times():
        pass

    def dot():
        pass

    def gauss():
        pass

    def solve():
        pass
