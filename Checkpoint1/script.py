


def acha_media(lista):    
    soma = 0    
    for num in lista:        
        soma += num    
    return soma / len(lista)
    
def i_maior(lista):    
    indice_maior = 0
    maior_elem = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i] > maior_elem:
            indice_maior = i
            maior_elem = lista[i]
    return indice_maior

def i_menor(lista):    
    indice_menor = 0
    menor_elem = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor_elem:
            indice_menor = i
            menor_elem = lista[i]
    return indice_menor

def obriga_cond(msg, cond):
    form = input(msg)
    while form not in cond:
        print("Resposta inválida")
        form = input(msg)
    return form

def verifica_num(msg):
    escolha = input(msg)
    while not escolha.isnumeric():
        print("Apenas números são permitidos")
        escolha = input(msg)
    return int(escolha)

def acha_indice(lista, elem):
    index = 0
    for i in lista:
        if i == elem:
            return index
        else:
            index += 1

vinhos = ['Tinto', 'Rose', 'Branco']
precos = [100, 250, 300]

index_compra_vinho = []
compra_qtd = []

print("Boas-Vindas")
enedereco = input("Qual o seu enderço: ")
# Verfificação Idade
nascimento = verifica_num("Qual a seu ano de nascimento: ")
if 2025 - nascimento < 18:        
    print("Você é menor de idade, VENDA PROIBIDA")
else:
    # Valores dos Vinhos
    while True:
        media_vinho = acha_media(precos)
        caro_vinho = i_maior(precos)
        barato_vinho = i_menor(precos)
        print(f"\nO custo médio dos vinhos é {media_vinho:.2f}\nMais caro: {vinhos[caro_vinho]} - {precos[caro_vinho]}\nMais barato: {vinhos[barato_vinho]} - {precos[barato_vinho]}\n")
        # Opções de Vinho
        print("As opções de vinhos são:")
        for wine in range(len(vinhos)):
            print(f"{vinhos[wine]} - {precos[wine]}")
        escolha = obriga_cond("Qual vinho você irá querer: ", vinhos)
        index_compra_vinho.append(acha_indice(vinhos, escolha))
        # Quantidade de Vinhos
        quant = verifica_num(f"Quantos vinho(s) {escolha}(s) você irá querer: ")
        compra_qtd.append(quant)
        # Verificação se quer continuar
        s_n = obriga_cond("Quer comprar mais?? (s/n)", ["s", "n"])
        if s_n == "s":
            continue
        else:
            break
    # Printando Resultados Finais
    print(f"\n---STATUS DA COMPRA---")
    count = 0
    total = 0
    for wines in index_compra_vinho:
        print(f"Vinho: {vinhos[wines]} - Qtd: {compra_qtd[count]} = Total: {compra_qtd[count] * precos[wines]}")
        total += compra_qtd[count] * precos[wines]
        count += 1
    frete = total * 0.10
    if total > 500:
        print("Você ganhou frete grátis")
    else:
        print(f"Com taxa de 10%, você irá pagar {frete:.2f} de frete")
    print(f"O valor total foi: {total + frete:.2f}")

        