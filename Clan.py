"""Clase para hacer la grafica para el problema del clan"""

class Clan(object):
	"""docstring for Clan"""
	def __init__(self, graph_dict = None):
		"""Inicializa una grafica, en caso de que no se
		reciba nada, se usara un diccionario vacio"""
		if graph_dict == None:
			self.__graph_dict = graph_dict

	"""Regresa una lista de vertices de la grafica"""
	def vertices(self):
		return list(self.__graph_dict.keys()) 

	"""Regresa las aristas de la grafica"""
	def aristas(self):
		return self.__generate_edges()

	"""Metodo estatico que permite generar aristas a la grafica"""
	def __generate_edges(self):
		arista = []
		for vertice in self.__graph_dict:
			for vecinos in self.__graph_dict[vertice]:
				if {vecinos, vertice} not in arista:
					arista.append({vertice, vecinos})
		return arista

	"""Metodo que permite agregar un vertice a nuestra grafica, en dado
	caso que un vertice no esta en la grafica, se agrega al diccionario"""
	def agregaVertice(self, vertice):
		if vertice not in self.__graph_dict:
			self.__graph_dict[vertice] = []

	"""Metodo que permite agregar una arista a nuestra grafica
	las arista se le esta considerando como un conjunto debido a que
	esta entre dos vertices"""
	def agregaArista(self, arista):
		arista = set(arista)
		(verticeU, verticeV) = tuple(arista)
		if verticeU in self.__graph_dict:
			self.__graph_dict[verticeU].append(verticeV)
		else:
			self.__graph_dict[verticeU] = [verticeV]


	def __str__(self):
		res = "Vertices: "
		for k in self.__graph_dict:
			res += str(k) + " "
		res += "\nAristas: "
		for arista in self.__generate_edges():
			res += str(arista) + " "
		return res
