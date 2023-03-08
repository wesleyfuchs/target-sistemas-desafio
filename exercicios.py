print('Sequencia de Fibonacci')
def verifica_fibonacci(n):
    a = 0
    b = 1
    while b < n:
        a, b = b, a+b
    if b == n:
        return "{} pertence à sequência de Fibonacci".format(n)
    else:
        return "{} não pertence à sequência de Fibonacci".format(n)

print(verifica_fibonacci(13))  # Output: 13 pertence à sequência de Fibonacci
print(verifica_fibonacci(14))  # Output: 14 não pertence à sequência de Fibonacci

# Recebendo um numero do teclado
# numero_teclado = int(input('Insira o numero a ser testado: '))
# print(verifica_fibonacci(numero_teclado))

print('')
print( 'Faturamento diário de uma distribuidora')

import json

with open('dados.json') as file:
    dados = json.load(file)

# Encontra o menor e o maior valor de faturamento do mês
valores = [dia['valor'] for dia in dados]
menor_valor = min(valores)
maior_valor = max(valores)

# Calcula a média mensal, ignorando dias sem faturamento
valores_validos = [valor for valor in valores if valor > 0]
media = sum(valores_validos) / len(valores_validos)

# Encontra o número de dias em que o faturamento foi superior à média
dias_acima_da_media = len([valor for valor in valores_validos if valor > media])

# Exibe os resultados
print(f"Menor valor de faturamento do mês: R${menor_valor:.2f}")
print(f"Maior valor de faturamento do mês: R${maior_valor:.2f}")
print(f"Número de dias em que o faturamento foi superior à média: {dias_acima_da_media}")


print('')
print('faturamento mensal de uma distribuidora')

faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento_por_estado.values())

for estado, faturamento in faturamento_por_estado.items():
    percentual = faturamento / total * 100
    print(f"{estado}: {percentual:.2f}%")

print('')
print('Inverter uma string')
texto = input("Digite uma string para ser invertida: ")

texto_invertido = texto[::-1]

print(f"A string invertida é: {texto_invertido}")
