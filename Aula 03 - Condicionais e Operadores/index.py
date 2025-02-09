primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))

print(f'A soma dos valores são: {primeiro_valor + segundo_valor}')

# Exibindo mensagem de boas-vindas
print("Bem vindo à Lanchonete Vai nos Lanches")

# Solicitando informações sobre o pedido
pedido_cliente = input("Olá, querido cliente! Qual seu prato? ")  # Captura o prato escolhido
bebida_cliente = input("E o que gostaria de beber? ")  # Captura a bebida escolhida

# Exibindo o pedido formatado
print(f'O seu pedido foi registrado: {pedido_cliente} acompanhado de {bebida_cliente}.')

# Solicita os preços do prato e da bebida e os converte para float
valor_prato = float(input(f'O valor do seu pedido {pedido_cliente} é de: R$ '))
valor_bebida = float(input(f'O valor da sua bebida {bebida_cliente} é de: R$ '))

# Exibindo o total sem formatação decimal fixa
print(f'O valor total que você irá pagar é R$ {valor_prato + valor_bebida}')

# Condicionais --> Elas são as responsáveis por executarem um determinado bloco de código, baseado em uma ou mais respostas específicas

# Condicionais Simples
# Se o saldo for False (não há dinheiro), exibe uma mensagem
saldo = True  # Variável indicando se há saldo disponível

if not saldo:  
    print("Tá Lascado!")
    print("Sinto muito pela sua situação, também tô assim!!!")


# Condicionais Compostas
# Se o saldo for False (não há dinheiro), exibe uma mensagem
# Pergunta ? Executa uma ação do Tipo A se não: Executa uma ação do tipo B
idade = 18
if saldo and idade >= 18:
    print("Uhuuuul, você pode mandar um pix aos seus instrutores!!!")
else:
    print(f"Infelizmente você não pode mandar um pix para os seus instrutores, porque ou sua idade é {idade} ou o seu saldo é {saldo}!!!")

# Condicionais Aninhadas
# Verifica múltiplas condições de saldo e idade
jantar = "Churrasco acompanhado de fritas e farofa"
bebida = "Coca-Cola"

if jantar == "Churrasco acompanhado de fritas e farofa" and bebida == "Coca-Cola": 
    print("Partiuuuuu!! Churrascada!!")
elif jantar == "Strogonoff de Frango" and bebida =="Dolly Guaraná":
    print("Partiuuu!! Comer Strogonoff")
else:
    print("Deixo pra próxima!")

# Operadores Lógicos e Operadores de Comparação em Python

# JavaScript -> &, ||, !
# Python -> and, or, not

# and (e) -> Retorna True se uma sentença E outra é verdadeira (Eu quero Batata Frita e Coca-Cola)
# or(ou) -> Retorna True se uma das duas sentenças for verdadeira (Ou eu quero Batat Frita ou Coca-Cola)
# not(negação) -> Retorna True se a sentença for falsa ()

# Operadores de Comparação:
# >  : Maior que
# <  : Menor que
# >= : Maior ou igual a
# <= : Menor ou igual a
# != : Diferente de
# == : Igual a

# Exemplo prático
a = 20
b = 10

print(f'{a} > {b}:', a > b)   # True  -> Verifica se "a" é maior que "b"
print(f'{a} < {b}:', a < b)   # False -> Verifica se "a" é menor que "b"
print(f'{a} >= {b}:', a >= b) # True  -> Verifica se "a" é maior ou igual a "b"
print(f'{a} <= {b}:', a <= b) # False -> Verifica se "a" é menor ou igual a "b"
print(f'{a} == {b}:', a == b) # False -> Verifica se "a" é igual a "b"
print(f'{a} != {b}:', a != b) # True  -> Verifica se "a" é diferente de "b"