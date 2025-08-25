import json

#dicionário
produto_1: dict = {
    "Tipo": "Sapato",
    "Tamanh0": 39,
    "Cor": "Branco/Preto",
    "Linha": "M",
    "Disponibilidade": True
}

produto_2: dict = {
    "Tipo": "Tenis",
    "Tamanh0": 39,
    "Cor": "Branco/Rosa",
    "Linha": "F",
    "Disponibilidade": False    
}

carrinho: list = []

carrinho.append(produto_1)
carrinho.append(produto_2)

#convertendo a lista para json
carrinho_json = json.dumps(carrinho)

print(carrinho)
print("-----------------")
print(f"Carrinho em json  {carrinho_json}")



