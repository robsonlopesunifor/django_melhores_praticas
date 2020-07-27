# Dockerfile e visto como arquivo de bloqueio
# bloqueia que tentar criar um ambiente diferente

# Pegar a imagem base
FROM python:3.7

# Definir variáveis de ambiente
#   PYTHONDONTWRITEBYTECODE 1
#       PYTHON DONT WRITE BYTECODE ( NÃO ESCREVA O BYTECODE )
#       python não tentarar gravar arquivos compilador .pyc
ENV PYTHONDONTWRITEBYTECODE 1 
#   PYTHONUNBUFFERED
#       evitar que o docker escodas os logs. 
#       mostrando tudos os logs no console.
ENV PYTHONUNBUFFERED 1

# Definir pasta de trabalho
WORKDIR /code
# Instalar as dependencias 
COPY Pipfile Pipfile.lock /code/
# instala o pipenv ( pipenv e uma env tunada )
# depois instala as dependecias que estao no arquivo pipenv.lock
# esse arquivo e o requirements.txt do pipenv
# --system instala localmente sem gerar virtualenv
# nao faria sentido criar uma virtualenv no docker
RUN pip install pipenv && pipenv install --system
# Copiar o projeto 
COPY . /code/