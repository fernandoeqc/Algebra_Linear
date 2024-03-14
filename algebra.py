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
            raise Exception('Essa matriz não possui a linha ' + str(i))
        if j < 1 or j > self.cols:
            raise Exception('Essa matriz não possui a coluna ' + str(j))

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

    @staticmethod
    def times(a, b):
        if isinstance(a, int):
            if isinstance(b, Vector):
                c = Vector(b.dim, ([0] * b.dim))
                for i in range(b.dim):
                    c.set(i, b.get(i) * a)
                return c
            elif isinstance(b, Matrix):
                c = Matrix(b.rows, b.cols, ([0] * b.rows * b.cols))
                for i in range(b.rows):
                    for j in range(b.cols):
                      c.set(i, j, b.get(i,j) * a)
                return c
            else:
                raise Exception("o parâmetro 'b' precisa ser matriz ou vetor.")
        if isinstance(a, Vector):
            if isinstance(b, Vector):
                if a.dim != b.dim:
                    raise ValueError("os vetores precisam ter a mesma dimensão")
                else:
                    c = Vector(b.dim, ([0] * a.dim))
                    for i in range(b.dim):
                        c.set(i, a.get(i)*b.get(i))
                    return c
            else:
                raise Exception("o parâmetro 'b' precisa ser um vetor")
        if isinstance(a, Matrix):
            if isinstance(b, Matrix):
                if a.rows != b.rows or a.cols != b.cols:
                    raise ValueError("as matrizes precisam ter as mesmas dimensões")
                else:
                    c = Matrix(a.rows, a.cols, ([0] * a.rows * b.cols))
                    for i in range(a.rows):
                        for j in range(b.rows):
                            c.set(i, j, a.get(i,j)*b.get(i,j))
                    return c
        else:
            raise Exception("o parâmetro 'b' precisa ser uma matriz")
        
    @staticmethod
    def dot(A: Matrix, B: Matrix):
        """
        Multiplica duas matrizes.
        Considerando A(m.n) e B(n.p), e C(m.p)
        
        :param a: A matriz a ser multiplicada.
        :param b: A matriz a ser multiplicada.
        :return: Uma matriz resultante da multiplicação.
        """

        #Confere validade da multiplicação
        if A.cols != B.rows:
            print("Não é possível multiplicar as matrizes AxB! \
                \nA quantidade de colunas em A: (", A.cols, ") é diferente da quantidade de linhas em B: (", B.rows, ")")
            return []
        C = Matrix(A.rows, B.cols, ([0] * A.rows *B.cols)) # Cria uma matriz nula

        # Faz o somatório
        for i in range(1, C.rows+1): #start in 1
            for k in range(1, C.cols+1): #start in 1
                for j in range(A.cols):
                    # print("A{}{} {} * B{}{} {}".format(i, j, A.get(i, j), i, j, B.get(i, j)))
                    summation = C.get(i, k) + A.get(i, j) * B.get(j, k)
                    C.set(i, k, summation)
        return C

    @staticmethod
    def gauss():
        pass

    @staticmethod
    def solve(A: Matrix):
        """
        Recebe uma matriz ampliada e retorna a resolução da equação linear quando houver

        :param A: Matriz ampliada ser resolvida
        :return: Lista de valores das incógnitas ou []
        """

        n = A.rows
        solution = A.cols * [0]

        # Resolve a incógnita do último pivô
        solution[n] = A.get(n, n+1) / A.get(n, n)
        print(solution)

        if A.get(n, n) == 0:
            print("Não existe uma solução única.")
            return []

        for i in range(n-1, 0, -1):
            # print("n:{}, i:{}".format(n, i))
            if A.get(i, i) == 0:
                print("Não existe uma solução única.")
                return []

            summation = 0
            for j in range(i+1, n+1, 1):
                summation += A.get(i, j) * solution[j]
                print("j:{}, ->j:{}".format(j, A.get(i, j)))

            solution[i] = ( A.get(i, n+1) - summation ) / A.get(i, i)

        print("\n Solution: {}".format(solution))
