from sys import path 
path.append('..\\lib')
from Lib.areas import areacirculo,areacuadrado,arearectangulo
from Lib.perimetros import perimetrocirculo,perimetrocuadrado,perimetrorectangulo


def main():
    print('$' * 40)
    print('Programa para calcular Areas y Perimetros')
    print('$' * 40)

    figura = input('Ingrese nombre de la figura geometrica: ')
    
    if figura.lower() == 'cuadrado':
        areacuadrado()
        perimetrocuadrado()
    elif figura.lower() == 'circulo':
        areacirculo()
        perimetrocirculo()
   
    elif figura.lower() == 'rectangulo':
        arearectangulo()
        perimetrorectangulo()        
    else:
        print('Esa figura no puede ser calculada ')
        print(('Espere la version 2.0 '))
        
if __name__ == ('__main__'):
    main()