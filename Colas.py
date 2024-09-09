# Estructura tipo clase para "AGREGAR" un número a la COLA
from queue import Queue

# Se crea una cola vacía
cola_de_atencion = Queue() 

# Variable de número de atención
numero_atencion= 1

# Se encola el nuevo número (elemento)
cola_de_atencion.put(numero_atencion)


# Se muestra la cola actualizada [1]
print("Su numero de atencion es el: ",cola_de_atencion.queue) 

# Proceso "ELIMINAR" el primer número de atención de la cola.
from queue import Queue
cola = Queue()

# Se agregan nuevos números de atención a la cola
cola_de_atencion.put(2)
cola_de_atencion.put(3)
cola_de_atencion.put(4)

print("Numeros de atencion en la Cola: ",cola_de_atencion.queue)

# Se elemina el primer elemento agregado a la cola ([4])
numero_finalizado = cola_de_atencion.get()

# Se muestra elemento eliminado
print("Numero de atencion eliminado: ",numero_finalizado)

# Se imprime cola actual
print("Numeros pendientes de atencion: ",cola_de_atencion.queue)


# Proceso para "VACIAR" los números de atención de la Cola
cola_de_atencion = [1,2,3,4,5] # Método o Estructura tipo "Lista"

# Se define la funsión paran el vacio de cola
def vaciar_cola(cola_de_atencion): 
    cola_de_atencion.clear() # Operador "clear" para vaciado de elementos o números en la cola.

vaciar_cola(cola_de_atencion)

print("Numeros en la cola: ",cola_de_atencion)

# Jean Paul Villalobos V. 20/11/2023

