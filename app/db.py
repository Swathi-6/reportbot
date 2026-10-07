"""Database connection and session handling."""

from collections.abc import Iterator
from functools import lru_cache

from sqlalchemy import Engine
from sqlmodel import Session, SQLModel, create_engine

from app import config


@lru_cache
def get_engine() -> Engine:
    return create_engine(
        config.DATABASE_URL, # type: ignore
        echo=config.SQL_ECHO,
        pool_pre_ping=True,  # quietly replace dropped connections
    )


def create_tables(engine: Engine | None = None) -> None:
    from app import models  # noqa: F401  (registers the tables)

    SQLModel.metadata.create_all(engine or get_engine())


def get_session() -> Iterator[Session]:
    """FastAPI dependency: one session per request."""
    with Session(get_engine()) as session:
        yield session