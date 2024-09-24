from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .buy_step import BuyStep


class Step(Base):
    """Модель этапа покупки"""
    __tablename__ = 'steps'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    buy_steps: Mapped[list['BuyStep']] = relationship(back_populates='step')
