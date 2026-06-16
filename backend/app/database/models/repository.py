from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from datetime import datetime,timezone

from app.database import Base


class Repository(Base):

    __tablename__ = "repositories"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    github_url: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        unique=True
    )

    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc)
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )
    stars: Mapped[int | None] = mapped_column(
    Integer,
    nullable=True
)

    forks: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    language: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    owner: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    readme_content: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )