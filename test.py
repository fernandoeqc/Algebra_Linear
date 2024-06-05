import unittest
from algebra import Matrix, Vector, LinearAlgebra
from transformation import Transformations
from page_rank import PageRank


class TestMatrix(unittest.TestCase):
    def test_create(self):
        elements = [
            1, 0, 0,
            2, 1, 0,
            3, 2, 1,
            4, 3, 2
        ]
        matrix = Matrix(4, 3, elements)
        self.assertEqual(matrix.rows, 4)
        self.assertEqual(matrix.cols, 3)
        self.assertSequenceEqual(matrix.elements, elements)

    def test_get(self):
        elements = [
            4, 5, 6,
            2, 1, 0,
            3, 2, 1
        ]
        matrix = Matrix(3, 3, elements)
        self.assertEqual(matrix.get(1, 1), 4)
        self.assertEqual(matrix.get(1, 2), 5)
        self.assertEqual(matrix.get(1, 3), 6)

        self.assertEqual(matrix.get(2, 1), 2)
        self.assertEqual(matrix.get(2, 2), 1)
        self.assertEqual(matrix.get(2, 3), 0)

        self.assertEqual(matrix.get(3, 1), 3)
        self.assertEqual(matrix.get(3, 2), 2)
        self.assertEqual(matrix.get(3, 3), 1)

        
        elements = [
            4, 5, 6,
            3, 2, 1
        ]
        matrix = Matrix(2, 3, elements)
        self.assertEqual(matrix.get(1, 1), 4)
        self.assertEqual(matrix.get(1, 2), 5)
        self.assertEqual(matrix.get(1, 3), 6)

        self.assertEqual(matrix.get(2, 1), 3)
        self.assertEqual(matrix.get(2, 2), 2)
        self.assertEqual(matrix.get(2, 3), 1)

    def test_set(self):
        elements = [
            1, 0, 0,
            2, 1, 0,
            3, 2, 1
        ]
        matrix = Matrix(3, 3, elements)
        self.assertEqual(matrix.get(1, 1), 1)
        matrix.set(1, 1, 2)
        self.assertEqual(matrix.get(1, 1), 2)


class TestVector(unittest.TestCase):
    def test_create(self):
        elements = [3, 1, 2, 3]
        vector = Vector(4, elements)
        self.assertEqual(vector.dim, 4)
        self.assertSequenceEqual(vector.elements, elements)

    def test_get(self):
        elements = [3, 1, 2, 3]
        vector = Vector(4, elements)
        self.assertEqual(vector.get(1), 3)
        self.assertEqual(vector.get(2), 1)
        self.assertEqual(vector.get(3), 2)
        self.assertEqual(vector.get(4), 3)

    def test_set(self):
        elements = [3, 1, 2, 3]
        vector = Vector(4, elements)
        self.assertEqual(vector.get(1), 3)
        self.assertEqual(vector.get(3), 2)
        vector.set(1, 9)
        self.assertEqual(vector.get(1), 9)
        self.assertEqual(vector.get(3), 2)


class TestLinearAlgebra(unittest.TestCase):
    def test_transpose_matrix(self):
        matrix = Matrix(2, 3, [
            3, 2, 1,
            7, 8, 9
        ])
        transpose_matrix = LinearAlgebra.transpose(matrix)
        self.assertEqual(transpose_matrix.rows, 3)
        self.assertEqual(transpose_matrix.cols, 2)
        self.assertSequenceEqual(transpose_matrix.elements, [
            3, 7,
            2, 8,
            1, 9
        ])

    def test_sum_matrix(self):
        # adição de duas matriz 2x3
        first = Matrix(2, 3, [
            1, 2, 1,
            1, 2, 1
        ])
        second = Matrix(2, 3, [
            3, 2, 1,
            7, 8, 9
        ])
        result = LinearAlgebra.sum(first, second)
        self.assertEqual(result.rows, 2)
        self.assertEqual(result.cols, 3)
        self.assertSequenceEqual(result.elements, [
            4, 4, 2,
            8, 10, 10
        ])
        
        # Adição de duas matriz 2x2
        first = Matrix(2, 2, [
            2, 2,
            1, 2,
        ])
        second = Matrix(2, 2, [
            3, 5,
            6, 3
        ])
        result = LinearAlgebra.sum(first, second)
        self.assertEqual(result.rows, 2)
        self.assertEqual(result.cols, 2)
        self.assertSequenceEqual(result.elements, [
            5, 7,
            7, 5
        ])
        # Erro de soma de matriz com tamanhos diferentes
        with self.assertRaises(ValueError):
            first = Matrix(3, 2, [
                2, 2,
                1, 2,
                2, 1
            ])
            second = Matrix(2, 2, [
                3, 5,
                6, 3
            ])
            LinearAlgebra.sum(first, second)

    def test_sum_vector(self):
        # Soma de vetor
        first = Vector(3, [
            1, 2, 1,
        ])
        second = Vector(3, [
            3, 1, 3
        ])
        result = LinearAlgebra.sum(first, second)
        self.assertEqual(result.dim, 3)
        self.assertEqual(result.elements, [4, 3, 4])
        # Erro de soma de vetor com tamanhos diferentes
        with self.assertRaises(ValueError):
            first = Vector(3, [
                1, 2, 1,
            ])
            second = Vector(2, [
                3, 1
            ])
            LinearAlgebra.sum(first, second)

    def test_sum_matrix_vector(self):
        with self.assertRaises(ValueError):
            first = Vector(3, [
                1, 2, 1,
            ])
            second = Matrix(2, 2, [
                3, 5,
                6, 3
            ])
            LinearAlgebra.sum(first, second)

        with self.assertRaises(ValueError):
            first = Matrix(2, 2, [
                3, 5,
                6, 3
            ])
            second = Vector(3, [
                1, 2, 1,
            ])
            LinearAlgebra.sum(first, second)

    def test_times_scalar_vector(self):
        # times scalar and vector
        vector = Vector(3, [1, 2, 3])
        result = LinearAlgebra.times(3, vector)
        self.assertEqual(result.dim, 3)
        self.assertEqual(result.elements, [3, 6, 9])

        vector = Vector(5, [9, 8, 7, 6, 5])
        result = LinearAlgebra.times(1, vector)
        self.assertEqual(result.dim, 5)
        self.assertEqual(result.elements, [9, 8, 7, 6, 5])

    def test_times_scalar_matrix(self):
        # times scalar and matrix
        matrix = Matrix(3, 3, [
            1, 2, 3,
            4, 5, 6,
            7, 8, 9,
        ])
        result = LinearAlgebra.times(3, matrix)
        self.assertEqual(result.rows, 3)
        self.assertEqual(result.cols, 3)
        self.assertEqual(result.elements, [
            3, 6, 9,
            12, 15, 18,
            21, 24, 27
        ])

        matrix = Matrix(2, 4, [
            1, 2, 3, 2,
            4, 5, 6, 1
        ])
        result = LinearAlgebra.times(1, matrix)
        self.assertEqual(result.rows, 2)
        self.assertEqual(result.cols, 4)
        self.assertEqual(result.elements, [
            1, 2, 3, 2,
            4, 5, 6, 1
        ])

    def test_times_matrix(self):
        # times matrix
        first = Matrix(2, 3, [
            1, 2, 3,
            4, 5, 6,
        ])
        second = Matrix(2, 3, [
            5, 3, 1,
            7, 5, 3,
        ])
        result = LinearAlgebra.times(first, second)
        self.assertEqual(result.rows, 2)
        self.assertEqual(result.cols, 3)
        self.assertEqual(result.elements, [
            5, 6, 3,
            28, 25, 18,
        ])

    def test_times_vector(self):
        # times vector
        first = Vector(3, [1, 2, 3])
        second = Vector(3, [3, 2, 1])
        result = LinearAlgebra.times(first, second)
        self.assertEqual(result.dim, 3)
        self.assertEqual(result.elements, [3, 4, 3])

        first = Vector(5, [9, 8, 7, 6, 5])
        second = Vector(5, [9, 8, 7, 6, 5])
        result = LinearAlgebra.times(first, second)
        self.assertEqual(result.dim, 5)
        self.assertEqual(result.elements, [81, 64, 49, 36, 25])

    def test_dot(self):
        first = Matrix(2, 3, [
            1, 2, 3,
            4, 5, 6
        ])
        second = Matrix(3, 2, [
            1, 2,
            3, 4,
            5, 6
        ])

        result = LinearAlgebra.dot(first, second)
        self.assertEqual(result.rows, 2)
        self.assertEqual(result.cols, 2)
        self.assertSequenceEqual(result.elements, [
            22, 28,
            49, 64
        ])

    def test_gauss(self):
        pass

    def test_solve(self):
        matrix = Matrix(2, 3, [
            1, 2, 5,
            3, -5, 4
        ])
        result = LinearAlgebra.solve(matrix)
        self.assertAlmostEqual(result.get(1, 1), 3)
        self.assertAlmostEqual(result.get(2, 1), 1)

        matrix = Matrix(2, 3, [
            2, 1, 2,
            1, 3, -4
        ])
        result = LinearAlgebra.solve(matrix)
        self.assertAlmostEqual(result.get(1, 1), 2)
        self.assertAlmostEqual(result.get(2, 1), -2)

    def test_norm(self):
        A = Vector(4, [4, 4, 4, 4])
        self.assertEqual(
            LinearAlgebra.norm(A),
            8
        )
        A = Vector(3, [4, 2, 4])
        self.assertEqual(
            LinearAlgebra.norm(A),
            6
        )


class TestTransformations(unittest.TestCase):
    def test_rotation2D(self):
        u = Vector(2, [1, 1])
        result = Transformations.rotation2D(u, 30)
        self.assertEqual(len(result.elements), 2)
        self.assertAlmostEqual(round(result.get(1, 1), 2), 0.37)
        self.assertAlmostEqual(round(result.get(2, 1), 2), 1.37)

    def test_rotation3DX(self):
        # questão 19.a do livro de algebra
        u = Vector(3, [-2, 1, 2])
        result = Transformations.rotation3DX(u, 30)
        self.assertEqual(len(result.elements), 3)
        self.assertAlmostEqual(round(result.get(1, 1), 2), -2)
        self.assertAlmostEqual(round(result.get(2, 1), 2), -0.13)
        self.assertAlmostEqual(round(result.get(3, 1), 2), 2.23)

    def test_rotation3DY(self):
        # questão 19.b do livro de algebra
        u = Vector(3, [-2, 1, 2])
        result = Transformations.rotation3DY(u, 45)
        self.assertEqual(len(result.elements), 3)
        self.assertAlmostEqual(round(result.get(1, 1), 2), 0)
        self.assertAlmostEqual(round(result.get(2, 1), 2), 1)
        self.assertAlmostEqual(round(result.get(3, 1), 2), 2.83)

    def test_rotation3DZ(self):
        # questão 19.b do livro de algebra
        u = Vector(3, [-2, 1, 2])
        result = Transformations.rotation3DZ(u, 90)
        self.assertEqual(len(result.elements), 3)
        self.assertAlmostEqual(round(result.get(1, 1), 2), -1)
        self.assertAlmostEqual(round(result.get(2, 1), 2), -2)
        self.assertAlmostEqual(round(result.get(3, 1), 2), 2)

    def test_reflection2DX(self):
        e1 = Vector(2, [1, 0])
        self.assertSequenceEqual(Transformations.reflection2DX(e1).elements, [
            1, 0
        ])
        e2 = Vector(2, [0, 1])
        self.assertSequenceEqual(Transformations.reflection2DX(e2).elements, [
            0, -1
        ])

    def test_reflection2DY(self):
        e1 = Vector(2, [1, 0])
        self.assertSequenceEqual(Transformations.reflection2DY(e1).elements, [
            -1, 0
        ])
        e2 = Vector(2, [0, 1])
        self.assertSequenceEqual(Transformations.reflection2DY(e2).elements, [
            0, 1
        ])

    def test_reflection3DZ(self):
        # questão 15.a do livro de algebra
        u = Vector(3, [2, -5, 3])
        result = Transformations.reflection3DZ(u)
        self.assertEqual(len(result.elements), 3)
        self.assertSequenceEqual(result.elements, [
            2, -5, -3
        ])

    def test_reflection3DY(self):
        # questão 15.b do livro de algebra
        u = Vector(3, [2, -5, 3])
        result = Transformations.reflection3DY(u)
        self.assertEqual(len(result.elements), 3)
        self.assertSequenceEqual(result.elements, [
            2, 5, 3
        ])

    def test_reflection3DZ(self):
        # questão 15.c do livro de algebra
        u = Vector(3, [2, -5, 3])
        result = Transformations.reflection3DX(u)
        self.assertEqual(len(result.elements), 3)
        self.assertSequenceEqual(result.elements, [
            -2, -5, 3
        ])

    def test_projection3DX(self):
        # questão 17.c do livro de algebra
        u = Vector(3, [-2, 1, 3])
        result = Transformations.projection3DX(u)
        self.assertEqual(len(result.elements), 3)
        self.assertSequenceEqual(result.elements, [
            0, 1, 3
        ])

    def test_projection3DY(self):
        # questão 17.b do livro de algebra
        u = Vector(3, [-2, 1, 3])
        result = Transformations.projection3DY(u)
        self.assertEqual(len(result.elements), 3)
        self.assertSequenceEqual(result.elements, [
            -2, 0, 3
        ])

    def test_projection3DZ(self):
        # questão 17.a do livro de algebra
        u = Vector(3, [-2, 1, 3])
        result = Transformations.projection3DZ(u)
        self.assertEqual(len(result.elements), 3)
        self.assertSequenceEqual(result.elements, [
            -2, 1, 0
        ])


class TestPageRank(unittest.TestCase):
    def test_center_vector(self):
        A = Matrix(4, 4, [
            0, 0, 1, 1,
            1, 0, 0, 0,
            1, 0, 0, 1,
            1, 1, 1, 0
        ])
        result = PageRank.center_vector(A)
        self.assertEqual(result.elements, [
            2, 1, 2, 3
        ])

if __name__ == '__main__':
    unittest.main()
