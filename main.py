from transformation import *

a = Vector(2, [2,1])
b = Vector(3, [-2, 1, 3])


print(a)


proj2x = Transformations.projection2DX(a)
proj2y = Transformations.projection2DY(a)
proj3x = Transformations.projection3DX(b)
proj3y = Transformations.projection3DY(b)
proj3z = Transformations.projection3DZ(b)

print("============ 2D ============")
print(proj2x)
print(proj2y)
print("============ 3D ============")
print(proj3x)
print(proj3y)
print(proj3z)

