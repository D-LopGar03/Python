# En python es posible alinear texto a la izquierda, a la derecha y al centro a la hora de imprimir en pantalla

cadena1 = "VOY A CENTRAR ESTE TEXTO"
largo = len(cadena1)
ancho = largo + 10

print(cadena1.center(ancho, "_")) 
                    # Centramos la impresión en pantalla
                    # Cabe destacar que donde dice "ancho" debe de ser mayor a la longitud de la cadena principal, 
                    # es decir que si el máximo de ancho de la cadena es 4 dentro del método se deberá de poner como mínimo 5
                    # y el número siempre debe de ser un entero

# https://www.youtube.com/watch?v=QSZ1xhu_Wo4