# SITE CHECKER
Aplicação em python que checa a disponibilidade de site, se o site está online ou offline, através da url.

## Arquivos
Este programa contém os seguintes arquivos:

```
README.md
requirements.txt
.gitignore
sitechecker/
├── checker.py
├── cli.py
├── __init__.py
├── __main__.py
```

`requirements.txt` contém os pacotes utilizados na aplicação.

`checker.py` função que identifica se o site está online ou não.

`cli.py` contém a funcionalidade para receber os argumentos da linha de comando.

`__main__.py` junção de toda a lógica do programa.

`__init__.py` inicialização do pacote.


## Preparar o ambiente

Antes de começar, é recomendado trabalhar em um ambiente virtual. Para criá-lo siga esses passos:
- Para criar um:
```
python -m venv venv
```
- Para ativá-lo:
```
source venv/scripts/activate
```

Agora dentro do ambiente virtual, é preciso instalar os pacotes usados que estão dentro do arquivo `requirements.txt`.
```
pip install -r requirements.txt
```


## Rodando a aplicação

No terminal, através da linha de comando é preciso rodar o seguinte código:
**python -m sitechecker --urls *url desejada***

Como por exemplo:
```
python -m sitechecker --urls google.com
```

Também é possível verificar a disponibilidade de mais de uma url ao mesmo tempo, bastando apenas inserir no mesmo comando.
```
python -m sitechecker --urls indicium.tech python.org
```

## Referência
https://realpython.com/site-connectivity-checker-python/
