# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:02:14 2024

@author: miguel
"""
import math
import random
import matplotlib.pyplot as plt
import numpy as np

x = 0
def func(x):
    y = - abs(x*(math.sin(math.sqrt(abs(x)))))
    return y

def gerarelementos(quantidade):
    elementos = [random.randint(0, 512) for _ in range(quantidade)]
    print(elementos)
    return elementos

def gerarElementosBinarios(decimal_list):
    binar = []
    for decimal in decimal_list:
        # Convertendo para binário e removendo o prefixo '0b'
        binario_sem_prefixo = bin(decimal)[2:]
        # Preenchendo com zeros à esquerda para garantir que tenha 10 bits
        binario_com_zeros = binario_sem_prefixo.zfill(10)
        binar.append(binario_com_zeros)
    print(binar)
    return binar

def gerarImagem(decimal_list):
    imagem = []
    for decimal in decimal_list:
        imagem.append((func(decimal)*(-1)))
    print(imagem)
    return imagem

def gerarProbabilidades(imagemFuncao):
    aptidoes = sum(imagemFuncao)
    probrolet = []
    for i in range(len(imagemFuncao)):
        probrolet.append((imagemFuncao[i]/aptidoes))
    return probrolet

def separarVinteMelhores(probabRolet,popBin):
    melhores = []
    for i in range(len(probabRolet)):
        maiorprob = max(probabRolet)
        indice  = probabRolet.index(maiorprob)
        probabRolet[indice] = 0
        melhores.append(popBin[indice])
    print(melhores)
    return melhores

def sortearCasais():
    casais = np.zeros((10, 2), dtype=int)
    numeros_sorteados = set()  # Usando um conjunto para armazenar os números sorteados e garantir que não haja repetições
    for i in range(10):
        for j in range(2):
            aleatorio = random.randint(0, 19)
            while aleatorio in numeros_sorteados:  # Verifica se o número já foi sorteado
                aleatorio = random.randint(0, 19)
            casais[i][j] = aleatorio
            numeros_sorteados.add(aleatorio)  # Adiciona o número sorteado ao conjunto
    print(casais)
    return casais
    
def gerarPontoDeCorte():
    pc = random.uniform(0.5,0.95)
    return pc

def recombinar(pontoCorte,recomb,melhores):
    filhos =[]
    bits = len(melhores[recomb[0][0]])
    pc = round(pontoCorte*bits)
    print(pc)
    for i in range(10):
        # Dividindo a string em duas a partir do índice especificado
        bits1_1 = melhores[recomb[i][0]][:pc]
        print(bits1_1)
        bits1_2 = melhores[recomb[i][0]][pc:]
        print(bits1_2)

        bits2_1 = melhores[recomb[i][1]][:pc]
        print(bits2_1)
        bits2_2 = melhores[recomb[i][1]][pc:]
        print(bits2_2)
        
        filho1 = bits1_1 + bits2_2
        print(filho1)
        filho2 = bits2_1 + bits1_2   
        print(filho2)
        filhos.append(filho1)
        filhos.append(filho2)
    print(filhos)
    return filhos

def efetuarMutacao(filhos):
    filhosmutados = []
    mutacao = random.uniform(0.001, 0.1)
    for i in range(20):
        filho = list(filhos[i])  # Converte a string para lista
        for j in range(len(filho)):
            prob = random.uniform(0, 0.5)
            if prob < mutacao:
                bit = int(filho[j])
                bit = 1 - bit
                filho[j] = str(bit)  # Modifica o elemento da lista
        filhosmutados.append("".join(filho))  # Converte a lista de volta para string e adiciona à lista de filhos mutados
        print(filhosmutados)
    return filhosmutados

def novaPopulação(binario,filhos):
    decimais = gerarelementos(30)
    binar = gerarElementosBinarios(decimais)
    novapop = []
    for i in range(len(filhos)):
        novapop.append(filhos[i])
    for i in range(len(binar)):
        novapop.append(binar[i])
    print(novapop)
    return novapop

def novosValoresDecimais(binar):
    decimal = []
    for i in range(len(binar)):
        valor = int(binar[i], 2)
        decimal.append(valor)
    print(decimal)
    return decimal

geracao = 0
convergencia = 0
limiteconverg = 100
minimoglobal = 0
popDec = gerarelementos(50)

while(geracao < 10000 and convergencia<limiteconverg):
    popBin = gerarElementosBinarios(popDec)
    imagemFuncao = gerarImagem(popDec)
    probabRolet = gerarProbabilidades(imagemFuncao)
    sMelhores = separarVinteMelhores(probabRolet,popBin)
    recomb = sortearCasais()
    pontoCorte = gerarPontoDeCorte()
    s_filhos = recombinar(pontoCorte,recomb,sMelhores)
    s_filhos = efetuarMutacao(s_filhos)
    popBin = novaPopulação(popBin,s_filhos)
    popDec = novosValoresDecimais(popBin)
    minimo = max(gerarImagem(popDec))
    if(minimo > minimoglobal):
        minimoglobal = minimo
        convergencia = 0
    else:
        convergencia = convergencia + 1
    print(minimoglobal)
    geracao = geracao + 1