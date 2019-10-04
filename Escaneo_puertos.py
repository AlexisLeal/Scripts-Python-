import sys
import socket

sT = "sT"

if len(sys.argv) == 3:
    

    if sys.argv[1] == sT:
        for x in range(1,1025):
            ip_address = (sys.argv[2])
            tipo_escaneo  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#ipv4 y que sea tcp completo 
            tipo_escaneo.settimeout(20) #Tiempo de espera
            conexion = tipo_escaneo.connect_ex((ip_address,x))
            if conexion == 0:
                print(ip_address + ":", x, "Open")
            tipo_escaneo.close
            
            
