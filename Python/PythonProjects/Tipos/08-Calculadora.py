n1 = float(input("Ingresa el primer número "))
n2 = float(input("Ingresa el segundo número "))

suma = n1 + n2
resta = n1 - n2
mult = n1 * n2
divi = n1 / n2

mensaje = f"""
Para los números {n1} y {n2}
el resultado de la suma es {suma}.
el resultado de la resta es {resta}.
el resultado de la multiplicación es {mult}.
el resultado de la división es {divi}.
"""

print(mensaje)