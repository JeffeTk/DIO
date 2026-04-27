# Lê a entrada do usuário (nome do cliente)
entrada = input()

# Remove espaços extras no início/fim e divide a string em palavras
palavras = entrada.split()

# Capitalize cada palavra (primeira letra maiúscula, demais minúsculas)
palavras_formatadas = [palavras.capitalize() for palavras in palavras]

# Junta as palavras com um único espaço entre elas
nome_formatado = " ".join(palavras_formatadas)

# Exibe o nome formatado
print(nome_formatado)