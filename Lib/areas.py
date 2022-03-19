def areacuadrado():
    lado = float(input('Ingrese el valor del lado: '))
    return print ('El area del cuadrado es', lado**2)


def arearectangulo():
    base = float(input('Ingrese el valor del lado: '))
    altura = float(input('Ingrese el valor de la altura: '))
    return print ('El area del rectangulo es',base * altura )


def areacirculo():
    radio = float(input('Ingrese el valor del radio: '))
    pi = 3.1416
    return print ('El area del circulo es', 2 * pi * radio)


if __name__ == ('__main__'):
    print (__name__)
    print ('Soy el archivo principal')
    areacirculo()
    areacuadrado()
    arearectangulo()
    
else:
    print(('Soy una libreria'))
    print(__name__)