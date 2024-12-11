import matplotlib.pyplot as plt
import numpy as np
N=[4, 8, 12] # Iniciamos esta lista N con estos valores
def factorial(n):
    facto = 1
    for i in range(2, n + 1):
        facto = facto*i #Factorial, se va autoconteniendo la multiplicacion y sumandose
    return facto #Retorna el valor del factorial cuando se llama a la funcion

def taylor_arcsen(x, N):
    sumatoria = 0 #Declaramos la variable sumatoria
    for n in range(N): #Recorre los valores de n a el rango N dados por el array
        coef = factorial(2*n) / (4**n * factorial(n)**2 * (2*n + 1))
        sumatoria += coef * (x**(2*n + 1))
    return sumatoria 
exacta = np.linspace(-1, 1, num=200)#Exacta Arcsen con num=200 para mejor exactitud
plt.subplots(figsize=(9, 7))#Seteamos el tamaño para nuestro grafico
plt.plot(exacta, np.arcsin(exacta),label="Exacta")#Ploteamos la exacta aqui, debido que si queda en el ciclo for, se plotearia N veces xd

for i in range(len(N)):# Ciclo for que recorre la longitud de N con la funcion len, que opera como int entonces no entra en conflicto con sintaxis range
    x_valores = np.linspace(-1, 1, N[i])#   Seteamos rango del grafico -1,1, y N para calcular el intervalo de espaciado lineal
    plt.suptitle(f"Arcsen Exacta vs Taylor con N={N}")# Seteamos un titulo a nuestro grafico
    plt.plot(x_valores, taylor_arcsen(x_valores,N[i]), label='{} N'.format(N[i]))#Ploteamos los N, mientras va recorriendo el ciclo
    plt.legend()#Desplegamos las legend para Cada N y para el arcsen exacto

N=[3, 6, 9, 12] # Ahora N toma estos nuevos valores para la pregunta 3
fig, axs= plt.subplots(2,2) #Creamos una figura el cual seran axes(subplots) de 2x2 
fig.set_size_inches(9,7) #Seteamos el tamaño de la figura 
for j in range(len(N)): #Ciclo por que recorre j a un rango de tamaño de la longitud del array N
    x_valores = np.linspace(-1, 1, N[j])#Seteamos rango del grafico, y N , lo que hace linspace es crear un vector espaciado linealmente
    fila = j // 2#Division entera cuando j=0 o 1 fila=0,0, cuando j=2,3 fila=1,1 y asi jugamos con las filas
    col = j % 2 #Resto de la division asi tenemos 0,1,0,1 para las columnas
    axs[fila, col].plot(exacta, np.arcsin(exacta),label="Exacta")#Ploteamos la arcsen exacta
    axs[fila, col].plot(x_valores, taylor_arcsen(x_valores, N[j]), label='N={}'.format(N[j]))#A la vez en el mismo ploteamos en conjunto nuestra aproximacion de Taylor
    axs[fila, col].legend() #Desplegamos la leyenda 
    axs[fila, col].set_title('Arcsen Exacto vs Taylor con N={}'.format(N[j])) #Seteamos un titulo para cada axs
plt.show()# Desplegamos cada Fig
