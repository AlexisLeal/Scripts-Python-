def main():
    numero=int(input("Introduce un numero entero por favor\n"))
    
    numprimo = isprime(numero)
    
    
    if(numprimo == True):
      print("El numero es primo")
    elif(numprimo == False):
      print("El numero no es primo")
                                   
        
def isprime(num):

  if(num == 2):#El dos es un numero primo 
    return True

  for i in range(2,num):
    if(num % i==0):
      return False

    else:
      return True



if __name__ == '__main__': #Permite que al ejecutar el scrip de python encuentre la funcion 
	main()
