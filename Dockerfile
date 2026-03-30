# Conteúdo de Dockerfile
# Use uma imagem base Python oficial
FROM python:3.11-alpine

RUN apk add --no-cache \
    mariadb-connector-c-dev \
    build-base \
    netcat-openbsd
    

# Define o diretório de trabalho dentro do container
WORKDIR /usr/src/app

# Desativa o buffer de saída do Python (melhora o log no Docker)
ENV PYTHONUNBUFFERED=1

# Copia e instala as dependências primeiro para aproveitar o cache do Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# 2. INSTALAR NETCAT (nc) PARA O SCRIPT ENTRYPOINT.SH
# Instalamos o netcat-traditional para garantir que o comando 'nc' funcione com o Alpine Linux



# Copia o restante do código do projeto para o container
COPY . .

# Define o comando padrão para iniciar o Gunicorn (se não usarmos entrypoint)
# Se você for usar o entrypoint.sh para migrações, este CMD será sobrescrito/executado depois.
CMD ["gunicorn", "nome.wsgi:application", "--bind", "0.0.0.0:8000"]