import numpy as np
from math import sqrt
a=round(50*np.random.random ())
b=round(50*np.random.random ())
c=round(50*np.random.random ())
d=round(50*np.random.random ())
e=round(50*np.random.random ())
f=round(50*np.random.random ())

class Vector:
    basic=np.array ([1,1,1])
    coordinates_1=np.array ([a,b,c])
    coordinates_2 = np.array([d, e, f])
    def norm (a,b,c): #норма вектора
        norm=sqrt((a*a+b*b+c*c))
        return norm

    def scalar (coordinates): #умножение на число
        k=int(input())
        new_coordinates=k*coordinates_1
        return new_coordinates

    def e (coordinates_1,coordinates_2): #сложение векторов
        e=coordinates_1+coordinates_2
        return e

    def foo (basic,coordinates_1,coordinates2): #длина векторного произведения
        foo=np.linalg.det(np.array((np.concatenate((basic, coordinates_1, coordinates_2)))).reshape (3.3))
        return foo

    def foo_1 (a,b,c,d,e,f): #скалярное произведение
        foo_1=a*d+b*e+c*f
        return foo_1

    def angle (foo_1,a,b,c,d,e,f): #угол между векторами
        angle=((foo_1)/(sqrt(a*a+b*b+c*c)+sqrt(d*d+e*e+f*f)))
        return angle