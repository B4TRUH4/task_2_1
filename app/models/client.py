from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .city import City
    from .buy import Buy


class Client(Base):
    """Модель клиента"""
    __tablename__ = 'clients'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    city_id: Mapped[int] = mapped_column(ForeignKey('cities.id'))
    email: Mapped[str]

    city: Mapped['City'] = relationship(back_populates='clients')
    buys: Mapped[list['Buy']] = relationship(back_populates='client')
