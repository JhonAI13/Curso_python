def	cria_conta(numero,	titular,	saldo,	limite):
	"""cria uma conta

	Args:
		numero (_type_): numero de identificação da conta
		titular (_type_): nome do titular
		saldo (_type_): quantidade de dinhiro que tem na conta
		limite (_type_): _description_
	"""
	conta	=	{"numero":	numero,	"titular":	titular,	"saldo":	saldo,	"limite":	limite}
	return	conta

def	deposita(conta,	valor):
	"""Soma um valor a conta

	Args:
		conta (_type_): numero da conta
		valor (_type_): quantidade a ser somada a conta
	"""
	conta['saldo']	+=	valor

def	saca(conta,	valor):
	"""subtrai o valor da conta.

	Args:
		conta (_type_): A conta cadastrada
		valor (_type_): O valor a ser sacado
	"""
	conta['saldo']	-=	valor

def	extrato(conta):
	"""Dis quanto tem na conta

	Args:
		conta (_type_): numero da conta
	"""
	print("numero: {} \nsaldo: {}".format(conta['numero'],	conta['saldo']))
help(saca)