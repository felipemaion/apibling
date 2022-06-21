import os

import requests
from dotenv import load_dotenv, find_dotenv
import json
from time import sleep

load_dotenv(find_dotenv())
BLING_SECRET_KEY = os.getenv("BLING_API_KEY")


def list_products(page='all'):
    url = f'https://bling.com.br/Api/v2/produtos/page={page}/json/'
    payload = {'apikey': BLING_SECRET_KEY,
               'imagem': 'S'}

    if page == 'all':
        page = 1
        all_products = {'retorno': {'produtos': []}}

        while True:
            url = f'https://bling.com.br/Api/v2/produtos/page={page}/json/'
            produtos = requests.get(url, params=payload)
            sleep(1)
            try:
                pagina = produtos.json()['retorno']['produtos']
                page += 1
                for item in pagina:
                    all_products['retorno']['produtos'].append(item)
            except KeyError as e:
                break

        return all_products

    produtos = requests.get(url, params=payload)
    sleep(1)
    return produtos

def products_to_json(page='all', debug=True):
    if debug==True:
        return json.loads(open('produtos.json').read())
    else:
        data = export_products(page)
        return json.loads(json.dumps(data))


def export_products(page='all'):
    with open('produtos.json', 'w') as outfile:
        data = list_products(page=page)
        json.dump(data, outfile)
    return data

def only_produtosPai():
    # todo listar somente o pai.
    pass
    

def filter_products_by_(key='codigo', value='NWC01P'):
    filtered = []
    all_products = products_to_json()["retorno"]["produtos"]

    for product in all_products:
        if key in product['produto']:
            if product['produto'][key] == value:
                filtered.append(product)
    return filtered
    


def find_variacoes(codigo):
    produto = find_codigoPai_by_codigo(codigo)
    retorno = {}
    
    if len(produto) > 0:
        retorno['codigoSuperior'] = produto['produto']['codigo']
        virtuais = find_virtuais(produto['produto']['codigo'])
        retorno['virtuais']= virtuais
        if 'variacoes' in produto['produto']:
            retorno['variacoes'] = produto['produto']['variacoes']
        else:
            print(f"O codigo superior:{produto['produto']['codigo']} não tem variacoes.")
            retorno['codigoPai'] = filter_products_by_('codigo', codigo)[0]['produto']['codigoPai']
            retorno['variacoes']= find_variacoes(retorno['codigoPai'])
    return retorno
    
def find_virtuais(codigo):
    filtered = []
    all_products = products_to_json()["retorno"]["produtos"]

    for product in all_products:
        if 'estrutura' in product['produto']:
            if product['produto']['estrutura'][0]['componente']['codigo'] == codigo:
                filtered.append({'codigo':product['produto']['codigo']})
    return filtered


# Achar produto por codigo e retornar o produtoPai (e as variações) desse codigo.
def find_codigoPai_by_codigo(codigo):
    # procurar como produto pai:
    produtoPrincipal = filter_products_by_('codigo', codigo)
    if (produtoPrincipal != []):
        # if ('codigoPai' in produtoPrincipal[0]['produto']):
        #     produtoPai = filter_products_by_('codigo', produtoPrincipal[0]['produto']['codigoPai'])[0]
        #     return produtoPai
        # elif
        if ('estrutura' in produtoPrincipal[0]['produto']):
            produtoPai = filter_products_by_('codigo', produtoPrincipal[0]['produto']['estrutura'][0]['componente']['codigo'])[0]
            return produtoPai
    elif (produtoPrincipal == []):
        produtoPai = []
    
    produtoPai = produtoPrincipal[0]
    
    return produtoPai
            
def f1():
    codigo = 'NWC01P'
    return find_codigoPai_by_codigo(codigo)
    
def f2():
    codigo = 'NWC01F'
    return find_codigoPai_by_codigo(codigo)

def test_find_codigoPai_by_codigo():
    assert f1() == f2()
    
    
def get_product(codigo):
    url = f'https://bling.com.br/Api/v2/produto/{codigo}/json/'
    payload = {'apikey': BLING_SECRET_KEY,
               'imagem': 'S'}

    produto = requests.get(url, params=payload)
    sleep(1)
    return produto.json()["retorno"]["produtos"][0]['produto']


def get_produto(codigo):
    produto = find_codigoPai_by_codigo(codigo)["produto"]
    return produto


def get_produtoLoja(idLoja, codigo):
    # 203330855
    url = f'https://bling.com.br/Api/v2/produto/{codigo}/json/'
    payload = {'apikey': BLING_SECRET_KEY,
               'imagem': 'S',
               'loja':idLoja}
    produto = requests.get(url, params=payload).json()
    sleep(1)
    if 'retorno' in produto:
        produto = produto['retorno']['produtos'][0]['produto']
        if 'produtoLoja' in produto:
            return {'codigo':produto['codigo'], 'produtoLoja':produto['produtoLoja'], 'loja':idLoja}
    return {}


def get_produtoLojas(codigo):
    lojas = [{'nome':'1 - Magalu','codigo':'203330855'},
            {'nome':'2 - Mercado Livre' ,'codigo':'203330826'},
            {'nome':'3 - Shopee' ,'codigo':'203567665'},
            {'nome':'4 - B2W','codigo': '203185493'},
            {'nome':'Loja Jundiaí','codigo': '203415283'}]
    lojasdoProduto = {'codigoProduto':codigo, 'produtoLojas':[]}
    for loja in lojas:
        produtoLoja = get_produtoLoja(loja['codigo'], codigo)
        if produtoLoja != {}:
            lojasdoProduto['produtoLojas'].append(produtoLoja)
    return lojasdoProduto


# Produtos a investigar: 
# 101033811
# AL-MYBABY-003
# KECOMS8
# 101033351
# 101033763
# TUTTICARE85
# ET4ZN9NEN
# 12117