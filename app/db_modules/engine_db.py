from sqlalchemy import create_engine

from app.config.config import (
    DSN,
    DB_ECHO,

)

engine = create_engine(
    url=DSN,
    echo=DB_ECHO,
    client_encoding="utf8"
)

