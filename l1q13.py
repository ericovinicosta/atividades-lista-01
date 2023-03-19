"""
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    ◦ Para homens: (72.7*h) - 58
    ◦ Para mulheres: (62.1*h) - 44.7
"""
altura = float(input('Informe sua altura: '))

peso_ideal_m = (72.2*altura) - 58
peso_ideal_f = (62.1*altura) - 44.7

print('Peso Ideal para',f'Homens {peso_ideal_m:.2f} Kg', f'Mulheres {peso_ideal_f:.2f} Kg', sep='\n')