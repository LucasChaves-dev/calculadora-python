#Função para calcular velocidade média
def calcular_velocidade_media(distancia:float, tempo:float, unidade_medida="km/h"):
    if tempo == 0:
        return 0
    velocidade_media = distancia / tempo
    return f"{velocidade_media} {unidade_medida}"


#Função para converter a temperatura

def converter_temperatura(temperatura:float, unidade_medida="celsius"):
    if unidade_medida == "celsius":
        return temperatura * 1.8 + 32
    elif unidade_medida == "fahrenheit":
        return (temperatura - 32) / 1.8
    else:
        return 0

#Função para exibir um menu
def exibir_menu():
    print("Menu de Opções:")
    print("1 - Calcular Velocidade Média")
    print("2 - Converter Temperatura")
    print("3 - Sair")

#Função para chamar as outras funções
def aluno_de_fisica():
        op = 0
        while op != "3":
            exibir_menu()
            op = input("Escolha uma opção: ")
            if op == "1":
                distancia_percorrida = float(input("Digite a distância (em km): "))
                tempo_viagem = float(input("Digite o tempo (em horas): "))
                medida = input("Digite a unidade de medida (km/h, m/s): ")
                print(f" A vaelocidade média é {calcular_velocidade_media(distancia_percorrida, tempo_viagem, medida)}")   
            elif op == "2":
                temperatura_informada = float(input("Digite a temperatura: "))
                medida = input("Converter para (celsius, fahrenheit): ")
                print(f"e resultado de conversão é {converter_temperatura(temperatura_informada, medida)}")
            elif op == "3":
                print("Saindo...")
            else:
                print("Opção inválida. Tente novamente.")

aluno_de_fisica()