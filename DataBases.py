# страницы 6-9)

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30)) #строка из 30 символов
    fullname: Mapped[Optional[str]] #опциональная строка. Может быть пуста
    addresses: Mapped[List["Address"]] = relationship(  #Словарь адресов. Указываем связь с другой таблицей
       back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://postgres:abobaPOST@localhost:5432/ZZZ", echo=True)

Base.metadata.drop_all(engine)    
Base.metadata.create_all(engine)



from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import joinedload

with Session(engine) as session:
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(name="patrick", fullname="Patrick Star")
    session.add_all([spongebob, sandy, patrick])
    session.commit()
    stmt = select(User).options(joinedload(User.addresses))
    for user in session.scalars(stmt):
        print(user)

    


