def perimetrocuadrado():
    lado = float(input('Ingrese el valor del lado: '))
    return print ('El perimetro del cuadrado es', lado * 4)


def perimetrorectangulo():
    base = float(input('Ingrese el valor del lado: '))
    altura = float(input('Ingrese el valor de la altura: '))
    return print ('El perimetro del rectangulo es',2 * base + 2 * altura )


def perimetrocirculo():
    radio = float(input('Ingrese el valor del radio: '))
    pi = 3.1416
    return print ('El perimetro del circulo es', 2 * pi * radio)


if __name__ == ('__main__'):
    print (__name__)
    print ('Soy el archivo principal')
    perimetrocirculo()
    perimetrocuadrado()   
    perimetrorectangulo()
    
else:
    print(('Soy una libreria'))
    print(__name__)