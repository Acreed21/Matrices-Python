#Suma y Multiplicación de Matrices cuadradas para mirar el tiempo que dura cada operación
import numpy
from time import time
import matplotlib.pyplot as plt
promedios_Multi = [1,2,3,4,5,6,7,8,9,10]#,11,12,13,14,15,16,17,18,19,20]#Guardaremos los promedios acá
x = [1,2,3,4,5,6,7,8,9,10]
promedios_numpy = [0.0,0.0,1.889388664518597e-09,0.0,0.0,0.0,1.482108741617994e-10,0.0,0.0,0.0]
Promedio_Java = [2.426118478996792E-7,9.427386702204974E-8,2.3022488341094076E-8,7.3899549370711985E-9,9.596320106736191E-9,1.175366483428901E-8,6.272099110743644E-9,5.778830879259645E-9,5.5863127271920025E-9,5.440958291457287E-10] 
Promedios_C = [0.0,6.021e-8,8.021e-10,7.012e-10,7.05e-10,7.000e-10,7.42e-10,7.025e-10,7.2e-10,7.811e-10,]
contador=0
for z in range(10,90,10):#Aumenta el tamaño de la matriz de 10 en 10 hasta 100
    tamaño_matrices = z
    tiempo_promedio_multi=0
    matriz1=numpy.zeros((tamaño_matrices,tamaño_matrices))#Se crean las matrices
    matriz2=numpy.zeros((tamaño_matrices,tamaño_matrices))#Se crean las matrices
    for i in range(tamaño_matrices):#Llena las filas
        for j in range(tamaño_matrices):#Llenas las columnas
            matriz1[i][j]=1
            matriz2[i][j]=2
    for f in range(10):#Ejecutará 10 veces el mismo problema
        #Operación de multiplicación
        matriz_Resultados_multi = numpy.zeros((tamaño_matrices,tamaño_matrices))#guardarán los resultados
        time1_multi = time()
        for i in range(0,tamaño_matrices):
            for j in range(0,tamaño_matrices):
                for k in range(0,tamaño_matrices):
                    matriz_Resultados_multi[i,j]+=matriz1[i,k]*matriz2[k,j]
        time2_multi=time()
        tiempo_final_multi=(time2_multi-time1_multi)/(z*z*(2*z-1))
        tiempo_promedio_multi=tiempo_promedio_multi+tiempo_final_multi
    promedios_Multi[contador]=tiempo_promedio_multi/10
    contador=contador+1
    x[contador] = z
promedios_Multi[contador]=tiempo_promedio_multi/10
plt.plot(x,promedios_Multi,label='Python')
plt.plot(x,promedios_numpy,label='Python Numpy')
plt.plot(x,Promedio_Java,label='Java')
plt.plot(x,Promedios_C,label='C')
plt.ylabel("Tiempo (mls)")
plt.xlabel("Fibonacci")
plt.show()