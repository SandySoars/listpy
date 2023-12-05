"""Faça um programa em Pascal que leia uma sequência de 10 números e os ar- mazene em um vetor de 10 posições.
Em seguida imprima a lista de números repetidos no vetor. Use ao máximo funções e procedimentos adequados."""
def ler_vetor():
  vetor = [] 
  for i in range(10): 
    numero = int(input("Digite um número: ")) 
    vetor.append(numero)
  return vetor 

def imprimir_repetidos(vetor):
  repetidos = [] 
  for i in range(len(vetor)): 
    numero = vetor[i] 
    if numero in vetor[i+1:]:
      if numero not in repetidos: 
        repetidos.append(numero)
  print("Os números repetidos no vetor são:", repetidos) 

vetor = ler_vetor() 
imprimir_repetidos(vetor) 
