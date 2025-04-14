import math as math
def line():
    A= float(input('Ingrese el coeficiente A: '))
    B= float(input('Ingrese el coeficiente B: '))
    x1= float(input('Ingrese el  coeficiente X1: '))
    x2= float(input('Ingrese el  coeficiente X2: '))
    print('El coeficiente A de su ecuación de la recta es:', A)
    print('El coeficiente B de su ecuación de la recta es:',B)
    print('El coeficiente X1 de su ecuación de la recta es:',x1)
    print('El coeficiente X2 de su ecuación de la recta es:', x2)
    print('Para la siguente ecuación:')
    print(f"\tY= {A}x + {B}")
    p1= (x1, A*x1+B)
    p2= (x2, A*x2+B)
    print('Dados los siguientes puntos:')
    print('P1', p1)
    print('P2', p2)
    distancia=math.dist(p1,p2)
    print('La distancia entre ellos es:', distancia)


