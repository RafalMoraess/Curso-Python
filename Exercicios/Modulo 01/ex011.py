largura = float(input('Digite em metros a largura da parede: '))
altura = float(input('Digite em  metros a altura da parede: '))
aria = largura*altura
litro = aria/2
print('A largura é de {}m e a altura é de {}m a aria será de {}m²'.format(largura, altura, aria))
print('Se a aria é de {}m² a quantidade de litros de tinta será {}litros'.format(aria, litro))