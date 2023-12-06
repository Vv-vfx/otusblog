from sqlalchemy.orm import Session
from app.db_modules.demo_authors import authors_list
from app.db_modules.engine_db import engine
from sqlalchemy import select

from app.models import (
    Author,
    Articles,
)


def fill_db_fakes_info():
    with Session(engine) as session:
        print('Заполняем базу 25 авторами и статьями')
        session.add_all(authors_list)
        session.commit()
        print('*' * 100)


def get_all_articles_by_author_login_v1(author_login):

    session = Session(engine)

    stmt = select(Author).where(Author.login==author_login)

    print(f"Все статьи для автора с логином {author_login}")
    # print(stmt)
    
    for author in session.scalars(stmt):
        for article in author.articles:
            print(f'Заголовок статьи: "{article.article_heading}"')
            print(f'Тело статьи: "{article.article_body}"')

def get_all_articles_by_author_login_v2(author_login):

    session = Session(engine)

    stmt = session.query(Author).filter(Author.login==author_login).all()

    print(f"Все статьи для автора с логином {author_login}")
    
    for author in stmt:
        for article in author.articles:
            print(f'Заголовок статьи: "{article.article_heading}"')
            print(f'Тело статьи: "{article.article_body}"')


        print(article)


if __name__ == '__main__':
    fill_db_fakes_info()