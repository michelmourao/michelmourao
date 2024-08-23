import psycopg2
from datetime import datetime

# Parâmetros de conexão
conn_params = {
    "dbname": "michelmourao",
    "user": "michelmourao",
    "password": "12345678",
    "host": "localhost",  # ou o endereço do servidor PostgreSQL
    "port": "5432"  # porta padrão do PostgreSQL
}

# Conectar ao banco de dados
try:
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    # Comando SQL para atualizar os dados
    update_query = """
    UPDATE users
    SET username = %s,
        email = %s
    WHERE id = %s;
    """

    create_query = """
    INSERT INTO users (nome, email, created_at)
    VALUES (%s, %s, NOW());
    """

    # Valores a serem passados para o comando SQL
    valores = ('Mike', 'mike@gmail.com')

    # Executar o comando
    cursor.execute(update_query, valores)

    # Confirmar a transação
    conn.commit()

    print("Dados atualizados com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    if conn:
        conn.rollback()  # Reverter a transação em caso de erro

finally:
    # Fechar o cursor e a conexão
    if cursor:
        cursor.close()
    if conn:
        conn.close()
