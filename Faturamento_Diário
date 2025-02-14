faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
# Considerando sábados e domingos como datas sem faturamento, portanto ignorados nos dias úteis para não afetar cálculo da média
dias_uteis = 22

faturamento_diario = []

for estado, total in faturamento_mensal.items():
    faturamento_diario.extend([total / dias_uteis] * dias_uteis)

def menor_faturamento(faturamento_diario):
    return min(faturamento_diario)

def maior_faturamento(faturamento_diario):
    return max(faturamento_diario)

def media_mensal(faturamento_diario):
    if len(faturamento_diario) > 0:
        return sum(faturamento_diario) / len(faturamento_diario)
    else:
        return 0

def dias_superiores_a_media(faturamento_diario, media):
    return len([valor for valor in faturamento_diario if valor > media])

menor = menor_faturamento(faturamento_diario)
maior = maior_faturamento(faturamento_diario)
media = media_mensal(faturamento_diario)
dias_acima_media = dias_superiores_a_media(faturamento_diario, media)

print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Número de dias com faturamento superior à média: {dias_acima_media} dias")
