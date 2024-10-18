# Usando a imagem oficial do Python como base
FROM python:3.9-slim

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiando o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt requirements.txt

# Instalando as dependências
RUN pip install -r requirements.txt

# Copiando o código da aplicação para o contêiner
COPY . .

# Expondo a porta que o Flask vai rodar (5000)
EXPOSE 5000

# Comando para rodar a aplicação Flask
CMD ["python", "app.py"]