from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from models import Pessoas, Atividades, Usuarios

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

''' Hardcode '''
# USUARIOS = {
	# 'rafael':'123',
	# 'muller': '321'
# }

# @auth.verify_password
# def verificacao(login, senha):
	# if not login, senha:
		# return False
	# return USUARIOS.get(login) == senha	
	
@auth.verify_password
def verificacao(login, senha):
	if not login, senha:
		return False
	return Usuarios.query.filter_by(login=login, senha=senha).first()


class Pessoa(Resource):
	# Consultar
	def get(self, nome):
		pessoa = Pessoas.query.filter_by(nome=nome).first()

		try:
			response = {
				"nome": pessoa.nome,
				"idade": pessoa.idade,
				"id": pessoa.id
			}
		except AttributeError:
			response = {
				"status": "erro",
				"mensagem": "Pessoa não encontrada"
			}
		return jsonify(response)

	# editar
	@auth.login_required
	def put(self, nome):
		pessoa = Pessoas.query.filter_by(nome=nome).first()
		dados = request.json
		if 'nome' in dados:
			pessoa.nome = dados['nome']
		if 'idade' in dados:
			pessoa.idade = dados['idade']
		pessoa.save()
		response = {
			'id': pessoa.id,
			'nome': pessoa.nome,
			'idade': pessoa.idade
		}
		return response

	def delete(self, nome):
		pessoa = Pessoas.query.filter_by(nome=nome).first()
		pessoa.delete()
		return {"status":"Sucesso", "mensagem": "Pessoa excluida com sucesso"}


class ListarPessoas(Resource):
	
	def get(self):
		pessoas = Pessoas.query.all()
		response = [{'id':x.id, 'nome':x.nome, 'idade':x.idade} for x in pessoas]
		return response
		
	def post(self):
		dados = request.json
		pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
		pessoa.save()
		response = {
			'id': pessoa.id,
			'nome': pessoa.nome,
			'idade': pessoa.idade
		}
		return response


class ListarAtividades(Resource):
	
	def get(self):
		atividades = Atividades.query.all()
		print(atividades)
		response = [{"id": x.id, "nome":x.nome, "pessoa": x.pessoa.nome} for x in atividades]
		return response
	
	
	def post(self):
		dados = request.json
		pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
		atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
		atividade.save()
		response = {
			"pessoa": atividade.pessoa.nome,
			"nome": atividade.nome,
			"id": atividade.id
		}
		return response
		
		
api.add_resource(Pessoa, "/pessoas/<string:nome>/")
api.add_resource(ListarPessoas, "/pessoas/")

api.add_resource(ListarAtividades, "/atividades/")

if __name__ == '__main__':
	app.run(debug=True)