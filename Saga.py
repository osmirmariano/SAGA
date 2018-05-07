#!/usr/bin/env python3
# -*- coding: utf-8 -*

from random import random
from Individual import Individual

class Saga():
	def __init__(self, populationSize = 20, numGenerations = 100, mutationRate = 0.1):
		self.__population = []
		self.__populationSize = populationSize
		self.__generation = 0
		self.__numGenerations = numGenerations
		self.__mutationRate = mutationRate
		self.__bestSolution = 0
		self.__best = []
		self.__worstSolution = 0 # Para efeitos de testes
		self.__worst = [] # Para efeito de testes
		

	"""
	A partir do alinhamento informado cria uma populacao de individuos randomicos
	"""
	def __initialPopulation(self, alignment):
		for i in range(0, self.__populationSize):
			self.__population.append(Individual(alignment))


	def __fitness(self, individual):
		pass


	"""
	Calcula o fitness de cada individuo da população atual, e a ordena com base neste valor
	"""
	def __scorePopulation(self):
		for Individual in self.__population:
			self.__fitness(individual)
		sorted(self.__population, key=lambda indiv: indiv.getFitness(), reverse=True)

	def __selectParent(self):
		pass

	"""
	Principal metodo do saga, o qual realizará a execução do algoritmo genetico, possui como 
	parametro o alinhamento a ser realizado
	"""
	def execute(self, alignment):
		self.__initialPopulation(alignment)
		self.__scorePopulation()

		while self.__generation < self.__numGenerations:
			parents = self.__selectParent()