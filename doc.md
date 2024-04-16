Estrutura de projetos de dados do Zero

1 - Escolher a versão do python:
python --version (traz o python global)
recomendado utilizar a mais moderna, ao menos que seja necessario outra
pyenv local python-version (Define o python que sera usado dentro do diretorio
que foi dado o comando)

2 - Gestão do ambiente virtual

poetry config virtualenvs.in-project true
poetry init
poetry shell (inicia o ambiente)

3 - GIT

4 - Teste
pytest

5 - Padrão de projeto

isort - organiza as bibliotecas (imports)

isort .

blue - Organiza código

blue .

Ambas acima seguem o padrão pep8, e ja formatam automticamente

temos tambem a flake8 - Esse olha todos os arquivos é ve oq esta fora da pep8 e aponta

MKDocs vamos usar para realizar a dococumentação do nosso projeto.


6 - Hooks (pre commit)

Nos ajuda com dor de cabeca, ele roda o código antes do commit rodar
