# Leitura dos três valores inteiros em uma única linha
entrada = input()
valor_transacao, taxa_servico, pagamento_minimo = map(int, entrada.split())

# TODO: Calcule o valor final da transação subtraindo a taxa do valor
valor_final = valor_transacao - taxa_servico

# Verifique se o valor final é suficiente para aprovar a transação
if valor_final >= pagamento_minimo:
    print("Aprovada")
else:
    print("Recusada")
