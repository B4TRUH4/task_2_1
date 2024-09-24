from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from .base import Base

if TYPE_CHECKING:
    from .author import Author
    from .genre import Genre
    from .buy_book import BuyBook


class Book(Base):
    """Модель книги"""
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'))
    genre_id: Mapped[int] = mapped_column(ForeignKey('genres.id'))
    price: Mapped[float]
    amount: Mapped[int]

    author: Mapped['Author'] = relationship(back_populates='books')
    genre: Mapped['Genre'] = relationship(back_populates='books')
    buy_books: Mapped['BuyBook'] = relationship(back_populates='book')
