from algebra import Matrix, Vector

class PageRank:
    @staticmethod
    def run(A):
        '''
        Faz o calculo do page rank
        '''
        pass

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
        pass
