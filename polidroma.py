#Verificar si una palabra es polidroma o no 

cadena=input("Introduce la cadena por favor\n")
cadenarev=cadena[::-1]


if cadena.upper() == cadenarev.upper():
  print("Las cadenas son polidromas")

else:
  print("Las cadenas no son polidromas")
