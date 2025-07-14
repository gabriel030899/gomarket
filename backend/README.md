# gomarket Backend

Este é o backend do projeto **gomarket**, uma aplicação que utiliza Python com SQLAlchemy para interação com banco de dados PostgreSQL.

## Requisitos

- Python 3.8+
- PostgreSQL
- pip (gerenciador de pacotes Python)

## Configuração do Banco de Dados

O backend está configurado para conectar a um banco PostgreSQL com as seguintes credenciais (padrão):

- Host: localhost
- Porta: 5432
- Banco de dados: gomarketdb
- Usuário: gomarket
- Senha: gomarketpass

### Criar banco e usuário no PostgreSQL

Execute os comandos abaixo no terminal do PostgreSQL para criar o banco e o usuário:

```bash
psql -U postgres
```

No prompt do PostgreSQL:

```sql
CREATE DATABASE gomarketdb;
CREATE USER gomarket WITH PASSWORD 'gomarketpass';
GRANT ALL PRIVILEGES ON DATABASE gomarketdb TO gomarket;
```

## Instalação das dependências

1. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

2. Instale as dependências:

```bash
pip install sqlalchemy psycopg2-binary
```

> Caso seu projeto tenha outras dependências, adicione-as no comando acima ou crie um arquivo `requirements.txt`.

## Rodando o backend

Você pode testar a conexão com o banco de dados executando o script de teste:

```bash
python backend/test_connection.py
```

Se a conexão for bem sucedida, verá a mensagem:

```
Conexao bem sucedida
```

## Estrutura do projeto

- `backend/app/database.py`: Configuração da conexão com o banco de dados usando SQLAlchemy.
- `backend/test_connection.py`: Script para testar a conexão com o banco.

## Observações

- Certifique-se que o PostgreSQL está rodando e acessível na porta 5432.
- Ajuste a variável `DATABASE_URL` em `backend/app/database.py` caso utilize outras credenciais ou host.

---

Se precisar de ajuda adicional, fique à vontade para perguntar!