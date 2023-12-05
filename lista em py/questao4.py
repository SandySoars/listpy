"""Faça um programa em Pascal para determinar se um número inteiro A é divisível por um outro número inteiro B.
Esses valores devem ser fornecidos pelo usuário."""
a = int(input())
b = int(input())

if a%b == 0:
    print("sim")
else:
    print("nao")