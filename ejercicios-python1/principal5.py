"""
    @dani117m
    Manejo de estructuras
"""
# lista normal la misma puede ser modificada
diccionario = {"nombre": "René", "apellidos": "Elizalde"}
diccionario2 = {"nombre": "Luis", "apellidos": "Alvarez"}

lista = [diccionario, diccionario2] 

print("Imprimir diccionario")
for l in lista:
	# mi diccionario siver para guarda los valores 
	midiccionario = l
	# \ es para limitar el codigo para no pasarse de los 80 caracteres 
	print("Mi nombre es: %s y mi apellido es: %s " % \
    	(midiccionario["nombre"], midiccionario["apellidos"])
    	) 
"""
nota cuidado con la identacion si hay un error se debe volver a la linea anterior 
y enter para que se corriga el error
"""    	


