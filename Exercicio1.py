"""
AC1 - Exercicio 1
Programação Estruturada
Esse programa calcula as raizes de uma equação do segundo grau através da fórmula de Bhaskara.

Autor: Marcelle Lohane Gonçalves Ganimo
Matricula: 202402726056
Turma: 1

"""
# Solicita os Coeficientes
a= float(input("coeficiente a: "))
b= float(input("coeficiente b: "))
c= float(input("coeficiente c: "))

#Calcula as Raizes através da fórmula de Bhaskara
delta= (b**2)-(4*a*c)
raiz1= (-b+(delta**(0.5)))/(2*a)
raiz2= (-b-(delta**(0.5)))/(2*a)

#Imprime as Raizes
print("As raízes da equação são", raiz1, "e", raiz2) 