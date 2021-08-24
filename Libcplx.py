from math import sqrt, cos, sin, pi, atan

# Adicion de vectores complejos
def cplxsum(a, b):
    real = a[0] + b[0]
    imag = a[1] + b[1]
    return (real, imag)

# Producto de vectores complejos
def cplxproduct(a, b):
    real = a[0]*b[0] - a[1]*b[1]
    imag = a[0]*b[1] + b[0]*a[1]
    return (real, imag)

# Sustracción de vectores complejos
def cplxsust(a, b):
    real = a[0] - b[0]
    imag = a[1] - b[1]
    return (real, imag)

# Módulo de vectores complejos
def cplxmod(a, b):
    real = sqrt(b*b + a*a)
    return real

# Sustracción de vectores complejos
def cplxcoc(a, b):
    real = (a[0]*b[0] + a[1]*b[1])/(b[0]*b[0] + b[1]*b[1])
    imag = (b[0]*a[1] - a[0]*b[1])/(b[0]*b[0] + b[1]*b[1])
    return (real, imag)

# Conjugado de un vector complejo
def cplxconj(a, b):
    real = a
    imag = (-1)*(b)
    return (real, imag)

# Cambio de coorfenadas de polar a cartesiana
def cplxpolaracartesiana(d, theta):
    x = d*cos(theta*(pi/180))
    y = d*sin(theta*(pi/180))
    return (x, y)

# Cambio de coorfenadas de cartesiana a polar
def cplxcartesianaapolar(x, y):
    d = sqrt((x*x)+(y*y))
    theta = atan(y/x)*(180/pi)
    return (d, theta)

def cplxfase(a, b):
    theta = atan(a/b)*(180/pi)
    return theta

if __name__ == '__main__':
    print(cplxsum((3,5), (-2.6,6.8)))  # (3 + 5i) + (-2.6 + 6.8i) = (0.4, 11.8i)
    print(cplxproduct((3,-1), (1,4)))  # (3 - i) x (1 + 4i) = (7, 11i)
    print(cplxsust((3,5), (-2.6,6.8)))  # (3 + 5i) - (-2.6 + 6.8i) = (5.6, -1.8i)
    print(cplxcoc((-2,1), (1,2))) # (-2 + i) x (1 + 2i) = (0, i)
    print(cplxmod(2, 1)) # (2 + i) -> sqrt((-2*-2) + (1*1)) = 5
    print(cplxconj(2, 3)) # (2, 3) -> (2, -3)
    print(cplxpolaracartesiana(sqrt(2), 45)) # (sqrt(2), pi/4) --> 1 + i
    print(cplxcartesianaapolar(1, 1)) # 1 + i --> (sqrt(2), pi/4)
    print(cplxfase(1, 1)) # a + i --> atan(1/1) = pi/4
