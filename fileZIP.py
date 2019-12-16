import datetime
from zipfile import ZipFile

z_path = input("Introduce la ruta por favor ")

with ZipFile(z_path,'r') as zipf:
    
    for z in zipf.infolist():
        print("*"*40)
        print("Nombre del archivo: {}".format(z.filename))
        print("Fecha de creacion: {}".format(datetime.datetime(*z.date_time)))
        print("Tamaño comprimido: {} bytes".format(z.compress_size))
        print("Tamaño real: {} bytes".format(z.file_size))
        
        
        
zipf.close()

