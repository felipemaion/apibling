# Objetivo:
# Recebe o produto e retorna os preços para as diferentes plataformas.

# condiçoes de peso por plataforma.
# condições premium?

# MG = (PV - C) / PV
# PV*MG = PV - C
# PV*(MG-1) = C
# PV = C / (MG-1)
# 
# MG: Margem, PV: Preço de Venda, C: Custo
# 
# C = Custo Produto + Comissao + Imposto + Frete + Embalagem 

# Custo Produto: Cadastro Produto.
# Comissao: Comissao Loja.
# Exemplo 1: Mercado Livre:  {'nome':'2 - Mercado Livre' ,'codigo':'203330826'},
# =SE(AA2="Premium";SE(E2<79;16%*E2+5;16%*E2);SE(E2<79;11,5%*E2+5;11,5%*E2))
if tipoAnuncio == 'Premium':
    if precoVenda < 79:
        comissao = (0.16 * precoVenda) + 5
    else:
        comissao = (0,16 * precoVenda)
else:
    if precoVenda < 79:
        comissao = (0.115 * precoVenda) + 5
    else:
        comissao = (0.115 * precoVenda)
        
        

imposto = precoVenda * 0.11

embalagem = 0.8


# Frete:

# Peso*	            Produtos novos de menos de R$ 79,		Produtos novos a partir de R$ 79		 Categorias especiais	
# 			        usados e anúncios grátis                50% de desconto                          25% de desconto	
# 	                Full    	Outros	                    Full	    Outros	                     Full	    Outros
# Até 500 g	        R$ 33,90	R$ 33,90	                R$ 16,95	R$ 16,95	                 R$ 25,42	R$ 25,42
# De 500 g a 1 kg	R$ 36,90	R$ 36,90	                R$ 18,45	R$ 18,45	                 R$ 27,67	R$ 27,67
# De 1 kg a 2 kg	R$ 37,90	R$ 37,90	                R$ 18,95	R$ 18,95	                 R$ 28,42	R$ 28,42
# De 2 kg a 5 kg	R$ 46,90	R$ 46,90	                R$ 23,45	R$ 23,45	                 R$ 35,17	R$ 35,17
# De 5 kg a 9 kg	R$ 69,90	R$ 69,90	                R$ 34,95	R$ 34,95	                 R$ 52,42	R$ 52,42
# De 9 kg a 13 kg	R$ 109,90	R$ 109,90	                R$ 54,95	R$ 54,95	                 R$ 82,42	R$ 82,42
# De 13 kg a 17 kg	R$ 121,90	R$ 121,90	                R$ 60,95	R$ 60,95	                 R$ 91,42	R$ 91,42
# De 17 kg a 23 kg	R$ 142,90	R$ 142,90	                R$ 71,45	R$ 71,45	                 R$ 107,17	R$ 107,17
# De 23 kg a 30 kg	R$ 164,90	R$ 164,90	                R$ 82,45	R$ 82,45	                 R$ 123,67	R$ 123,67
# De 30 a 40 kg	    R$ 186,90	R$ 186,90	                R$ 93,45	R$ 93,45	                 R$ 140,17	R$ 140,17
# De 40 a 50 kg	    R$ 199,90	R$ 199,90	                R$ 99,95	R$ 99,95	                 R$ 149,92	R$ 149,92
# De 50 a 60 kg	    R$ 214,90	R$ 214,90	                R$ 107,45	R$ 107,45	                 R$ 161,17	R$ 161,17
# De 60 a 70 kg	    R$ 230,90	R$ 230,90	                R$ 115,45	R$ 115,45	                 R$ 173,17	R$ 173,17
# De 70 a 80 kg	    R$ 245,90	R$ 245,90	                R$ 122,95	R$ 122,95	                 R$ 184,42	R$ 184,42
# De 80 a 90 kg	    R$ 261,90	R$ 261,90	                R$ 130,95	R$ 130,95	                 R$ 196,42	R$ 196,42
# De 90 a 100 kg	R$ 276,90	R$ 276,90	                R$ 138,45	R$ 138,45	                 R$ 207,67	R$ 207,67
# De 100 a 125 kg	R$ 296,90	R$ 296,90	                R$ 148,45	R$ 148,45	                 R$ 222,67	R$ 222,67
# De 125 a 150 kg	R$ 315,90	R$ 315,90	                R$ 157,95	R$ 157,95	                 R$ 236,92	R$ 236,92
# Maior que 150 kg	R$ 331,90	R$ 331,90	                R$ 165,95	R$ 165,95	                 R$ 248,92	R$ 248,92

# =SE(E3>=79;SE(O3<=0,499;'Tabela de Frete MELI'!$D$4;SE(E(O3>=0,5;O3<0,999);'Tabela de Frete MELI'!$D$5;SE(E(O3>=1;O3<1,999);'Tabela de Frete MELI'!$D$6;SE(E(O3>=2;O3<4,999);'Tabela de Frete MELI'!$D$7;SE(E(O3>=5;O3<8,999);'Tabela de Frete MELI'!$D$8;SE(E(O3>=9;O3<12,999);'Tabela de Frete MELI'!$D$9;'Tabela de Frete MELI'!$D$10))))));0)
