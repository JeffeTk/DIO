# Leitura das listas de clientes de cada projeto
linha1 = input().strip()
linha2 = input().strip()

# TODO: Converta cada linha em um conjunto de nomes, garantindo que listas vazias resultem em conjuntos vazios
# Dica: Use split() para separar os nomes e set() para eliminar duplicatas

# clientes_projeto1 = ...
# clientes_projeto2 = ...

clientes_projeto1 = set(linha1.split())
clientes_projeto2 = set(linha2.split())
 
# Identificação dos nomes exclusivos usando a operação de diferença simétrica
exclusivos = clientes_projeto1.symmetric_difference(clientes_projeto2)

# Impressão dos nomes exclusivos em ordem alfabética, ou "Nenhum" se não houver
if exclusivos:
    print(' '.join(sorted(exclusivos)))
else:
    print("Nenhum")