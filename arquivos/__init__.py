def linha(tam = 42):
	print('='* tam)


def cadastro(arq, pontos):
	try:
		o = open(arq, 'at')
	except:
		print('ERRO AO ABRIR LOGIN E SENHA.')
	else:
		try:
			o.write(f'{pontos}')
		except:
			print('ERRO ao ESCREVER NO ARQUIVO O USUARIO E SENHA')
		finally:
			o.close()


def limpar(arq):
	o = open(arq, 'w').close()


def guardardados(arq, lista):
	o = open(arq, 'rt')
	for f in o.readlines():
		inteiro = int(f)
		lista.append(inteiro)
	o.close()