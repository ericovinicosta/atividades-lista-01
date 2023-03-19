"""
 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
tamanho_do_download = float(input('Informe o tamanho, em MB, do Download: '))
velocidade_download = float(input('Informe a velocidade, em Mbps, do Download: '))

tempo_download =( tamanho_do_download / velocidade_download ) * 60

print(f'O tempo é de aproximadamente {tempo_download:.0f} minutos')
