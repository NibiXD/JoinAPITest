#!/bin/bash
source ../.venv/Scripts/activate


HOST="localhost"
PORT="5432"
USER="postgres"
PASSWORD="postgres"
DB_NAME="join_teste_db"
DJANGO_APP="JoinAPIApp"

echo "Verificando se o banco de dados $DB_NAME existe..."
DB_EXISTS=$(PGPASSWORD="$PASSWORD" psql -h $HOST -p $PORT -U $USER -tAc "SELECT 1 FROM pg_database WHERE datname='$DB_NAME';")
if [ "$DB_EXISTS" != "1" ]; then
  echo "Criando Banco de Dados $DB_NAME"
  PGPASSWORD="$PASSWORD" psql -h $HOST -p $PORT -U $USER -c "CREATE DATABASE $DB_NAME;"
  if [ $? -ne 0 ]; then
    echo "Erro ao criar o banco de dados. Verifique as configurações."
    exit 1
  fi
  echo "Banco de Dados $DB_NAME criado com sucesso!"
else
  echo "O banco de dados $DB_NAME já existe. Pulando criação."
fi
echo "===================================="

# Criando migrations
echo "Criando migrations para $DJANGO_APP"
python manage.py makemigrations $DJANGO_APP
if [ $? -ne 0 ]; then
  echo "Erro ao criar migrations. Verifique o Django e a configuração do banco."
  exit 1
fi
echo "Migrations criadas com sucesso!"
echo "===================================="

# Aplicando migrations
echo "Aplicando migrations"
python manage.py migrate
if [ $? -ne 0 ]; then
  echo "Erro ao aplicar migrations. Verifique o Django e o banco de dados."
  exit 1
fi
echo "Migrations aplicadas com sucesso!"
echo "===================================="

if [ "$DB_EXISTS" != "1" ]; then
  # Alimentando tabelas
  echo "Inserindo dados no banco de dados"
  SQL_CARGO=$(echo "INSERT INTO cargo (nome_cargo) VALUES
  ('Gerente de Projetos'),
  ('Tecnologia da Informação'),
  ('Serviços Gerais'),
  ('Departamento Pessoal');" | iconv -f ISO-8859-1 -t UTF-8)
  PGPASSWORD="$PASSWORD" psql -h $HOST -p $PORT -U $USER -d $DB_NAME -c "$SQL_CARGO"
  if [ $? -ne 0 ]; then
    echo "Erro ao inserir dados no banco. Verifique as tabelas e os dados."
    exit 1
  fi

  SQL_PESSOA=$(echo "INSERT INTO pessoa (nome, admissao, id_cargo) VALUES
  ('Antônio Carlos', '1999-05-10', 1),
  ('Marcos Paulo', '1998-04-05', 2),
  ('Samanta Oliveira', '2005-06-20', 2),
  ('Beatriz Pires', '2003-12-10', 1),
  ('José dos Santos', '1999-01-17', 3),
  ('Maria das Graças', '2007-06-07', 1);" | iconv -f ISO-8859-1 -t UTF-8)
  PGPASSWORD="$PASSWORD" psql -h $HOST -p $PORT -U $USER -d $DB_NAME -c "$SQL_PESSOA"
  if [ $? -ne 0 ]; then
    echo "Erro ao inserir dados no banco. Verifique as tabelas e os dados."
    exit 1
  fi
  echo "Dados inseridos com sucesso!"
  echo "===================================="
fi

python manage.py runserver 0.0.0.0:8000