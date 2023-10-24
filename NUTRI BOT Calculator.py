print('  Olá! Sou o NUTRI BOT e vamos calcular algumas métricas importantes para seu processo de emagrecimento! \n  Vou precisar de algumas informações para isso, ok?')

Nome = str(input(' Qual é o seu nome? '))
Genero = ''
while True:
    Genero = input('1º - Voce é um homem ou uma mulher? ')
    
    if Genero.capitalize() == 'Homem':
        print('Certo, então você é um homem')
        break
    if Genero.capitalize() == 'Mulher':
        print('Certo, então você é uma mulher')
        break            
    else:
        print('Não entendi, você é um homem ou uma mulher?')
        continue

if Genero == 'homem':
    Genero_Classified = 'Masculino'
else: # Genero == 'mulher'
    Genero_Classified = 'Feminino'    
    
Idade = int(input("2º - Qual a sua idade? (em anos) "))
Altura = int(input("3º - Qual a sua altura? (em cm) "))
Peso = float(input("4º - Qual o seu peso? (em kg) "))
IMC = round((Peso/((Altura/100)**2)), 2)

## IMC_Classified condition:
if IMC <= 16.9:
    IMC_Classified = str(IMC) + ' - "Muito abaixo do peso"'
if IMC >= 17 and IMC <= 18.4:
    IMC_Classified = str(IMC) + ' - "Abaixo do peso"'
if IMC >= 18.5 and IMC <= 24.9:
    IMC_Classified = str(IMC) + ' - "Peso Normal"'
if IMC >= 25 and IMC <= 29.9:
    IMC_Classified = str(IMC) + ' - "Sobrepeso"'
if IMC >= 30 and IMC <= 34.9:
    IMC_Classified = str(IMC) + ' - "Obesidade grau I"'
if IMC >= 35 and IMC <= 39.9:
    IMC_Classified = str(IMC) + ' - "Obesidade grau II"'
if IMC >= 40:
    IMC_Classified = str(IMC) + ' - "Obesidade grau III"'

## TMB calc:
if Genero.capitalize() == "Homem":
    TMB = 88.362 + (13.397 * Peso) + (4.799 * Altura) - (5.677 * Idade)
if Genero.capitalize() == "Mulher":
    TMB = 655 + (9.6 * Peso) + (1.8 * Altura) - (4.7 * Idade)

## Atividade Física Laboral - Sedentario ("Office Work") x Trabalho Ativo:
Sedentario = ''
while True:
    Sedentario = input('5º - Atividade Laboral: Você passa a maior parte do tempo sentado durante o dia ("trabalho de escritório")? ')
    
    if Sedentario.capitalize() == 'Sim':
        print('Certo, então você é um sedentário')
        break
    if Sedentario.capitalize() == 'Nao':
        print('Certo, você é uma pessoa bastante ativa...')
        break               
    else:
        print('Não entendi...')
        continue

## Atividade Física Não Laboral:
Fator_Atividade = ''
while True:
    Fator_Atividade = input('6º - Atividades Física: Você pratica algum treino de força ao menos 3x na semana? ')

    if Fator_Atividade == 'sim':
        print('Legal, então você é um atleta!')
        break
    if Fator_Atividade == 'nao':
        print('Entendi, que pena...')
        break            
    else:
        print('Não entendi...')
        continue

## Multiplicador Atividade, esquema combinatório entre Atividade Física Laboral e Atividade Física Não Laboral:
if Sedentario == 'sim' and Fator_Atividade == 'nao':
    TDEE = TMB * 1.15
elif Sedentario == 'sim' and Fator_Atividade == 'sim':
    TDEE = TMB * 1.35
elif Sedentario == 'nao' and Fator_Atividade == 'nao':
    TDEE = TMB * 1.35
else: #Sedentario == 'nao' and Fator_Atividade == 'sim'
    TDEE = TMB * 1.55

## Definidor de Objetivo automatico baseado em IMC, input necessário em caso de Peso Normal:
if IMC < 18.5:
    Objetivo = 'BULK1'     
elif IMC > 24.9:
    Objetivo = 'CUT'
else: # IMC >= 18.5 and IMC <= 24.9
    Objetivo_Desejo = ''
    while True:
        Objetivo_Desejo = input('7º - Você precisa perder gordura corporal? ')
        if Objetivo_Desejo == 'sim':
            Objetivo = 'CUT'
            break
        if Objetivo_Desejo == 'nao':
            Objetivo = 'BULK2'
            break
        else:
            print('Não entendi...')
            continue

## Target daily calorie intake (TDCI) = TDEE – (Bodyweight x target weekly fat loss rate x 500*)
if Objetivo == 'CUT':
    TDCI = TDEE - (Peso * 0.0075 * 1100)
## Target daily calorie intake (TDCI) = TDEE + (Bodyweight x target monthly gain rate x 330*)
elif Objetivo == 'BULK1':
    TDCI = TDEE + (Peso * 0.02 * 330)
## BULK2 - Avaliar Experiencia de Treino
elif Objetivo == 'BULK2':
    Exp_Treino = ''
    while True:
        Exp_Treino = input('8º - Níveis de Experiência de Treino: \n * Iniciante (totalmente novo à treinos de força) \n * Novato (aumenta os pesos dos exercícios todas as semanas) \n * Intermediário (aumenta os pesos dos exercícios todos os meses) \n * Avançado (raramente aumenta os pesos dos exercícios) \n Qual das opções acima melhor te descreve quanto à experiência de treino?: ')
    
        if Exp_Treino == 'iniciante':
            Exp_Treino_multiplicador = 0.02
            break
        if Exp_Treino == 'novato':
            Exp_Treino_multiplicador = 0.015
            break
        if Exp_Treino == 'intermediario':
            Exp_Treino_multiplicador = 0.01
            break
        if Exp_Treino == 'avancado':
            Exp_Treino_multiplicador = 0.005
            break
        else:
            print('Não entendi...')
            continue
    TDCI = TDEE + (Peso * Exp_Treino_multiplicador * 330)         
# Objetivo_Classified condition:
if Objetivo == 'CUT':
    Objetivo_Classified = 'Perda de Peso / Emagrecimento'
elif Objetivo == 'BULK1':
    Objetivo_Classified = 'Ganho de Peso / Massa Muscular'
else: #Objetivo = BULK2    
    if Exp_Treino == 'novato':
        Objetivo_Classified = 'Ganho de Peso / Massa Muscular - Bulking - Novato'
    elif Exp_Treino == 'iniciante':
        Objetivo_Classified = 'Ganho de Peso / Massa Muscular - Bulking - Iniciante'
    elif Exp_Treino == 'intermediario':
        Objetivo_Classified = 'Ganho de Peso / Massa Muscular - Bulking - Intermediário'
    else: # Exp_Treino == 'avancado':
        Objetivo_Classified = 'Ganho de Peso / Massa Muscular - Bulking - Avançado'
## PTN calculation:
if Objetivo == 'CUT':
    PTN = str(round(Peso * 2.2)) + '-' + str(round(Peso * 2.6)) + 'g/dia'
else:
    PTN = str(round(Peso * 1.6)) + '-' + str(round(Peso * 2.2)) + 'g/dia'
        
### RELATORIO FINAL!    
print('*****RELATORIO FINAL - NUTRI BOT: \n \n ***INFORMAÇÕES CADASTRADAS: \n **Nome: ', Nome, '\n **Genero: ', Genero_Classified, '\n **Idade: ', Idade, '\n **Altura: ', Altura/100, 'm \n **Peso: ', Peso, 'kg \n \n **IMC: ', IMC_Classified,'\n **OBJETIVO: ', Objetivo_Classified, ' \n \n ***CALCULOS NUTRICIONAIS: \n **TMB: ', round(TMB), 'kcal \n **TDEE: ', round(TDEE), 'kcal \n **TDCI: ', round(TDCI), 'kcal \n **PTN: ', PTN)