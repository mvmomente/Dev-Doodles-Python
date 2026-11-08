from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base

class User(Base):

    __tablename__ = "users_tb"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(105),
        unique=True,
        nullable=False
    )

    password: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    enable: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )