#Intento de Curva de PH, toma dois.

#ESTO ME PERMITE QUE EL USUARIO PUEDA ESTIPULAR LA CANTIDAD DE REACTIVOS
#EN LA REACCION, EVITANDO SUPONER QUE SOLO PUDEN HABER DOS REACTIVOS
#INVOLUCRADOS:
#------------------------------------------------------------------------
cant_reactivos = input("Numero de reactivos: ") #me pide la cantidad de reactivos
a_iterar = str(cant_reactivos*"x") #como no puedo iterar enteros, multiplico al numero de cant_reactivos por un literal y lo convierto en un string, que si se puede iterar. Esto en realidad lo hago porque me itera una cantidad de veces equivalente a la cantidad de caracteres dentro de la variable.

for i in a_iterar: #itero la misma cantidad de veces estipuladas por el usuario a traves de cant_reactivos
	reactivos = raw_input("Reactivo: ")
	print reactivos
#------------------------------------------------------------------------

