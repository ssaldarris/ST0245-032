import matplotlib.pyplot as plt
import timeit
##LAB1
##Puerto Antioquia
def cadenaDNA(x, y):
    if(len(x) == 0) or (len(y) == 0):
        return 0
    elif (x[0] == y[0]):
        return 1 + cadenaDNA(x[1:], y[1:])
    else:
        return max(cadenaDNA(x[1:],y), cadenaDNA(x,y[1:]))
    print (cadenaDNA)

def cuadrados(n):
        if(n <= 2):
            return n
        else:
            return cuadrados(n-1) + cuadrados(n-2)
        
x = []
tiempos = []
for f in range (1,50):
        x.append(f)
        st = timeit.default_timer()
        cuadrados(f)
        tiempos.append((timeit.default_timer()-st)*1000)

plt.plot(x,tiempos,'ro')
plt.axis([0,50,0,10000])
plt.ylabel('tiempo en milisegundos')
plt.xlabel('largo del arreglo')
plt.show()

print(tiempos[0])