from math import sqrt


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

    def __str__(self):
        return str(self.elements)
    
    def __abs__(self):
        return Vector(self.dim, [abs(value) for value in self.elements])
    
    def __add__(self, other):
        return LinearAlgebra.sum(self, other)
    
    def __sub__(self, other):
        return self + LinearAlgebra.times(-1, other)


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

    def __str__(self):
        max_elements_size = max([len(str(item)) for item in self.elements])
        content = ''
        content += ('-' * max_elements_size * self.cols) + '---' * self.cols
        content += '\n'
        for row in self.matrix:
            content += '|'
            content += ' | '.join([f'{item:<{max_elements_size}}' for item in row])
            content += '|\n'

        content += ('-' * max_elements_size * self.cols) + '---' * self.cols
        return content


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
                column = []
                for i in range(1, a.rows + 1):
                    column.append(a.get(i, j))
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
            sum_elements = [
                a.get(i, j) + b.get(i, j)
                for i in range(1, a.rows + 1)
                for j in range(1, a.cols + 1)
            ]
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
        is_scalar = isinstance(a, float) or isinstance(a, int)
        if is_scalar:
            if isinstance(b, Vector):
                c = Vector(b.dim, [0] * b.dim)
                for i in range(1, b.dim + 1):
                    c.set(i, b.get(i) * a)
                return c
            elif isinstance(b, Matrix):
                c = Matrix(b.rows, b.cols, ([0] * b.rows * b.cols))
                for i in range(1, b.rows + 1):
                    for j in range(1, b.cols + 1):
                      c.set(i, j, b.get(i, j) * a)
                return c

            raise Exception("o parâmetro 'b' precisa ser matriz ou vetor.")
        if isinstance(a, Vector):
            if not isinstance(b, Vector):
                raise Exception("o parâmetro 'b' precisa ser um vetor")
            if a.dim != b.dim:
                raise ValueError("os vetores precisam ter a mesma dimensão")

            c = Vector(b.dim, ([0] * a.dim))
            for i in range(1, b.dim + 1):
                c.set(i, a.get(i) * b.get(i))
            return c
        if isinstance(a, Matrix):
            if not isinstance(b, Matrix):
                raise Exception("o parâmetro 'b' precisa ser uma matriz")
            if a.rows != b.rows or a.cols != b.cols:
                raise ValueError("as matrizes precisam ter as mesmas dimensões")

            c = Matrix(a.rows, a.cols, ([0] * a.rows * b.cols))
            for i in range(1, a.rows + 1):
                for j in range(1, b.cols + 1):
                    c.set(i, j, a.get(i, j) * b.get(i, j))
            return c
        raise Exception("o parâmetro 'a' precisa ser uma matriz")
        
    @staticmethod
    def dot(A: Matrix, B):
        """
        Multiplica duas matrizes.
        Considerando A(m.n) e B(n.p), e C(m.p)
        
        :param a: A matriz a ser multiplicada.
        :param b: A matriz a ser multiplicada.
        :return: Uma matriz resultante da multiplicação.
        """

        if isinstance(B, Vector):
            return LinearAlgebra.dot_matrix_by_vector(A, B)

        #Confere validade da multiplicação
        if A.cols != B.rows:
            raise Exception("Não é possível multiplicar as matrizes AxB! \
                \nA quantidade de colunas em A: (", A.cols, ") é diferente da quantidade de linhas em B: (", B.rows, ")")
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
    def dot_matrix_by_vector(A: Matrix, B: Vector):
        #Confere validade da multiplicação
        if A.cols != B.dim:
            raise Exception("Não é possível multiplicar as matrizes AxB! \
                \nA quantidade de colunas em A: (" + str(A.cols) + ") é diferente da quantidade de linhas em B: (" + str(B.dim) + ")")
        C = Vector(A.rows, [0] * A.rows) # Cria um vetor nula

        # Faz o somatório
        for i in range(1, A.rows+1): #start in 1
            for j in range(1, A.cols+1): #start in 1
                summation = C.get(i) + A.get(i, j) * B.get(j)
                C.set(i, summation)
        return C

    @staticmethod
    def gauss(a):
        if not isinstance(a, Matrix):
            raise Exception("o valor de entrada deve ser uma matriz")
        
        if a.rows + 1 != a.cols:
            raise ValueError('A matriz não está no formato n linhas e n + 1 colunas')

        # Criando uma cópia da matriz para não modificar a original
        result_matrix = Matrix(a.rows, a.cols, a.elements)

        # Eliminação gaussiana
        for k in range(1, a.rows + 1):
            # Encontrando o pivô máximo na coluna k
            max_index = k
            max_val = abs(result_matrix.get(k, k))
            for i in range(k + 1, a.rows + 1):
                if abs(result_matrix.get(i, k)) > max_val:
                    max_val = abs(result_matrix.get(i, k))
                    max_index = i

            # Trocando as linhas
            for j in range(k, a.cols + 1):
                temp = result_matrix.get(k, j)
                result_matrix.set(k, j, result_matrix.get(max_index, j))
                result_matrix.set(max_index, j, temp)

            # Zerando os elementos abaixo do pivô
            for i in range(k + 1, a.rows + 1):
                factor = result_matrix.get(i, k) / result_matrix.get(k, k)
                for j in range(k, a.cols + 1):
                    result_matrix.set(i, j, result_matrix.get(i, j) - factor * result_matrix.get(k, j))

        return result_matrix

    @staticmethod
    def solve(A: Matrix):
        """
        Recebe uma matriz ampliada e retorna a resolução da equação linear quando houver

        :param A: Matriz ampliada ser resolvida
        :return: Lista de valores das incógnitas ou []
        """

        A = LinearAlgebra.gauss(A)
        n = A.rows
        solution = Matrix(A.rows, 1, A.cols * [0])
        # solution

        # Resolve a incógnita do último pivô
        solution.set(n, 1, A.get(n, n+1) / A.get(n, n))
        # print(solution)

        if A.get(n, n) == 0:
            raise ValueError("Não existe uma solução única.")

        for i in range(n-1, 0, -1):
            # print("n:{}, i:{}".format(n, i))
            if A.get(i, i) == 0:
                raise ValueError("Não existe uma solução única.")

            summation = 0
            for j in range(i+1, n+1, 1):
                summation += A.get(i, j) * solution.get(j, 1)
                # print("j:{}, ->j:{}".format(j, A.get(i, j)))

            solution.set(i, 1, ( A.get(i, n+1) - summation ) / A.get(i, i))

        return solution
    
    @staticmethod
    def norm(A: Vector):
        '''
        Calcula a norma da vetor A
        '''
        total_sum = 0
        for i in range(1, A.dim + 1):
            total_sum += A.get(i) ** 2

        return sqrt(total_sum)
        

    @staticmethod
    def unit_vector(A: Vector) -> Vector:
        '''
        Calcula o vetor unitario de A
        '''
        norm = 1 / LinearAlgebra.norm(A)
        return LinearAlgebra.times(norm, A)
