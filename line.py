def line():
    print("TO DO")
    A= int(input('Ingrese el coeficiente A: '))
    B= int(input('Ingrese el coeficiente B: '))
    X1= int(input('Ingrese el  coeficiente X1: '))
    X2= int(input('Ingrese el  coeficiente X2: '))
    print('El coeficiente A de su ecuación de la recta es:', A)
    print('El coeficiente B de su ecuación de la recta es:',B)
    print('El coeficiente X1 de su ecuación de la recta es:',X1)
    print('El coeficiente X2 de su ecuación de la recta es:', X2)
    print('Para la siguente ecuación:')
    print(f"\tY= {A}x + {B}")
    p1= (X1, A*X1+B)
    p2= (X2, A*X2+B)
    print('Dados los siguientes puntos:')
    print('P1', p1)
    print('P2', p2)
    distancia= ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)*0.5
    print('La distancia entre ellos es:' distancia)


