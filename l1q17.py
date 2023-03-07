import math

tamanho_area = float(input('Qual o tamanho da area em metros quadrados? '))

lata = 18 * 6
galao = 3.6 * 6

print(f'A área {tamanho_area} precisa de:')
print(f'\t {math.ceil(tamanho_area/lata)} latas \t = {math.ceil(tamanho_area/lata)*80}')

print(f'\t {math.ceil(tamanho_area/galao)} galoes \t = {math.ceil(tamanho_area/galao)*25}')