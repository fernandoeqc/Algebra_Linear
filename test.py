import unittest
from algebra import Matrix


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


if __name__ == '__main__':
    unittest.main()
