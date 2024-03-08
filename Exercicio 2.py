"""
AC1- Exercicio 2
Programação Estruturada

Este programa indica se o ano é bissexto ou não.
Autor: Marcelle Lohane Gonçalves Ganimo
Matricula: 202402726056
Turma: 1
"""
# Solicita o ano
ano = int(input("Digite o ano: "))

# Verifica se o ano é bissexto
print(f"O ano é bissexto? {ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0}")
