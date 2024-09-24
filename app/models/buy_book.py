from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .buy import Buy
    from .book import Book


class BuyBook(Base):
    """Модель связи покупки и книги"""
    __tablename__ = 'buy_books'
    id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey('buys.id'))
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
    amount: Mapped[int]

    buy: Mapped['Buy'] = relationship(back_populates='buy_book')
    book: Mapped['Book'] = relationship(back_populates='buy_books')
