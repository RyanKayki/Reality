import os

# Participantes
PESSOAS = (1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1210, 1211, 1212)   # Tupla
NOMES = ("Mari", "Lino", "Belinha", "Alexa", "Jaque", "Bob", "Pimpo", "Kitto", "Alfenas", "Juca", "Rita", "Chico")  # Tupla
saldo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Lista

# Função para adicionar o saldo
def adicao_saldo(codigo, valor):
    try:
        if codigo in saldo:
            saldo[codigo] += valor
            print(f"Saldo de {NOMES[codigo]} atualizado para {saldo[codigo]} estrelas.")
        else:
            print("Código de participante inválido.")
    except Exception as e:
        print("Ocorreu um erro ao adicionar saldo:", str(e))

# Níveis de punição
def punicao(codigo, nivel):
    try:
        if codigo in saldo:
            nome_pessoa = NOMES[codigo]


            if saldo[codigo] < 0:
                saldo[codigo] = 0 

            if nivel == "leve":
                saldo[codigo] -= 50

            elif nivel == "relevante":
                saldo[codigo] -= 100

            elif nivel == "grave":
                saldo[codigo] -= 200
            

            print(f"{nome_pessoa} levou uma punição {nivel}. Seu saldo atual é: {saldo[codigo]} estrelas.")
        else:
            print("Código de participante inválido.")
    except Exception as e:
        print("Ocorreu um erro ao aplicar punição:", str(e))

# Função para consultar o saldo
def consultar_saldo(codigo):
    try:
        if codigo in saldo:
            print(f"Saldo de {NOMES[codigo]}: {saldo[codigo]} estrelas.")
        else:
            print("Código de participante inválido.")
    except Exception as e:
        print("Ocorreu um erro ao consultar saldo:", str(e))

# Função para listar os saldos
def listar_saldos():
    try:
        print("Lista de saldos:")
        for i in range(len(PESSOAS)):
            print(f"{NOMES[i]}: {saldo[i]} estrelas.")
    except Exception as e:
        print("Ocorreu um erro ao listar saldos:", str(e))

#repetição placar
while True:
    try:
        os.system('cls')
        print("BEM VINDO ao Reality Show dos Grandes Irmãos\n 1 - Adicionar Saldos\n 2 - Punições\n 3 - Ver Saldo individual\n 4 - Listar Todos Os Saldos\n 0 - Exit")

        alternativas = int(input("Por favor, insira em qual setor deseja entrar: "))

#alternativas
        
        if alternativas == 1:
            codigo_pessoa = int(input("insira o código do participante: "))
            valor_adicao = int(input("insira o valor a ser adicionado: "))
            adicao_saldo(codigo_pessoa, valor_adicao)

        elif alternativas == 2:
            codigo_pessoa = int(input("Insira o código do participante: "))
            nivel_punicao = input("Insira o nível da punição (leve/relevante/grave): ")
            punicao(codigo_pessoa, nivel_punicao)

        elif alternativas == 3:
            codigo_pessoa = int(input("Insira o código do participante: "))
            consultar_saldo(codigo_pessoa)

        elif alternativas == 4:
            listar_saldos()

        elif alternativas == 0:
            break

        again = input("\n Deseja fazer outra consulta? (s/n): ")
        if again.lower() == 's':
            continue
        else:
            break

    except Exception as e:
        print(f"Ocorreu um erro: {e}")