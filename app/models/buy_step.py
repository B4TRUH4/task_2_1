from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .buy import Buy
    from .step import Step


class BuyStep(Base):
    """Модель связи покупки и этапа"""
    __tablename__ = 'buy_steps'
    id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey('buys.id'))
    step_id: Mapped[int] = mapped_column(ForeignKey('steps.id'))
    date_step_beg: Mapped[datetime]
    date_step_end: Mapped[datetime]

    buy: Mapped['Buy'] = relationship(back_populates='buy_step')
    step: Mapped['Step'] = relationship(back_populates='buy_steps')
