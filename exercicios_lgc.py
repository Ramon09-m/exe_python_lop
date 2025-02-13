altura = int(input('Coloque sua altura (Ex: 160): '))/100
peso = int(input('Coloque seu peso: '))

calcular_IMC = peso/(altura*altura)

if calcular_IMC < 18:
  print('Seu IMC é', calcular_IMC, 'Sua classificação é magreza')
elif calcular_IMC >=18 and calcular_IMC <= 24.9:
  print('Seu IMC é', calcular_IMC, 'Sua classificação é Saudável')
elif calcular_IMC >=25 and calcular_IMC <= 29.9:
  print('Seu IMC é', calcular_IMC, 'Sua classificação é Sobrepeso')
elif calcular_IMC > 30:
  print('Seu IMC é', calcular_IMC, 'Sua classificação é Obesidade')