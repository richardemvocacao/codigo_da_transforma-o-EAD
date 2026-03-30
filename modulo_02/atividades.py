import datetime

# Passo 1: Pedir o nome do usuário
nome = input("Qual é o seu nome? ")

# Passo 2 (Desafio Extra): Obter a hora atual do sistema
agora = datetime.datetime.now()
hora_formatada = agora.strftime("%H:%M:%S")

# Passo 3: Exibir a mensagem personalizada com a hora
print(f"Olá, {nome}! Seja bem-vindo(a).")
print(f"Agora são exatamente: {hora_formatada}")