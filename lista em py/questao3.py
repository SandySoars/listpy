"""Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo desconto aos clientes. 
Faça um programa em Pascal que possa entrar com o valor de um produto e imprima o novo valor tendo em vista. que o desconto foi de 9%. 
Além disso, imprima o valor do desconto."""
preço = float(input('qual é o preço do produto? R$'))
novo = preço - (preço * 9 / 100)
desconto = preço - novo
print("O valor final do produto será de: R${:.2f}, e o valor de desconto será R${:.2f}.".format(novo,desconto))
