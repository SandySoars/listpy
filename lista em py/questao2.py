"""Faça um programa em Pascal que efetue o cálculo do salário líquido de um professor.
Os dados fornecidos serão: valor da hora aula, número de aulas dadas no mês e percentual de desconto do INSS."""
valor_hora = float(input())
num_aulas = float(input())
percentual_inss = float(input())

salario = valor_hora * num_aulas
print(salario)
desconto = salario * (percentual_inss/100)
print(desconto)
salario_bruto = salario - desconto

print("{:.2f}".format(salario_bruto))
