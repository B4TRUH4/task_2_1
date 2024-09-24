from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .client import Client
    from .buy_book import BuyBook
    from .buy_step import BuyStep


class Buy(Base):
    """Модель пожеланий к покупке"""
    __tablename__ = 'buys'
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str]
    client_id: Mapped[int] = mapped_column(ForeignKey('clients.id'))

    client: Mapped['Client'] = relationship(back_populates='buys')
    buy_book: Mapped['BuyBook'] = relationship(back_populates='buy')
    buy_step: Mapped['BuyStep'] = relationship(back_populates='buy')
