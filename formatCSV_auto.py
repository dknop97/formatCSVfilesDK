import os
import time

def MyHandler(notEdited):	
	while notEdited:
		cont = 0
		print("Procurando arquivos para editar...\n")
		try:
			for filename in os.listdir(origin_folder):
				cont += 1
				print(filename)
				if ".txt" in filename.lower():
					print("Encontrado o arquivo de coordenadas.\n")
					aux = False
					with open(filename, "r") as file_object:
						lines = file_object.readlines()
						if "version" in lines[0].lower():
							aux = True
						else:
							print("ATENÇÃO! O arquivo já foi alterado.")
							print("\n>>> Feche a janela para encerrar.\n\n")
							return
					if aux:
						notEdited = False
						with open(filename, "w") as file_object:
							lista = []
							lista = lines[5:-3]
							num = 1
							for item in lista:
								xy = item[9:33]
								z = item[51:56]
								coordenadas = str(num) + xy + z + "\n"
								file_object.write(coordenadas)
								#print(coordenadas, end="")
								num = num + 1
						print("\n >>>>Arquivo editado com sucesso!! Feche a janela para encerrar.\n\n")
						return
					else:
						notEdited = True
				else:
					print("HEY! This file isn't the file with the track data.\n-----------------------------------")
					if cont == len(os.listdir(origin_folder)):
						print("Todos os arquivos já foram avaliados\n")
						return
					continue
		except Exception as error:
			print("Error trying to open the directory => ", error)
			return

origin_folder = os.path.abspath(os.path.dirname(__file__))

notEdited = True
event_Handler = MyHandler(notEdited)
