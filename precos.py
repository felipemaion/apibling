# Objetivo:
# Recebe o produto e retorna os preços para as diferentes plataformas.

# condiçoes de peso por plataforma.
# condições premium?

# MG = (PV - C) / PV
# PV*MG = PV - C
# PV*(MG-1) = - C
# PV = C / (1 - MG)
# 
# MG: Margem, PV: Preço de Venda, C: Custo
# 
# C = Custo Produto + Comissao + Imposto + Frete + Embalagem 

# Custo Produto: Cadastro Produto.
# Comissao: Comissao Loja.
# Exemplo 1: Mercado Livre:  {'nome':'2 - Mercado Livre' ,'codigo':'203330826'},
# =SE(AA2="Premium";SE(E2<79;16%*E2+5;16%*E2);SE(E2<79;11.5%*E2+5;11.5%*E2))

import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(sys.getrecursionlimit()*50) # Vai saber quão longe vai o preço de venda. ?

def calcular_comissao(precoVenda, tipoAnuncio="Premium"):
    if tipoAnuncio != 'Premium':
        if precoVenda < 79:
            comissao = (0.16 * precoVenda) + 5
        else:
            comissao = (0.16 * precoVenda)
    else:
        if precoVenda < 79:
            comissao = (0.115 * precoVenda) + 5
        else:
            comissao = (0.115 * precoVenda)
    return comissao            


def calcular_imposto(precoVenda):
    imposto = precoVenda * 0.11
    return imposto

def calcular_embalagem():
    embalagem = 0.8
    return embalagem


# Frete:
# A:A               B:B                                     D:D
# Peso*	            Produtos novos de menos de R$ 79.		Produtos novos a partir de R$ 79		 Categorias especiais	
# 			        usados e anúncios grátis                50% de desconto                          25% de desconto	
# 	                Full    	Outros	                    Full	    Outros	                     Full	    Outros
# Até 500 g	        R$ 33.90	R$ 33.90	                R$ 16.95	R$ 16.95	                 R$ 25.42	R$ 25.42
# De 500 g a 1 kg	R$ 36.90	R$ 36.90	                R$ 18.45	R$ 18.45	                 R$ 27.67	R$ 27.67
# De 1 kg a 2 kg	R$ 37.90	R$ 37.90	                R$ 18.95	R$ 18.95	                 R$ 28.42	R$ 28.42
# De 2 kg a 5 kg	R$ 46.90	R$ 46.90	                R$ 23.45	R$ 23.45	                 R$ 35.17	R$ 35.17
# De 5 kg a 9 kg	R$ 69.90	R$ 69.90	                R$ 34.95	R$ 34.95	                 R$ 52.42	R$ 52.42
# De 9 kg a 13 kg	R$ 109.90	R$ 109.90	                R$ 54.95	R$ 54.95	                 R$ 82.42	R$ 82.42
# De 13 kg a 17 kg	R$ 121.90	R$ 121.90	                R$ 60.95	R$ 60.95	                 R$ 91.42	R$ 91.42
# De 17 kg a 23 kg	R$ 142.90	R$ 142.90	                R$ 71.45	R$ 71.45	                 R$ 107.17	R$ 107.17
# De 23 kg a 30 kg	R$ 164.90	R$ 164.90	                R$ 82.45	R$ 82.45	                 R$ 123.67	R$ 123.67
# De 30 a 40 kg	    R$ 186.90	R$ 186.90	                R$ 93.45	R$ 93.45	                 R$ 140.17	R$ 140.17
# De 40 a 50 kg	    R$ 199.90	R$ 199.90	                R$ 99.95	R$ 99.95	                 R$ 149.92	R$ 149.92
# De 50 a 60 kg	    R$ 214.90	R$ 214.90	                R$ 107.45	R$ 107.45	                 R$ 161.17	R$ 161.17
# De 60 a 70 kg	    R$ 230.90	R$ 230.90	                R$ 115.45	R$ 115.45	                 R$ 173.17	R$ 173.17
# De 70 a 80 kg	    R$ 245.90	R$ 245.90	                R$ 122.95	R$ 122.95	                 R$ 184.42	R$ 184.42
# De 80 a 90 kg	    R$ 261.90	R$ 261.90	                R$ 130.95	R$ 130.95	                 R$ 196.42	R$ 196.42
# De 90 a 100 kg	R$ 276.90	R$ 276.90	                R$ 138.45	R$ 138.45	                 R$ 207.67	R$ 207.67
# De 100 a 125 kg	R$ 296.90	R$ 296.90	                R$ 148.45	R$ 148.45	                 R$ 222.67	R$ 222.67
# De 125 a 150 kg	R$ 315.90	R$ 315.90	                R$ 157.95	R$ 157.95	                 R$ 236.92	R$ 236.92
# Maior que 150 kg	R$ 331.90	R$ 331.90	                R$ 165.95	R$ 165.95	                 R$ 248.92	R$ 248.92

def calcular_frete(peso, precoVenda):
    frete = 0
    if peso < 0.5:
        frete = 16.95
    elif 0.5 <= peso < 1:
        frete = 18.45
    elif 1 <= peso < 2:
        frete = 18.95
    elif 2 <= peso < 5:
        frete = 23.45
    elif 5 <= peso < 9:
        frete = 34.95
    elif 9 <= peso < 13:
        frete = 54.95
    elif 13 <= peso < 17:
        frete = 60.95
    elif 17 <= peso < 23:
        frete = 71.45
    elif 23 <= peso < 30:
        frete = 82.45
    elif 30 <= peso < 40:
        frete = 93.45
    elif 40 <= peso < 50:
        frete = 99.95
    elif 50 <= peso < 60:
        frete = 107.45
    elif 60 <= peso < 70:
        frete = 115.45
    elif 70 <= peso < 80:
        frete = 122.95
    elif 80 <= peso < 90:
        frete = 130.95
    elif 90 <= peso < 100:
        frete = 138.45
    elif 100 <= peso < 125:
        frete = 148.45
    elif 125 <= peso < 150:
        frete = 157.95
    elif peso >= 150:
        frete = 165.95
        
    if precoVenda < 79:
        frete = 0
    return frete

def calcular_custo(produto, precoVenda):
    peso = float(produto['pesoLiq'])
    frete = calcular_frete(peso, precoVenda)
    
    precoCusto = float(produto['precoCusto'])
    imposto = calcular_imposto(precoVenda)
    embalagem = calcular_embalagem()
    comissao = calcular_comissao(precoVenda)
    soma_custos = precoCusto + comissao + imposto + embalagem + frete  
    custo = {'custoTotal': soma_custos, 'precoCusto':precoCusto, 'comissao':comissao, 'imposto':imposto,  'embalagem':embalagem,'frete':frete}
    
    # print(f"precoVenda:{precoVenda}; custo:{custo} = precoCusto:{precoCusto} + comissao:{comissao} + imposto:{imposto} + embalagem:{embalagem} + frete:{frete}")
    return custo


def calcular_margem(preco_de_venda, custo_total):
    return (preco_de_venda - custo_total) / preco_de_venda


def calcular_preco_venda(produto, margem, preco_inicial=None, incremento=100, erro=0.01):
    if type(produto) is not dict and type(produto) is str:
        produto = get_produto(produto) # Entrou com o código do produto.
    preco_inicial = float(produto['preco']) if preco_inicial is None else preco_inicial
    custos = calcular_custo(produto, preco_inicial)
    custo_total = custos['custoTotal']
    
    margem_calc = calcular_margem(preco_inicial, custo_total)
    taxa_margem = (margem_calc / margem)
    # print(f"\n\tpreco_inicial:{preco_inicial} custo_total:{custo_total} margem_calc:{margem_calc} margem:{margem}, margem_calc\margem:{(taxa_margem)} \n")
   
    if (1 - erro) <= (taxa_margem) <= (1 + erro):
        preco_final = preco_inicial
        
        print(f"PREÇO FINAL: R$ {preco_final:.2f} \n\t \
                - margem_target:{margem:.2%}; margem_calc:{margem_calc:.2%}; margem_calc\margem_target:{taxa_margem:.5f}; \n\t \
                - Custos: {custos} \n\t \
                - Lucro: R$ {(preco_final - custo_total):.2f} = ( precoVenda: R$ {preco_final:.2f} - custo_total: R$ {custo_total:.2f} )\n")
        return preco_final
    if margem_calc > margem: 
        # print("Decrementando Preco Final")
        preco_final = preco_inicial - incremento
        incremento = incremento / 2 
        incremento = max(incremento, 0.01)
        # print(incremento)
    if margem_calc < margem: 
        # print("Incrementando Preco Final")
        preco_final = preco_inicial + incremento
        if taxa_margem > 0.9:
            incremento = incremento / 2
        incremento = max(incremento, 0.01)
        # print(incremento)
    # print(f"preco_inicial = {preco_inicial} --> preco_final = {preco_final}")
    # input()
    return calcular_preco_venda(produto, margem, preco_final, incremento)
       


# mg = 13%
# pv = (precoVenda - custo)/(1 - mg)

def test_calcular_frete():
    assert calcular_frete(0.5, 79) == 18.45
    assert calcular_frete(0.499, 79) == 16.95
    assert calcular_frete(0.499, 78.99) == 33.90
    assert calcular_frete(150, 78.99) == 331.90
    print("Todos os testes passaram!")
    

def test_calcular_margem():
    assert calcular_margem(100, 80) == 0.2
    assert calcular_margem(100, 50) == 0.5



from produtos import *
p = get_produto('0080054-1')