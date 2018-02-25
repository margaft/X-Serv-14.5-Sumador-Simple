#!/usr/bin/python3

import sys

def calcular(num1, num2, op):

	try:
		num1 = float(num1)
		num2 = float(num2)
		if op == "suma":
			print("La suma es: ", num1 + num2)
			return num1 + num2
		elif op == "resta":
			print("La resta es: ", num1 - num2)
			return num1 - num2
		elif op == "mult":
			print("La multiplicación es: ", num1 * num2)
			return num1 * num2
		elif op == "div":
			if num2 == 0:
				print("Error: No se puede dividir entre 0")
				return "No se puede dividir entre 0"
			else:		
				print("La división es: ", num1 / num2)
				return num1 / num2
		else:
			print("La operación debe ser: suma, resta, mult o div, ", op, "es inválido")
			return "La op debe ser: suma, resta, mult o div"
	
	except ValueError:
		print("Los dos valores introducidos deben ser de tipo FLOAT")

if __name__ == "__main__":
	if len(sys.argv) != 4:
		sys.exit("Error número de argumentos: Introduce una operación (suma, resta, multiplicación o división) número1 número2")
	else:
		op = sys.argv[1]
		num1 = sys.argv[2]
		num2 = sys.argv[3]
		print("El resultado es: ", calcular(num1, num2, op))
