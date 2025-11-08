# variavel
nome = 'João'
idade = 30
altura = 1.75
print(f'Nome: {nome}, Idade: {idade}, Altura: {altura}')
print()

# constante
TAXA_JUROS = 3.4  # taxa percentual (%)
valor = 5  # valor base
valor_juros = (TAXA_JUROS / 100) * valor  # converte para decimal e aplica

print(f'A taxa de juros de {TAXA_JUROS}% aplicada sobre R${valor} resulta em R${valor_juros:.2f} de juros.')
print()

# Juros simples
TAXA_JUROS = 3.4  # ao mês
valor = 1000      # capital
meses = 6         # tempo

# cálculo
valor_juros = valor * (TAXA_JUROS / 100) * meses
valor_total = valor + valor_juros

print(f'Em {meses} meses, a {TAXA_JUROS}% ao mês, os juros serão R${valor_juros:.2f}.')
print(f'Valor total a pagar: R${valor_total:.2f}')
print()

# Juros compostos mensais
TAXA_JUROS = 3.4  # ao mês
valor = 1000      # capital
meses = 6

# cálculo
valor_total = valor * (1 + TAXA_JUROS / 100) ** meses
valor_juros = valor_total - valor

print(f'Em {meses} meses, a {TAXA_JUROS}% ao mês, os juros compostos serão R${valor_juros:.2f}.')
print(f'Valor total a pagar: R${valor_total:.2f}')
print()

# Juros simples em dias
TAXA_JUROS_MENSAL = 3.4  # % ao mês
valor = 1000
dias = 10

# converte a taxa mensal para diária
taxa_dia = TAXA_JUROS_MENSAL / 30  

# calcula os juros
valor_juros = valor * (taxa_dia / 100) * dias
valor_total = valor + valor_juros

print(f'Em {dias} dias, a {TAXA_JUROS_MENSAL}% ao mês (~{taxa_dia:.4f}% ao dia),')
print(f'os juros serão R${valor_juros:.2f} e o total R${valor_total:.2f}.')
