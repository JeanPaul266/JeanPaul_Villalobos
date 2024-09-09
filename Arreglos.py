
Notas_Julian = [65,45,40,55,35,]

print ("Las notas de Julian: ", Notas_Julian)

Sumanotas = sum(Notas_Julian)

print ("La suma de las notas: ", Sumanotas)

PromedioNotas = (Sumanotas/len(Notas_Julian))

print ("El promedio del alumno Julian es: ", PromedioNotas)

#Encuentra un elemento en el arreglo
Element = 95

if Element in Notas_Julian:

    print ("Si se encuentra el elemento ", Element,"en el ARRAY")

else:

    print ("No se encuentra", Element,"en el ARRAY")

#Insertar elemento en el ARREGLO

Notas_Julian.insert(5, 70)

print ("Arreglo despues de la insercion de un nuevo elemento ", Notas_Julian)

# Eliminacion de elemento en el arreglo

Notas_Julian.remove(65)

print ("Arreglo despues de la eliminacion de un elemento ", Notas_Julian)

# reemplazar un elemento en el arreglo

Eliminado = Notas_Julian.pop(1)

print ("Arreglo despues de la siguiente eliminacion POP: ", Eliminado)

# Elimina TODOS los elementos de un Arreglo

Notas_Julian.clear()

print("Arreglo despues de ClEAR ", Notas_Julian)

