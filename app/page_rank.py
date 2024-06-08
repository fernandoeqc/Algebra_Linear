from app.algebra import Matrix, Vector, LinearAlgebra

class PageRank:
    @staticmethod
    def run(A: Matrix):
            
        tolerance = 0.0001

        a0 = PageRank.authority_vector(A)
        for i in range(1000):
            u = LinearAlgebra.dot(A, a0)

            hn = LinearAlgebra.unit_vector(u)
            A_transpose = LinearAlgebra.transpose(A)

            v = LinearAlgebra.dot(A_transpose, hn)
            an = LinearAlgebra.unit_vector(v)

            diff = abs(an - a0)

            if max(diff.elements) <= tolerance:
                result = a0
                break
            else:
                print(i, end='\r')
                a0 = an

        return result
    
    @staticmethod
    def center_vector(A: Matrix):
        '''
        Calcula o vetor centro da matriz A
        O vetor centro é a soma de todos os elementos das linhas da matriz A
        '''
        result = Vector(A.rows, [0] * A.rows)
        for i in range(1, A.rows + 1):
            total_sum = 0
            for j in range(1, A.cols + 1):
                total_sum += A.get(i, j)

            result.set(i, total_sum)
        
        return result

    @staticmethod
    def authority_vector(A):
        '''
        Calcula o vetor autoridade da matriz A
        O vetor autoridade é a soma de todos os elementos das colunas da matriz A
        '''
        result = Vector(A.cols, [0] * A.cols)
        for j in range(1, A.cols + 1):
            total_sum = 0
            for i in range(1, A.rows + 1):
                total_sum += A.get(i, j)

            result.set(j, total_sum)
        
        return result
    