'''
PEDRA PAPEL TESOURA COM PONTOS V1.2
-----DEV: Leandro Furtado

JOGO PEDRA PAPEL TESOURA COM SISTEMA DE SAVE
DE PONTOS! VOCÊ PERDE 7 PONTOS SE PERDER
E GANHA 10 AO VENCER, 2 AO EMPATAR. COM ISSO 
TODO A SUA QUANTIDADE DE PONTOS SERÁ SALVA EM 
UM ARQUIVO TXT.

AO INICIAR O PROGRAMA A QUANTIDADE DE PONTOS
SERÁ PASSADO PARA UMA LISTA E DEPOIS PARA 
A SOMA DE PONTOS ATUAL, DEPOIS O PROGRAMA IRÁ
LIMPAR O ARQUIVO TXT E ADICIONAR A NOVA PONTUAÇÃO,
REPETINDO ESSE MESMO PROCESSO NA PRÓXIMA VEZ QUE INICIA-LO.
'''

from time import sleep
from datetime import date
from arquivos import *
from random import randint

arq = 'logins.txt'
pontuation = []
dadosrapido = []

guardardados(arq, pontuation)
for c in pontuation:
	dadosrapido.append(c)
dadosrapido.append(0)
print('\033[1;32m')
linha()
data = date.today()
formatando_data = (f'{data.day}/{data.month}/{data.year}')
print(f'\033[1;32m      BEM-VINDO! Hoje é: {formatando_data}!')
print(f'\033[1;32m      SEUS PONTOS: [   {dadosrapido[0]}   ]')
linha()
while True:
	print('\n\033[1;32m[P] --- > PAPEL')
	print('[T] --- > TESOURA')
	print('[A] --- > PEDRA')
	print('[S] --- > [SAIR DO PROGRAMA e SALVAR]\033[1;97m')
	option = str(input('\033[1;91mDigite sua opção: \033[1;97m'))
	if option in 'Pp':
		bot = randint(0,2)
		if bot == 2:
			print('\033[1;93mVocê jogou PAPEL e o adversário jogou PEDRA!')
			print('\033[1;32mPARABÉNS VOCÊ VENCEU! [+10 PONTOS]\033[1;97m')
			dadosrapido.append(10)
		if bot == 1:
			print('\033[1;93mVocê jogou PAPEL e o adversário jogou TESOURA!')
			print('\033[1;31mVOCÊ PERDEU! [-7 PONTOS]\033[1;97m')
			dadosrapido.append(-7)
		if bot == 0:
			print('\033[1;93mVocê jogou PAPEL e o adversário jogou PAPEL!')
			print('\033[1;34mEMPATE! [+2 PONTOS]\033[1;97m')
			dadosrapido.append(2)


	elif option in 'Tt':
		bot = randint(0,2)
		if bot == 2:
			print('\033[1;93mVocê jogou TESOURA e o adversário jogou PEDRA!')
			print('\033[1;31mVOCÊ PERDEU! [-7 PONTOS]')
			dadosrapido.append(-7)
		if bot == 1:
			print('\033[1;93mVocê jogou TESOURA e o adversário jogou TESOURA!')
			print('\033[1;34mEMPATE! [+2 PONTOS]')
			dadosrapido.append(2)
		if bot == 0:
			print('\033[1;93mVocê jogou TESOURA e o adversário jogou PAPEL!')
			print('\033[1;32mVOCÊ VENCEU PARABÉNS!! [+10 PONTOS]')
			dadosrapido.append(10)
		

	elif option in 'Aa':
		bot = randint(0,2)
		if bot == 2:
			print('\033[1;93mVocê jogou PEDRA e o adversário jogou PEDRA!')
			print('\033[1;34mEMPATE! [+2 PONTOS]')
			dadosrapido.append(2)
		if bot == 1:
			print('\033[1;93mVocê jogou PEDRA e o adversário jogou TESOURA!')
			print('\033[1;32mVOCÊ GANHOU :)! [+10 PONTOS]')
			dadosrapido.append(10)
		if bot == 0:
			print('\033[1;93mVocê jogou PEDRA e o adversário jogou PAPEL!')
			print('\033[1;31mVOCê PERDEU! [-7 PONTOS]')
			dadosrapido.append(-7)
	elif option in 'Ss':
		dadosfinal = sum(dadosrapido)
		limpar(arq)
		cadastro(arq, dadosfinal)
		print('FECHANDO O PROGRAMA E SALVANDO...')
		sleep(0.3)
		print('.')
		sleep(0.3)
		print('.')
		sleep(0.3)
		print('.')
		sleep(0.4)
		print('SALVO!')
		break