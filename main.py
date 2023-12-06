from app.db_modules.create_db import create_DB, drop_DB
from app.db_modules.query_db import (
    fill_db_fakes_info, 
    get_all_articles_by_author_login_v1,
    get_all_articles_by_author_login_v2,
)
from app.models import create_table


def start_app():
    # Удаляем БД и создаём заново
    create_DB()
    # Создаём таблицы
    create_table()
    # Заполняем базу 25 авторами и статьями
    fill_db_fakes_info()
    # Получаем все статьи для конкретных авторов
    get_all_articles_by_author_login_v1('maxxx')
    get_all_articles_by_author_login_v2('johnnn')


if __name__ == '__main__':
    start_app()




