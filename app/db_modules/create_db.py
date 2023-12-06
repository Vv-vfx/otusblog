import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from app.config.config import (
    TEST_DB_NAME,
    DB_USER,
    BD_PASSWORD,

)


def create_DB():
  
    # Устанавливаем соединение с postgres
    connection = psycopg2.connect(user=DB_USER, password=BD_PASSWORD)
    print("Подключились к postgres")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Создаем курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # удаляем базу, если база существует
    cursor.execute(f'DROP DATABASE IF EXISTS {TEST_DB_NAME}')
    # создаем базу
    cursor.execute(f'create database {TEST_DB_NAME}')
    print("Создали базу")
    # Закрываем соединение
    cursor.close()
    connection.close()

def drop_DB():
    # Устанавливаем соединение с postgres
    connection = psycopg2.connect(user=DB_USER, password=BD_PASSWORD)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Создаем курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Удаляем базу данных
    cursor.execute(f'drop database {TEST_DB_NAME}')
    print("Удалили базу")
    # Закрываем соединение
    cursor.close()
    connection.close()

if __name__=='__main__':
    TEST_DB_NAME = "test_base"
    DB_USER = "postgres"
    BD_PASSWORD = "12345"

    
    create_DB()
    drop_DB()