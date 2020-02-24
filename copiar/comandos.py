from datetime import date
from datetime import datetime
import subprocess
from os import makedirs
import os.path as path 


class Consola:    
	
	
	
	def comando(self, ruta_orig, ruta_dest, parametros):

		"Ejecuta Comandos"

		if path.exists(ruta_dest):
			pass
			
		else:
			makedirs(ruta_dest, exist_ok=True)
			

		datos = ['robocopy', ruta_orig, ruta_dest]

		if type(parametros) is list:
			for parametro in parametros:
				if parametro == '/LOG:':
					param_log = self.crear_log(ruta_dest)
					log = parametro + param_log
					datos.append(log)
				
				else:
					
					datos.append(parametro)

			comando = self.armar_comando(datos)
			self.ejecutar_comando(comando)
			print("COPIADO")
			
		

		elif parametros == None:
		   comando = self.armar_comando(datos)
		   
		   self.ejecutar_comando(comando) 
		   print("COPIADO")
		         
		
	def crear_log(self, ruta):
		"""devuelve el nombre del log con fecha y hora 
			que fue generado"""

		fecha  = datetime.now()
		fecha_format = fecha.strftime('%d-%m-%Y_%H-%M-%S')
		nombre_log = ruta + "\\" + "log_backup_" + fecha_format + ".txt" 

		return nombre_log


	def armar_comando(self, datos):
		"""devuelve el string del comando"""

		separador = ' '
		comando = separador.join(datos)

		return comando
	
	def ejecutar_comando(self, comando):

		subprocess.run(comando, shell=True)
		