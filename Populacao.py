from dna import *
class Populacao:
	
	def __init__(self,alvo,mutationRate,qtd):
		self.individuos = []
		self.alvo = alvo
		self.mutationRate = mutationRate
		self.qtd = qtd
		self.geracao = 1
		self.piscina = []

		for _ in range(0,qtd):
			i = DNA(self.alvo,self.mutationRate)
			self.individuos.append(i)

	def evaluate(self):
		for _ in range(0,len(self.individuos)):
			self.individuos[_].setFitness()

	def enchePiscina(self):
		for _ in range(0,len(self.individuos)):
			n = int(self.individuos[_].fitness*100)
			i = 0
			for i in range(0,n):
				self.piscina.append(self.individuos[_])

	def esvaziaPiscina(self):
		self.piscina = []

	def reproduzir(self):
		novosIndividuos = []
		for _ in range(0,len(self.individuos)):
			posA = random.randint(0,len(self.piscina)-1)
			posB = random.randint(0,len(self.piscina)-1)

			parceiroA = self.piscina[posA]
			parceiroB = self.piscina[posB]

			crianca = parceiroA.crossover(parceiroB)
			crianca.mutate()

			novosIndividuos.append(crianca)
			
		self.individuos = novosIndividuos

	def fittest(self):
		for _ in range(0,len(self.individuos)):
			if (self.individuos[_].fitness > self.individuos[self.melhorIndice].fitness):
				self.melhorIndice = _



	def evoluir(self):
		self.melhorIndice = 0
		fraseGenetica = ""
		while (True):
			self.evaluate()
			indiceMelhor = self.fittest()
			print("Melhor até o momento: "+self.individuos[self.melhorIndice].frase()+" com fitness de: "+str(int(self.individuos[self.melhorIndice].fitness*100))+"%")
			self.esvaziaPiscina()
			self.enchePiscina()
			self.reproduzir()

			self.geracao += 1

			for _ in range(0,len(self.individuos)):
				fraseGenetica = self.individuos[_].frase()
				if(fraseGenetica == self.alvo):
					break

			if(fraseGenetica == self.alvo):
				break
		print("Geração: "+str(self.geracao))
		print("Frase: "+fraseGenetica)



