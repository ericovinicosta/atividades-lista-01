"""
    16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
cobertura_por_litro = 3
lata = 18
valor_lata = 80


tamanho_area = float(input('Informe a area em m²: '))
quantidade_de_tinta = tamanho_area // cobertura_por_litro

if quantidade_de_tinta > 0 and quantidade_de_tinta % lata == 0:
    quantidade_lata = quantidade_de_tinta // lata
else:
    quantidade_lata = (quantidade_de_tinta // lata) + 1

relatorio = f"""
    Quantidade de latas: {int(quantidade_lata):3d}
    Valor: R$ {(quantidade_lata*valor_lata):8.2f}
"""

print(relatorio)