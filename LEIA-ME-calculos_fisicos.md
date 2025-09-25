Leia-me: Sistema de Cálculos Físicos
Descrição
Este é um programa em Python que oferece duas funcionalidades principais para cálculos físicos:

Cálculo de velocidade média

Conversão de temperatura entre Celsius e Fahrenheit
### Exemplo de uso

```
Funcionalidades
1. Cálculo de Velocidade Média
Calcula a velocidade média com base na distância percorrida e no tempo gasto

Suporta diferentes unidades de medida (km/h, m/s, etc.)

Trata casos onde o tempo é zero para evitar divisão por zero
```

---
2. Conversão de Temperatura
Converte temperaturas entre Celsius e Fahrenheit

Fórmula de Celsius para Fahrenheit: °F = (°C × 1.8) + 32

Fórmula de Fahrenheit para Celsius: °C = (°F - 32) / 1.8

Como Usar
Execução do Programa
bash
python nome_do_arquivo.py
Fluxo do Programa
O programa exibe um menu com 3 opções

Digite o número correspondente à opção desejada:

1: Calcular velocidade média

2: Converter temperatura

3: Sair do programa

Exemplo de Uso
Para Calcular Velocidade Média:
text
Menu de Opções:
1 - Calcular Velocidade Média
2 - Converter Temperatura
3 - Sair
Escolha uma opção: 1
Digite a distância (em km): 100
Digite o tempo (em horas): 2
Digite a unidade de medida (km/h, m/s): km/h
A velocidade média é 50.0 km/h
Para Converter Temperatura:
text
Menu de Opções:
1 - Calcular Velocidade Média
2 - Converter Temperatura
3 - Sair
Escolha uma opção: 2
Digite a temperatura: 25
Converter para (celsius, fahrenheit): fahrenheit
O resultado de conversão é 77.0
Estrutura do Código
Funções Principais
calcular_velocidade_media(distancia, tempo, unidade_medida)

distancia: distância percorrida (float)

tempo: tempo gasto (float)

unidade_medida: unidade de medida desejada (padrão: "km/h")

converter_temperatura(temperatura, unidade_medida)

temperatura: valor da temperatura (float)

unidade_medida: unidade para conversão (padrão: "celsius")

exibir_menu()

Exibe as opções disponíveis para o usuário

aluno_de_fisica()

Função principal que controla o fluxo do programa
---
Requisitos
Python 3.x

Observações
O programa trata entradas inválidas e exibe mensagens de erro apropriadas

O loop do menu continua até que o usuário escolha a opção de sair (3)

As funções são tipadas para melhor legibilidade do código





