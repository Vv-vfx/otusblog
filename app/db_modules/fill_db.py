from sqlalchemy.orm import Session
from app.db_modules.demo_authors import authors_list

from app.db_modules.engine_db import engine

def fill_db_fakes_info():
    with Session(engine) as session:

        session.add_all(authors_list)
        session.commit()

if __name__ == '__main__':
    fill_db_fakes_info()