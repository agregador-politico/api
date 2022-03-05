# agrega-api
Api central do projeto, o objetivo é que todos os serviços agregadores consumam esta API única.

## Uso

### Docker

```shel
docker-compose build
docker-compose up
```

### Local

```shell
cd app/
pip install -r requirements.txt
python server.py
```

### Testando API:

####  access/

```shell
curl -d '{
  "hash": "x123",
  "origem": "0.0"
}' -H "Content-Type: application/json" -X POST http://localhost:8000/access
```

####  question/

```shell
curl -d '{
  "nome": "Arthur",
  "hash": "x123",
  "id_question": "pergunta-1",
  "answer": "0.0"
}' -H "Content-Type: application/json" -X POST http://localhost:8000/question
```

#### match/

```shell
curl -d '{
  "nome": "Arthur",
  "pergunta-1": "1.0",
  "pergunta-2": "0.0",
  "pergunta-3": "0.5",
  "pergunta-4": "1.0",
  "pergunta-5": "0.0",
  "pergunta-6": "0.5",
  "pergunta-7": "1.0",
  "pergunta-8": "0.0",
  "pergunta-9": "0.5",
  "pergunta-10": "1.0",
  "pergunta-11": "1.0",
  "pergunta-12": "0.0",
  "comentario": "x"
}' -H "Content-Type: application/json" -X POST http://localhost:8000/match

```
