import math
from app.algebra import *


class Transformations:
    def _cartesiana_to_homogenea(matrix: Matrix) -> Matrix:
        return Matrix(matrix.rows + 1, matrix.cols, matrix.elements + [1])

    @staticmethod
    def _homogenea_to_cartesiana(matrix: Matrix) -> Matrix:
        return Matrix(matrix.rows - 1, matrix.cols, matrix.elements[0:-1])

    @staticmethod
    def _vector_to_matrix(vector: Vector) -> Matrix:
        return Matrix(vector.dim, 1, vector.elements)

    @staticmethod
    def translate2D(vector: Vector, dx, dy) -> Matrix:
        translationMatrix2d = Matrix(3, 3, [
            1, 0, dx,
            0, 1, dy,
            0, 0, 1,
        ])
        matrix = Transformations._vector_to_matrix(vector)
        homoMatrix = Transformations._cartesiana_to_homogenea(matrix)
        result = LinearAlgebra.dot(translationMatrix2d, homoMatrix)
        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def translate3D(vector: Vector, dx, dy, dz) -> Matrix:
        translationMatrix3d = Matrix(4, 4, [
            1, 0, 0, dx,
            0, 1, 0, dy,
            0, 0, 1, dz,
            0, 0, 0, 1
        ])
        matrix = Transformations._vector_to_matrix(vector)
        homoMatrix = Transformations._cartesiana_to_homogenea(matrix)
        result = LinearAlgebra.dot(translationMatrix3d, homoMatrix)
        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def rotation2D(vector: Vector, angle) -> Matrix:
        angle = math.radians(angle)
        rotation_matrix = Matrix(3, 3, [
            math.cos(angle), -math.sin(angle), 0,
            math.sin(angle), math.cos(angle), 0,
            0, 0, 1
        ])
        vectorM = Matrix(vector.dim + 1, 1, vector.elements + [1])
        result = LinearAlgebra.dot(rotation_matrix, vectorM)
        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def rotation3DX(vector: Vector, angle) -> Matrix:
        angle = math.radians(angle)
        rotation_matrix = Matrix(4, 4, [
            1, 0, 0, 0,
            0, math.cos(angle), -math.sin(angle), 0,
            0, math.sin(angle), math.cos(angle), 0,
            0, 0, 0, 1
        ])
        vectorM = Matrix(vector.dim + 1, 1, vector.elements + [1])
        result = LinearAlgebra.dot(rotation_matrix, vectorM)
        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def rotation3DY(vector: Vector, angle) -> Matrix:
        angle = math.radians(angle)
        rotation_matrix = Matrix(4, 4, [
            math.cos(angle), 0, math.sin(angle), 0,
            0, 1, 0, 0,
            -math.sin(angle), 0, math.cos(angle), 0,
            0, 0, 0, 1
        ])
        vectorM = Matrix(vector.dim + 1, 1, vector.elements + [1])
        result = LinearAlgebra.dot(rotation_matrix, vectorM)
        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def rotation3DZ(vector: Vector, angle) -> Matrix:
        angle = math.radians(angle)
        rotation_matrix = Matrix(4, 4, [
            math.cos(angle), -math.sin(angle), 0, 0,
            math.sin(angle), math.cos(angle), 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ])
        vectorM = Matrix(vector.dim + 1, 1, vector.elements + [1])
        result = LinearAlgebra.dot(rotation_matrix, vectorM)
        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def reflection2DX(vector: Vector) -> Matrix:
        reflection_matrix = Matrix(3, 3, [
            1, 0, 0,
            0, -1, 0,
            0, 0, 1
        ])
        vectorM = Matrix(vector.dim + 1, 1, vector.elements + [1])
        result = LinearAlgebra.dot(reflection_matrix, vectorM)
        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def reflection2DY(vector: Vector) -> Matrix:
        reflection_matrix = Matrix(3, 3, [
            -1, 0, 0,
            0, 1, 0,
            0, 0, 1
        ])
        vectorM = Matrix(vector.dim + 1, 1, vector.elements + [1])
        result = LinearAlgebra.dot(reflection_matrix, vectorM)
        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def reflection3DX(vector: Vector) -> Matrix:
        reflection_matrix = Matrix(4, 4, [
            -1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ])
        vectorM = Matrix(4, 1, vector.elements + [1])
        result = LinearAlgebra.dot(reflection_matrix, vectorM)
        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def reflection3DY(vector: Vector) -> Matrix:
        reflection_matrix = Matrix(4, 4, [
            1, 0, 0, 0,
            0, -1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ])
        vectorM = Matrix(4, 1, vector.elements + [1])
        result = LinearAlgebra.dot(reflection_matrix, vectorM)
        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def reflection3DZ(vector: Vector) -> Matrix:
        reflection_matrix = Matrix(4, 4, [
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, -1, 0,
            0, 0, 0, 1
        ])
        vectorM = Matrix(4, 1, vector.elements + [1])
        result = LinearAlgebra.dot(reflection_matrix, vectorM)
        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def projection2DX(vector: Vector) -> Matrix:
        canonical_matrix = [
            0, 0, 0,
            0, 1, 0,
            0, 0, 1
        ]

        cmatrix = Matrix(3, 3, canonical_matrix)
        vectorM = Matrix(vector.dim + 1, 1, vector.elements + [1])

        result = LinearAlgebra.dot(cmatrix, vectorM)
        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def projection2DY(vector: Vector) -> Matrix:
        canonical_matrix = [
            1, 0, 0,
            0, 0, 0,
            0, 0, 1
        ]

        cmatrix = Matrix(3, 3, canonical_matrix)
        vectorM = Matrix(vector.dim + 1, 1, vector.elements + [1])

        result = LinearAlgebra.dot(cmatrix, vectorM)

        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def projection3DX(vector: Vector) -> Matrix:
        '''Projeção ortogonal sobre o plano YZ'''
        canonical_matrix = [
            0, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ]

        cmatrix = Matrix(4, 4, canonical_matrix)
        vectorM = Matrix(vector.dim + 1, 1, vector.elements + [1])

        result = LinearAlgebra.dot(cmatrix, vectorM)

        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def projection3DY(vector: Vector) -> Matrix:
        '''Projeção ortogonal sobre o plano XZ'''
        canonical_matrix = [
            1, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ]

        cmatrix = Matrix(4, 4, canonical_matrix)
        vectorM = Matrix(vector.dim + 1, 1, vector.elements + [1])

        result = LinearAlgebra.dot(cmatrix, vectorM)

        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def projection3DZ(vector: Vector) -> Matrix:
        '''Projeção ortogonal sobre o plano XY'''
        canonical_matrix = [
            1, 0, 0, 0,
            0, 1, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 1
        ]

        cmatrix = Matrix(4, 4, canonical_matrix)
        vectorM = Matrix(vector.dim + 1, 1, vector.elements + [1])

        result = LinearAlgebra.dot(cmatrix, vectorM)

        return Transformations._homogenea_to_cartesiana(result)

    @staticmethod
    def shearing(vector: Vector, kx: float, ky: float) -> Matrix:
        shearingMatrix = Matrix(3, 3, [
            1, kx, 0,
            ky, 1, 0,
            0, 0, 1
        ])

        matrix = Transformations._vector_to_matrix(vector)
        homoMatrix = Transformations._cartesiana_to_homogenea(matrix)
        result = LinearAlgebra.dot(shearingMatrix, homoMatrix)
        return Transformations._homogenea_to_cartesiana(result)
