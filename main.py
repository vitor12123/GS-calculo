# Gostariamos de lembrar que trabalhamos com o numero hipotetico de alagamento de 2 metros
# Agradecemos a compreenção!

nivelRio = float(input('Digite o nivel do rio?(em metros): '))
Chuva = int(input('Esta chovendo?(1-sim/0-nao/2-vai chover): '))

if Chuva == 1: 
    quanto = input('Classifique a chuva(forte, media ou fraca): ')
    filtro = quanto.lower()
    if 'fraca' in filtro and nivelRio < 1.5 or 'media' in filtro and nivelRio < 1.5: 
        print('Por enquanto nem um perigo, mas fique esperto se a chuva aumentar!')
    elif 'media' in filtro and 1.7> nivelRio > 1.5 or 'forte' in filtro and 1.5 < nivelRio < 1.85:
        print('O nivel do rio esta subindo, sem problemas aparetes, mas iremos alertar a defesa civil')
    elif 'forte' in filtro and nivelRio > 1.85: 
        print('Uma possivel enchente pode ocorrer, estamos alertando a defesa civil imediatamente!')
    else: 
        print('O nivel do rio esta subindo, sem problemas aparetes, mas iremos alertar a defesa civil')

if Chuva == 2 : 
    previsao = float(input('Qual a previsão de chuva?(em mm): '))
    if previsao < 15 and nivelRio <= 1.5 :
        print('Por enquanto nem um perigo, mas fique esperto se a chuva aumentar!')
    elif 10 < previsao < 15 and 1.8> nivelRio > 1.5:
        print('O nivel do rio esta subindo, sem problemas aparetes, mas iremos alertar a defesa civil')
    elif previsao >= 10 and nivelRio > 1.9: 
        print('Uma possivel enchente pode ocorrer, estamos alertando a defesa civil imediatamente!') 
    elif previsao < 10 :
        print('Por enquanto nem um perigo, mas fique esperto se a chuva aumentar!')
    elif previsao > 15 and nivelRio >1.8: 
        print('Uma possivel enchente pode ocorrer, estamos alertando a defesa civil imediatamente!')
    elif previsao > 15 and nivelRio < 1.8: 
        print('O nivel do rio esta subindo, sem problemas aparetes, mas iremos alertar a defesa civil')

if Chuva == 0: 
    if nivelRio < 1.5 :
        print('Por enquanto nem um perigo!')
    elif 1.5 < nivelRio < 1.85 : 
        print('O nivel do rio esta subindo, mas sem problemas aparetes')
    else :
        print('Uma possivel enchente pode ocorrer, estamos alertando a defesa civil imediatamente!') 

