from algebra import *


class Transformations:
    def _cartesiana_to_homogenea(self) -> Matrix:
        pass

    def _homogenea_to_cartesiana(self) -> Matrix:
        pass

    def _vector_to_matrix(vector:Vector) -> Matrix:
       return Matrix(vector.dim, 1, vector.elements)

    @classmethod
    def translate2D(self, vector:Vector, dx, dy) -> Matrix:
        pass

    @classmethod
    def translate3D(self, vector:Vector, dx, dy, dz) -> Matrix:
        pass

    @classmethod
    def roration2D(self, vector:Vector, angle) -> Matrix:
        pass

    @classmethod
    def rotation3DX(self, vector:Vector, angle) -> Matrix:
        pass

    def rotation3DY(self, vector:Vector, angle) -> Matrix:
        pass

    @classmethod
    def rotation3DZ(self, vector:Vector, angle) -> Matrix:
        pass

    @classmethod
    def reflection2DX(self, vector:Vector) -> Matrix:
        pass

    @classmethod
    def reflection2DY(self, vector:Vector) -> Matrix:
        pass

    @classmethod
    def reflection3DX(self, vector:Vector) -> Matrix:
        pass

    @classmethod
    def reflection3DY(self, vector:Vector) -> Matrix:
        pass

    @classmethod
    def reflection3DZ(self, vector:Vector) -> Matrix:
        pass

    @classmethod
    def projection2DX(self, vector:Vector) -> Matrix:
        canonical_matrix = [
            1, 0,
            0, 0
        ]

        cmatrix:Matrix = Matrix(2, 2, canonical_matrix)
        vectorM = self._vector_to_matrix(vector)

        result = LinearAlgebra.dot(cmatrix, vectorM)

        return result

    @classmethod
    def projection2DY(self, vector:Vector) -> Matrix:
        canonical_matrix = [
            0, 0,
            0, 1
        ]

        cmatrix:Matrix = Matrix(2, 2, canonical_matrix)
        vectorM = self._vector_to_matrix(vector)

        result = LinearAlgebra.dot(cmatrix, vectorM)

        return result

    @classmethod
    def projection3DX(self, vector:Vector) -> Matrix:
        canonical_matrix = [
            1, 0, 0,
            0, 1, 0,
            0, 0, 0
        ]

        cmatrix:Matrix = Matrix(3, 3, canonical_matrix)
        vectorM = self._vector_to_matrix(vector)

        result = LinearAlgebra.dot(cmatrix, vectorM)

        return result

    @classmethod
    def projection3DY(self, vector:Vector) -> Matrix:
        canonical_matrix = [
            1, 0, 0,
            0, 0, 0,
            0, 0, 1
        ]

        cmatrix:Matrix = Matrix(3, 3, canonical_matrix)
        vectorM = self._vector_to_matrix(vector)

        result = LinearAlgebra.dot(cmatrix, vectorM)

        return result

    @classmethod
    def projection3DZ(self, vector:Vector) -> Matrix:
        canonical_matrix = [
            0, 0, 0,
            0, 1, 0,
            0, 0, 1
        ]

        cmatrix:Matrix = Matrix(3, 3, canonical_matrix)
        vectorM = self._vector_to_matrix(vector)

        result = LinearAlgebra.dot(cmatrix, vectorM)

        return result

    @classmethod
    def shearing(self, vector:Vector) -> Matrix:
        pass
