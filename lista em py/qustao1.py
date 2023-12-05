"""Uma P.A. (progressão aritmética) é determinada pela sua razão (r) e pelo pri- meiro termo (a1).
Faça um programa em Pascal que seja capaz de determinar o enésimo (n) termo (a,,) de uma P.A., dado a razão (r) e o primeiro termo (a₁).
Seu programa deve ler n, r, a, do teclado e imprimir a...
 ana1+(n-1) × г."""
n = int(input("enézimo termo: " ))
r = int(input("razão da sequência:" ))
a1 = int(input("primeiro termo:" )) 

an = a1 +(n-1)* r
print(an)