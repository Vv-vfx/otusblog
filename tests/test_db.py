from app.db_modules.query_db import (
    fill_db_fakes_info,
    get_all_articles_by_author_login,
)
from app.models import create_table
  

def test_create_table():
    # Создаём таблицы
    create_table()


def test_fill():
    # Заполняем базу 25 авторами и статьями
    fill_db_fakes_info()

def test_get_all_articles_by_author_login():
    get_all_articles_by_author_login('maxxx')
    get_all_articles_by_author_login('johnnn')