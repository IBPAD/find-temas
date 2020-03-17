>## find-temas

>### como usar

```sh
find-temas find "base.csv" "temas.json" "texto"
```

Onde "texto" é nome da coluna de texto a ser analisada da base "base.csv" e "temas.json" é o arquivo com os termos que definem os temas.

O arquivo "temas.json" segue a estrutura seguinte:

```json
{
    "temas" : [
        {
            "nome": "mercado",
            "regex": "Extra|Pao de Acucar"
        },
        {
            "nome": "padaria",
            "regex": "Cafe" 
        }
    ]
}
```