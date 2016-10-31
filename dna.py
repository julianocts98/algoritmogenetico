#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class DNA:

	def __init__(self,alvo,mutationRate):
		self.alvo = alvo
		self.genes = []
		self.mutationRate = mutationRate

		for _ in range(0,len(alvo)):
			letra = chr(random.randint(32,128)) # caracter ASCII aleatório
			self.genes.append(letra)

	def crossover(self, parceiro):
		crianca = DNA(self.alvo, self.mutationRate)
		pontoDeCorte = int(random.randint(0,len(self.alvo)-1))
		i = 0
		for i in range(0,len(self.alvo)):
			if (i < pontoDeCorte):
				crianca.genes[i] = self.genes[i]
			else:
				crianca.genes[i] = parceiro.genes[i]
		return crianca

	def mutate(self):
		for _ in range(0,len(self.genes)):
			if (random.uniform(0,1) < self.mutationRate):
				self.genes[_] = chr(random.randint(32,128))

	def setFitness(self):
		tamanhoAlvo = len(self.alvo)
		score = 0
		for _ in range(0,len(self.genes)):
			if (self.genes[_] == self.alvo[_]):
				score += 1
		self.fitness = score/tamanhoAlvo

	def frase(self):
		frase = ""
		for l in self.genes:
			frase += l
		return str(frase)