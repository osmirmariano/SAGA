#!/usr/bin/env python3
# -*- coding: utf-8 -*
from random import randint

class Individual():
	"""
	Realiza a instanciacao do individual, em que caso o alignment ou a generation nao sejam informados
	os mesmos receberao valores nulos, caso o alignment seja informado o chromossome é inicializado de
	forma randomica a fim de criar a populacao inicial
	"""
	def __init__(self, generation = 0, alignment = []):
		self.__generation = generation
		self.__chromossome = alignment
		self.__fitness = 0
		self.__expectOffspring = 0 # expected offspring (EO)
		self.__lenAlignment = 0 
		
		self.__lengthChromossome()

		if self.__lenAlignment:
			self.__randChromossome()


	"""
	Calcula o comprimento da maior sequencia do chromossome
	"""
	def __lengthChromossome(self):
		for row in self.__chromossome:
			self.__lenAlignment = max(self.__lenAlignment, len(row))

	"""
	Inicializa de forma randomica o crhomossome, adicionando gaps a direita de cada linha
	até que todos tenham o mesmo comprimento
	"""
	def __randChromossome(self):
		for row in range(0, len(self.__chromossome)):
			while len(self.__chromossome[row]) < self.__lenAlignment:
				i = randint(0, len(self.__chromossome[row])-1)
				self.__chromossome[row] = self.__chromossome[row][0:i] + "-" + self.__chromossome[row][i::]
			print("row = %s\n" % (self.__chromossome[row]))

	def setChromossome(self, chromossome):
		self.__chromossome = chromossome
		self.__lengthChromossome()
	
	def setFitness(self, fitness):
		self.__fitness = fitness

	def setGeneration(self, generation):
		self.__generation = generation

	def getChromossome(self):
		return self.__chromossome

	def getFitness(self):
		return self.__fitness

	def getGeneration(self):
		return self.__generation

	def getLenAlignment(self):
		return self.__lenAlignment