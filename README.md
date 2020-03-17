>## find-temas
Ferramenta em linha de comando para auxiliar na identificação de temas predefinos em bases de texto

>## como instalar
Clone o repositório e instale via pip

1. `git clone https://github.com/IBPAD/find-temas.git`
2. `cd find-temas`
3. `pip install .`

>### como usar

O uso básico segue a estrutura

`find-temas find "base.csv" "temas.json" "texto" "output.csv"`

Onde "texto" é nome da coluna de texto a ser analisada da base "base.csv", "temas.json" é o arquivo com os termos que definem os temas e "output.csv" é a base csv com as dummies para cada tema. Também é possível usar um arquivo csv para definir os temas através da opção `--csv=True`, como a seguir:

`find-temas find "base.csv" "temas.csv" "texto" "output.csv" --csv=True`

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
            "regex": "Café" 
        }
    ]
}
```

O arquivo de temas csv segue a estrutua:

```csv
mercado,padaria
Extra,Café
pao de acucar,
```