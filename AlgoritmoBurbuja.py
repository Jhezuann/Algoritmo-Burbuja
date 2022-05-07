score=[]

class Estudiantes(object):
	def __init__(self, puntos):
		self.puntos=puntos
	
	def entregarPuntos(self):
		print("Score: {}".format(self.puntos))

def burbuja(array):
	#bucle para pasadas
	for i in range(1, len(array)):
		#bucle para comparar
		for j in range(0, len(array)-i):
			if array[j+1] < array[j]:
				aux=array[j]
				array[j] = array[j+1]
				array[j+1]=aux
	return array

def crearScore():
	print("Ingrese un Score: ")
	valor=int(input("Score: "))
	score.append(valor)

def mostrarScoreOrdenado():
	print("\n")
	print("|***********************************|")
	print("|**|		Scores	         |**|")
	print("|***********************************|")
	print("")
	print("Scores: ")
	print(burbuja(score))
	print("")
	print("|***********************************|")

def salir():
	print("Salir inminente....!")
	exit()


def main():
	while True:
		print("\n")
		print("|***********************************|")
		print("|**|		Bienvenido	 |**|")
		print("|**|		   Menu	         |**|")
		print("|***********************************|")
		print("")
		print("Selecione una de las siguientes opciones: ")
		print("1.- Registrar un Score(Puntos)")
		print("2.- Aplicar Burbuja")
		print("3.- Salir")

		opcion=int(input("Opcion: "))

		if opcion==1:
			crearScore()
		elif opcion==2:
			mostrarScoreOrdenado()
		elif opcion==3:
			salir()

if __name__=='__main__':
	main();