# Listas --> Array, Vetores ou Matrizes -> São estruturas que conseguem guardar uma quantidade quase infinita de informação, porém não estão organizadas

# Criando uma lista com diferentes tipos de dados
lista_dos_sonhos = ["Aposentar Cedo", "Amandah quer ser Mãe", "Visitar a Suiça","Uma conta na suiça cheia de money que a Fernanda vai pagar!!", "Emprego Home Office!!"]

# Exibindo a lista completa
print(lista_dos_sonhos)

# Indices -> Acessando elementos individuais da lista pelo índice
print(lista_dos_sonhos[0], lista_dos_sonhos[3])

# Ordenando a lista em ordem alfanumérica (irá gerar erro se houver tipos mistos)
lista_dos_sonhos.sort()  # Isso funcionaria apenas se todos os itens fossem do mesmo tipo
print(lista_dos_sonhos)

# Indexação Negativa -> P   ermite acessar elementos da lista de trás para frente
print(lista_dos_sonhos[-1])

# Verificando o tipo de dado da lista e seu tamanho
# len() -> retorna o tamanho total da nossa lista
print(len(lista_dos_sonhos)) # Retorna a quantidade de elementos na lista
print(type(lista_dos_sonhos)) # Mostra que o tipo é 'list'

# Manipulação de listas - Métodos comuns

# insert - Adiciona um elemento em uma posição específica da lista
lista_dos_sonhos.insert(0, "Fernanda pagar todas as minhas dívidas")
print(lista_dos_sonhos)

# append -> Adiciona uma elemento ao final da nossa lista
lista_dos_sonhos.append("Ficar Rica e viajar ao mundo todo!!")
print(lista_dos_sonhos)

# sort -> Ordena em Ordem Alfanúmerica (números e letras) todos os nossos valores dentro da lista
nomes_que_ela_esta_devendo = ["Tayna", "Nathalia", "Frank", "Enzo", "Lucas,", "Camila", "Tulani", "Mayke", "Mônica", "Bianca", "Felipe", "Ana Luiza", "Henrique", "Audrey"]
nomes_que_ela_esta_devendo.sort() # Ordenação crescente (A-Z)
print(nomes_que_ela_esta_devendo)
nomes_que_ela_esta_devendo.sort(reverse=True) # Ordenação decrescente (Z-A)
print(nomes_que_ela_esta_devendo)

valores = [1, 15, 678, 987, 4356, 2975, 0]
valores.sort()
print(valores)

# remove -> Remove um elemento específico pelo valor fornecido
valores.remove(0)  # Remove o número 0 da lista
print(valores)

valores.remove(4356)  # Remove o número 4356 da lista
print(valores)

# pop -> Remove um elemento pelo índice informado
lista_comidas = ["Hambúrguer", "Lasanha", "Macarrão"]
print(lista_comidas)

lista_comidas.pop(1)
print(lista_comidas)

# Cadastro de pessoas usando listas
pessoas_cadastradas = []
qtd_pessoas = int(input("Digite quantas pessoas você quer cadastrar no Sistema de Crédito da Fernanda: "))

# Loop para adicionar os nomes na lista de cadastro
while len(pessoas_cadastradas) < qtd_pessoas:
    pessoas_cadastradas.append(input(f"Digite o nome da {len(pessoas_cadastradas) + 1}ª pessoa que você irá cadastrar: "))

    # Exibindo os nomes cadastrados
    print(f'As pessoas cadastradas foram: {pessoas_cadastradas}')