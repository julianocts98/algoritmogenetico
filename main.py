#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from Populacao import *

alvo = "frase"
mutationRate = 0.01
qtdPopulacao = 2000
populacao = Populacao(alvo,mutationRate,qtdPopulacao)
populacao.evoluir()
