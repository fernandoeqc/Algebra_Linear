from algebra import Matrix, Vector, LinearAlgebra
from transformation import Transformations

class PageRank:
    @staticmethod
    def run(self, A: Matrix):
        
        center_v = self.center_vector(A)
        authority_v = self.authority_vector(A)
        while True:
            #para melhorar essa implementacao, talvez eu tenha que mexer no metodo dot depois
            authority_v_matrix = Transformations._vector_to_matrix(authority_v)
            u = LinearAlgebra.dot(A, authority_v_matrix)
            u_norm = LinearAlgebra.norm(u)
            center_v = LinearAlgebra.unit_vector(u, u_norm)
            A_transpose = LinearAlgebra.transpose(A)
            center_v_matrix = Transformations._vector_to_matrix(center_v)
            v = LinearAlgebra.dot(A_transpose, center_v_matrix)
            v_norm = LinearAlgebra.norm(v)
            authority_v = LinearAlgebra.unit_vector(v, v_norm)
        
        #TODO: construir condição de parada
        
        #TODO: construir forma de organizar o vetor autoridade (sorted_authority_vector)
                
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
        result = Vector(A.cols, [0] * A.cols)
        for j in range(1, A.cols + 1):
            total_sum = 0
            for i in range(1, A.rows + 1):
                total_sum += A.get(i, j)

            result.set(j, total_sum)
        
        return result
    
    
