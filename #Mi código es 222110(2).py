#Mi código es 222110(2)
#N = 2 + 3

N = 5
suma = 0
promedio = int
total = float

for i in range(N):
    Valor = float(input("Ingrese un número: "))
    suma += Valor
    
promedio = suma/N
total  = promedio

while total >1:
    
    if total%2 == 0:
        total = total/2    
    else:
        total = (total*3)+1
    print(round(total,2))
        
        