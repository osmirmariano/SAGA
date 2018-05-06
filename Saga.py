#!/usr/bin/env python3
# -*- coding: utf-8 -*

from random import random
from Individual import Individual

class Saga():
	def __init__(self, populationSize, numGenerations = 100, mutationRate = 0.1):
		self.__populationSize = populationSize
		self.__numGenerations = numGenerations
		self.__mutationRate = mutationRate
		self.__generation = 0
		self.__bestSolution = 0
		self.__best = []
		self.__worstSolution = 0 # Para efeitos de testes
		self.__worst = [] # Para efeito de testes
		self.__population = []


	"""
	A partir do alinhamento informado cria uma populacao de individuos randomicos
	"""
	def __initialPopulation(self, alignment):
		for i in range(0, self.__populationSize):
			self.__population.append(Individual(alignment))


	"""
	Calcula o fitness de cada individuo da população atual
	"""
	def scorePopulation(self):
		pass


	def execute():
		pass
