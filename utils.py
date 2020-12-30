from models import Pessoas, Usuarios

def insere_pessoas():
	pessoa = Pessoas(nome="Rafael", idade="26")
	pessoa.save()
	print(pessoa)
	

def consulta():
	#pessoa = Pessoas.query.filter_by(nome="Rafael").first()
	#print(pessoa.idade)
	pessoa = Pessoas.query.all()
	print(pessoa)

	
def altera_pessoa():
	# .first pega o primeiro registro com esse nome
	pessoa = Pessoas.query.filter_by(nome="Rafael").first()
	pessoa.idade = 21
	pessoa.save()
	
	
def excluir_pessoa():
	pessoa = Pessoas.query.filter_by(nome="Felipe").first()
	pessoa.delete()
	
	
def insere_usuario(login, senha):
	usuario = Usuarios(login=login, senha=senha)
	usuario.save()
	
def consultar_usuarios():
	usuario = Usuarios.query.all()
	print(usuarios)
	
if __name__ == '__main__':
	insere_usuario('rafael', '1234')
	#insere_pessoas()
	#altera_pessoa()
	#excluir_pessoa()
	consulta()