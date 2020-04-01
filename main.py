
a=float(input("digite el numero a: "))
b=float(input("digite el numero b: "))
c=float(input("digite el numero c: "))
if a!=0:
    d= b**b-4*a*c
    if d>0:
        x1= (-b+d**(1/2))/(2*a)
        x2= (-b-d**(1/2))/(2*a)
        print("las respuestas son", x1, "y", x2)
    elif d==0:
        x= (-b)/(2*a)
        print("x1 y x2 son iguales y corresponden a ", x)
    elif d<0:
        print("no existe solucion a la ecuacion dentro de el dominio de los numeros reales")
else:
    print("la ecuacion no es una funcion cuadratica")