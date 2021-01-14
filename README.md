# ex_flask_atividade
Exercício do curso de Flask da DIO, criação de API com Flask-RESTful e Flask-httpauth básico.<br/>

Objetivo:<br/>Estudo;<br/>

#### Ordem de execução:
models.py = cria o bando de dados; <br/>
utils.py = cria o usuário "rafael", senha "1234"; <br/>
app.py = servidos local, https:127.0.0.1:5000 <br/>

#### GET
/pessoas/ = listar todas as pessoas cadastradas
/pessoas/nome/ = listar todas as atividades geradas para essa pessoa
/atividades/ = listar todas as atividades cadastradas

#### PUT
/pessoas/nome/ = editar a pessoa que possui esse nome

#### DELETE
/pessoas/nome/ = remove a pessoa que possui esse nome

#### POST
/pessoas/ = inserir uma pessoa, type=JSON

```
{
  "id": id_personalizado,
  "nome: "nome da pessoa",
  "idade": idade_da_pessoa
}
```
/atividades/ = inserir uma atividade, type=JSON
```
{
  "id": id_atividade,
  "pessoa": "nome da pessoa",
  "nome": "nome da atividade"
}
```
