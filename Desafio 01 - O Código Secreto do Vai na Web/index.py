# Missão 1: Restaurando as Regras Escolares 📝 
# O vírus apagou os critérios de aprovação dos alunos! Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

aluno = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

if nota >= 6:
    print(f"O aluno(a) {aluno} foi aprovado(a) com a nota {nota}!") 
else:  
    print(f"O aluno(a) {aluno} foi reprovado(a) com a nota {nota}!")

# Missão 2: O Sistema Eleitoral Secreto 📝 
# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

idade = int(input("Digite a sua idade: "))
if idade >= 16:
    print("Você pode votar nas eleições do grêmio estudantil!")
else: 
    print("Você ainda não pode votar nas eleições do grêmio estudantil!")

# Missão 3: Recuperando o Sistema de Notas 📊
# As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F . Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:
# - A (90-100) – "Parabéns, você tirou A!"
# - B (80-89) – "Muito bem, você tirou B."
# - C (70-79) – "Bom trabalho, você tirou C."
# - D (60-69) – "Fique atento, você tirou D."
# - F (menos de 60) – "Estude um pouco mais, você tirou F."

nota = int(input("Digite a nota do aluno: "))

if nota >= 90:
    print("Parabéns, você tirou A!")
elif nota >= 80:
    print("Muito bem, você tirou B.")
elif nota >= 70:
    print("Bom trabalho, você tirou C.")
elif nota >= 60:
    print("Fique atento, você tirou D.")    
else:
    print("Estude um pouco mais, você tirou F.")

# Missão 4: Restaurando a Identificação de Números ⚖️
# Os robôs da escola precisam identificar padrões numéricos para resolver cálculos e otimizar os sistemas. No entanto, o vírus bagunçou os algoritmos e agora eles não conseguem mais somar corretamente!
    # Crie um programa que peça dois números ao usuário e exiba a soma deles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))  
soma = numero1 + numero2
print(f"A soma dos números {numero1} e {numero2} é igual a {soma}.")

# Missão 5: Recuperando o Cofre de Segurança 🔒
# O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha! Agora, apenas quem souber a combinação correta poderá acessá-lo.
    # Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".

senha = input("Digite a senha para acessar o cofre: ")
if senha == "Python123":
    print("Acesso permitido! A senha está correta.")
else:    
    print("Acesso negado! A senha está incorreta.")

# Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾
# O vírus está comprometendo o sistema de segurança e a contagem de registros! Para restaurar o funcionamento correto, você precisa reforçar as verificações e garantir que os dados sejam processados corretamente.
    # Exiba os números de 1 a 10 usando um loop while.  

contagem = 1
while contagem <= 10:
    print(f"Número {contagem}")
    contagem += 1

# Missão 7: Organizando a Lista📋
# Os números estão misturados e precisam ser organizados! 
    # Para resolver isso, você deve pegar os seguintes números: 8, 3, 10, 1 e 5, armazená-los em uma lista e depois exibi-los em ordem crescente. Isso ajudará a colocar tudo em ordem corretamente! 

listaNumerica = [8, 3, 10, 1, 5]
listaNumerica.sort()
print(listaNumerica)

# Missão 8: Acessando os Registros de Alunos 🏷️
# O sistema de alunos está desordenado! Para acessar as informações corretamente, você precisa organizar os dados.
    # Crie uma tupla com os seguintes nomes: Ana, Bruno, Carla, Daniel, Eduardo e exiba o primeiro e o último nome.  

alunos = ["Ana", "Bruno", "Carla", "Daniel", "Eduardo",]
print(f"Primeiro nome: {alunos[0]}")
print(f"Último nome: {alunos[-1]}")

# Missão 9: Calculando Dobro de um Número 🛠️
# Os alunos precisam de um programa que ajude em cálculos rápidos. 
    # Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
    # ➡️ Exemplo: dobro(5)
    # ➡️ Saída: "O dobro de 5 é 10"

numero = int(input("Digite um número: "))
dobro = numero * 2
print(f"O dobro de {numero} é {dobro}.") 

# Missão 10: Contando Letras 🔄
# O sistema precisa contar quantas letras há em um nome.
    # ➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
    # ➡️ Exemplo: contar_letras("Ana")
    # ➡️ Saída:" O nome Ana tem 3 letras"

def contar_letras(nome):
    nome = input("Digite um nome: ")
    quantidade = len(nome)
    print(f"O nome {nome} tem {quantidade} letras.")

contar_letras("nome")