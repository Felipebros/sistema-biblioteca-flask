# sistema-biblioteca-flask

## Como executar em Desenvolvimento

```bash
make build-dev
```
```bash
make bash
```
```bash
flask db upgrade
```
```bash
flask run --host=0.0.0.0
```
ou
```bash
make flask-run
```
Depois de executar o flask run, você pode fazer uma requisição POST utilizando sua aplicação preferida Insomnia, Postman ou cURL. O IP e porta aparece no log do flask run.
```json
{
	"titulo": "O Jogo Infinito",
	"editora": "Editora Sextante",
	"foto": "https://image.freepik.com/free-vector/cartoon-world-book-day-illustration_23-2148881001.jpg",
	"autores": ["Simon Sinek", "John Doe"]
}
```
Para descobrir qual é o IP atual do banco de dados Postgres, para conectar nele e verificar os registros salvos e a estrutura do banco de dados.
```bash
make ip-postgres
```

## Como executar em Produção

Leve em consideração este link https://flask.palletsprojects.com/en/2.0.x/tutorial/deploy/
