# Leitura da quantidade de livros cadastrados
n = int(input())

# Dicionário para armazenar o acervo: título -> código
acervo = {}

# Leitura dos pares título-código
for _ in range(n):
    linha = input().strip()
    # TODO: Separe o título e o código da linha e adicione ao dicionário 'acervo'
    # Dica: Use split() para separar e atribua corretamente no dicionário

    #separa a penas o último valor
    titulo, codigo = linha.rsplit(" ", 1)
    acervo[titulo] = codigo

# Leitura do título a ser consultado
consulta = input().strip()

# Busca pelo título no acervo e impressão do resultado
if consulta in acervo:
    print(acervo[consulta])
else:
    print("Livro nao encontrado")