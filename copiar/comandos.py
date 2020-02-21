from datetime import date
from datetime import datetime
import subprocess


class Consola:    
    
    
    
    def comando(self, ruta_orig, ruta_dest, parametros):
        espacio = ' '
        datos = ['robocopy', ruta_orig, ruta_dest]

        if type(parametros) is list:
            self.depurar_parametros(parametros, datos)

        elif parametros == None:
            comando = espacio.join(datos)
            subprocess.run(comando, shell=True)       
        
    def crear_log(self, ruta):
        fecha  = datetime.now()
        fecha_format = fecha.strftime('%d-%m-%Y_%H-%M-%S')
        nombre_log = ruta + "\\" + "log_backup_" + fecha_format + ".txt" 


    def depurar_parametros(self, parametros, lista):
            
            for parametro in parametros:
                lista.append(str(parametro))