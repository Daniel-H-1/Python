sim = str ('sim')
não = str ('não')
total_de_acertos = int ('0')

print ('Prova de 5 perguntas, sendo necessáro acertar quatro')

R1 = str (input ('Pergunta 1: Quando o farol está vermelho, você pode avançar com o carro? (sim ou não) '))

if R1 == não:
  print('Acertou! Vamos para a próxima pergunta.')
  total_de_acertos += 1
else:
    print('Errou, pesquise o assunto!')


R2 = str (input ('Pergunta 2: Quando o farol está amarelo, você deve acelerar o carro para passar? (sim ou não) '))

if R2 == não:
    print('Acertou! Vamos para a próxima pergunta.')
    total_de_acertos += 1
else:
    print('Errou, pesquise o assunto!')


R3 = str (input ('Pergunta 3: Se o farol está verde e não há pedrestre atravessando, você pode avançar? (sim ou não) '))

if R3 == sim:
  print('Acertou! Vamos para a próxima pergunta. ')
  total_de_acertos += 1
else:
    print('Errou, pesquise o assunto!')


R4 = str (input ('Pergunta 4: Se o farol está verde e há pedrestre atravessando, você pode avançar? (sim ou não) '))

if R4 == não:
  print('Acertou! Vamos para a próxima pergunta. ')
  total_de_acertos += 1
else:
    print('Errou, pesquise o assunto!')

R5 = str (input ('Pergunta 5: Se o farol está vermelho, você deve parar o carro? (sim ou não) '))

if R5 == sim:
  print('Acertou! Vamos para a próxima perguta. ')
  total_de_acertos += 1
else:
    print('Errou, pesquise o assunto!')

if total_de_acertos >= 4:
  print('Parabéns você conhece as leis de transito e acertou',total_de_acertos);
else:
  print('Você não passou no teste, você acertou apenas', total_de_acertos)

print('fim.')
