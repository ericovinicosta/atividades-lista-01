"""
14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""
limite = 50.0
valor_multa = 4

peso_informado = float(input('Informe o peso dos peixes:'))

excesso_de_peixe = peso_informado - limite

print(f'Quantidade informada: {peso_informado:.2f}')
print(f'Quantidade de excesso: {excesso_de_peixe:.2f}'
      if excesso_de_peixe > 0 else 0)

if excesso_de_peixe > 0:
	multa = excesso_de_peixe * valor_multa
	print(f'Valor da multa: {multa:.2f}')
else:
	print('Nao ha multa')
