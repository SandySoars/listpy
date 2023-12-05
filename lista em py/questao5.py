"""Faça um programa em Pascal para determinar se um número inteiro A é divisível por um outro número inteiro B. 
Esses valores devem ser fornecidos pelo usuário."""
primeiro = float(input())
segundo = float(input())

quadrado = min(primeiro, segundo)*min(primeiro,segundo)
raiz = max(primeiro, segundo)**(1/2)

print("{:.2f} {:.2f}".format(quadrado,raiz))
