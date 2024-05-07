#ingresar dos nuneros si primer numero es mayor que el segundo, comentar "es mayor", si es igual comentar "son iguales", si el primer numero es menor a 20 comentar "para la proxima ingrese un numero mayor", caso contrario comentar "correccion"
numero_uno:int=int(input("ingrese numero uno: "))
numero_dos:int=int(input("ingrese numero dos: "))
#si primer numero es mayor que el segundo, comentar "es mayor"
if numero_uno > numero_dos:
	print("es mayor")
#si es igual comentar "son iguales"
elif numero_uno == numero_dos:
	print("son iguales")
#si el primer numero es menor a 20 comentar "para la proxima ingrese un numero mayor"
elif numero_uno < 20:
	print("para la proxima ingrese una cantidad mayor en el primer numero")
#caso contrario comentar "correccion"
else:
	print("correcion")