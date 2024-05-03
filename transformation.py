from algebra import *


class Transformations:
    def _cartesiana_to_homogenea(self) -> Matrix:
        pass

    def _homogenea_to_cartesiana(self) -> Matrix:
        pass

    @staticmethod
    def _vector_to_matrix(vector: Vector) -> Matrix:
       return Matrix(vector.dim, 1, vector.elements)

    @staticmethod
    def translate2D(vector: Vector, dx, dy) -> Matrix:
        pass

    @staticmethod
    def translate3D(vector: Vector, dx, dy, dz) -> Matrix:
        pass

    @staticmethod
    def roration2D(vector: Vector, angle) -> Matrix:
        pass

    @staticmethod
    def rotation3DX(vector: Vector, angle) -> Matrix:
        pass

    def rotation3DY(vector: Vector, angle) -> Matrix:
        pass

    @staticmethod
    def rotation3DZ(vector: Vector, angle) -> Matrix:
        pass

    @staticmethod
    def reflection2DX(vector: Vector) -> Matrix:
        pass

    @staticmethod
    def reflection2DY(vector: Vector) -> Matrix:
        pass

    @staticmethod
    def reflection3DX(vector: Vector) -> Matrix:
        pass

    @staticmethod
    def reflection3DY(vector: Vector) -> Matrix:
        pass

    @staticmethod
    def reflection3DZ(vector: Vector) -> Matrix:
        pass

    @staticmethod
    def projection2DX(vector: Vector) -> Matrix:
        canonical_matrix = [
            1, 0,
            0, 0
        ]

        cmatrix: Matrix = Matrix(2, 2, canonical_matrix)
        vectorM = Transformations._vector_to_matrix(vector)

        result = LinearAlgebra.dot(cmatrix, vectorM)

        return result

    @staticmethod
    def projection2DY(vector: Vector) -> Matrix:
        canonical_matrix = [
            0, 0,
            0, 1
        ]

        cmatrix: Matrix = Matrix(2, 2, canonical_matrix)
        vectorM = Transformations._vector_to_matrix(vector)

        result = LinearAlgebra.dot(cmatrix, vectorM)

        return result

    @staticmethod
    def projection3DX(vector: Vector) -> Matrix:
        canonical_matrix = [
            1, 0, 0,
            0, 1, 0,
            0, 0, 0
        ]

        cmatrix: Matrix = Matrix(3, 3, canonical_matrix)
        vectorM = Transformations._vector_to_matrix(vector)

        result = LinearAlgebra.dot(cmatrix, vectorM)

        return result

    @staticmethod
    def projection3DY(vector: Vector) -> Matrix:
        canonical_matrix = [
            1, 0, 0,
            0, 0, 0,
            0, 0, 1
        ]

        cmatrix: Matrix = Matrix(3, 3, canonical_matrix)
        vectorM = Transformations._vector_to_matrix(vector)

        result = LinearAlgebra.dot(cmatrix, vectorM)

        return result

    @staticmethod
    def projection3DZ(vector: Vector) -> Matrix:
        canonical_matrix = [
            0, 0, 0,
            0, 1, 0,
            0, 0, 1
        ]

        cmatrix: Matrix = Matrix(3, 3, canonical_matrix)
        vectorM = Transformations._vector_to_matrix(vector)

        result = LinearAlgebra.dot(cmatrix, vectorM)

        return result

    @staticmethod
    def shearing(vector: Vector) -> Matrix:
        pass
