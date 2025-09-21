from datetime import datetime
from sqlalchemy import String, ForeignKey, Float, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(128), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    listings: Mapped[list["Listing"]] = relationship(
        "Listing", back_populates="user", cascade="all, delete-orphan"
    )
    favorites: Mapped[list["Favorite"]] = relationship(
        "Favorite", back_populates="user", cascade="all, delete-orphan"
    )


class Listing(Base):
    __tablename__ = "listings"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    price: Mapped[float] = mapped_column(nullable=False)
    area: Mapped[float] = mapped_column(nullable=False)
    floor: Mapped[int] = mapped_column(nullable=False)
    city: Mapped[str] = mapped_column(String(128), nullable=False)
    address: Mapped[str] = mapped_column(String(128), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # ForeignKey
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="listings")

    favorites: Mapped[list["Favorite"]] = relationship(
        "Favorite", back_populates="listing", cascade="all, delete-orphan"
    )


class Favorite(Base):
    __tablename__ = "favorites"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    listing_id: Mapped[int] = mapped_column(ForeignKey("listings.id"))

    user: Mapped["User"] = relationship("User", back_populates="favorites")
    listing: Mapped["Listing"] = relationship("Listing", back_populates="favorites")
