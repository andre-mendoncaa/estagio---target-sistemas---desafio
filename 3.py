# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

arquivo = 'faturamentomensal.json'

with open(arquivo, 'r') as f:
    dados_faturamento = json.load(f)


soma_faturamento = 0
dias_com_faturamento = 0

for dia in dados_faturamento:
    if dia["valor"] > 0:
        soma_faturamento += dia["valor"]
        dias_com_faturamento += 1

if dias_com_faturamento > 0:
    media_faturamento = soma_faturamento / dias_com_faturamento
    print(f"Média de faturamento: {media_faturamento:.2f}")
else:
    print("Não houve dias com faturamento.")

