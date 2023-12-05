"""Sabe-se que um número da forma n³ é igual a soma de números ímpares consecutivos.
Faça um programa em Pascal que leia um número inteiro positivo 
E imprima os ímpares consecutivos cuja soma é igual a n³ para n assumindo valores de 1 a M."""
m = int(input("Digite m: "))
n = 1
while n <= m:
    inicial = 1
    soma = 0
    while soma != n*n*n:
        soma = 0
        i = 1
        while i <= n:
            soma += inicial + (i-1)*2
            i += 1
        inicial += 2
    inicial -= 2
    print(inicial, end=" ")
    i = 2
    while i <= n:
        print(inicial + (i-1)*2, end=" ")
        i += 1
    print()
    n += 1
