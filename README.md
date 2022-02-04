# agrega-api
Api central do projeto, o objetivo é que todos os serviços agregadores consumam esta API única.

## Uso

```shell
python server.py
```

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
