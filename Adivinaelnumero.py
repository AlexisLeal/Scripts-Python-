import random


numero=random.randrange(1,100)
#print(numero)
conteo=0

while(True):
    x = int(input("Ingrese el numero a divinar:\n"))
    #conteo=0

    if(x==numero):
      conteo +=1
      print("Felicidades el numero {} es le correcto con un total de {} intentos".format(x,conteo))
      print("Adios")
      break

    elif(x>numero):
      print("Es un numero menor \nSigue intentando")
      conteo += 1

    elif(x<numero):
      print("Es un numero mayor \nSigue intentando")
      conteo += 1
