"""
    15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
        ◦ salário bruto.
        ◦ quanto pagou ao INSS.
        ◦ quanto pagou ao sindicato.
        ◦ o salário líquido.
        ◦ calcule os descontos e o salário líquido, conforme a tabela abaixo:
          + Salário Bruto : R$
          - IR (11%) : R$
          - INSS (8%) : R$
          - Sindicato ( 5%) : R$
          = Salário Liquido : R$
          Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
irpf = 0.11
inss = 0.08
sindicato = 0.05

valor_por_hora = float(input('Informe quanto recebe por hora de trabalho: '))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas: '))

salario_bruto = valor_por_hora * horas_trabalhadas

pagou_inss = salario_bruto * inss
pagou_irpf = salario_bruto * irpf
pagou_sindicato = salario_bruto * sindicato

relatorio = f"""
    + Salário Bruto : R$ {salario_bruto:.2f}
    - IR ({irpf*100:.0f}%) : R$ {pagou_irpf:.2f}
    - INSS ({inss*100:.0f}%) : R$ {pagou_inss:.2f}
    - Sindicato ( {sindicato*100:.0f}%) : R$ {pagou_sindicato:.2f}
    = Salário Liquido : R$ {salario_bruto-(pagou_irpf+pagou_inss+pagou_sindicato):.2f}
"""

print(relatorio)