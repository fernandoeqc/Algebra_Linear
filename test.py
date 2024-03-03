import unittest
from algebra import Matrix, Vector


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
            1, 0, 0,
            2, 1, 0,
            3, 2, 1
        ]
        matrix = Matrix(3, 3, elements)
        self.assertEqual(matrix.get(1, 1), 1)
        self.assertEqual(matrix.get(1, 2), 0)

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
        self.assertEqual(vector.get(3), 2)

    def test_set(self):
        elements = [3, 1, 2, 3]
        vector = Vector(4, elements)
        self.assertEqual(vector.get(1), 3)
        self.assertEqual(vector.get(3), 2)
        vector.set(1, 9)
        self.assertEqual(vector.get(1), 9)
        self.assertEqual(vector.get(3), 2)


if __name__ == '__main__':
    unittest.main()
