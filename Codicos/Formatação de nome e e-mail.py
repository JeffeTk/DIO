def formatar_nome(nome):
    # Retorna o nome com a primeira letra de cada palavra em maiúsculo
    return ' '.join(palavra.capitalize() for palavra in nome.strip().split())

def validar_email(email):
    # TODO: Verifique se o e-mail contém exatamente um '@' e pelo menos um '.' após o '@'
    # Dica: Use métodos de string para contar e dividir.
   
    if email.count('@') != 1:
        return False
    
    usuario, dominio = email.split('@')
    
    if '.' not in dominio:
        return False
    
    return True

def processar_cadastro(entrada):
    # Divide a entrada em nome e email
    if ', ' not in entrada:
        return 'Entrada inválida - ERRO'
    nome, email = entrada.split(', ', 1)
    nome_formatado = formatar_nome(nome)
    if validar_email(email):
        return f"{nome_formatado} - OK"
    else:
        return f"{nome_formatado} - ERRO"

# Entrada padrão
entrada = input()
print(processar_cadastro(entrada))