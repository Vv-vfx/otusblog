from app.db_modules.fill_db import fill_db_fakes_info
from app.models import create_table
  
def test_fill():
    print('Создаём таблицы')
    create_table()


def test_fill():
    print('Заполняем базу 25 авторами и статьями')
    fill_db_fakes_info()
   